"""
Presubmission script to export ass files.

To write your own presubmission script, use this as a jumping off point and
consult the Conductor Max reference documentation.
https://docs.conductortech.com/reference/max/#pre-submission-script
"""

from contextlib import contextmanager
from pymxs import runtime as rt
import os
import fileinput
import sys
from ciopath.gpath import Path

# Color manager removal stuff
CM_SEARCHING = 0
CM_REMOVING = 1
CM_DONE = 2
CM_OPT = " color_manager "
CM_START = "color_manager_ocio"
CM_END = "}"


@contextmanager
def preserve_state():
    """
    Remember, and then reset all the properties we change.
    """
    rend_time_type = rt.rendTimeType
    rend_pickup_frames = rt.rendPickupFrames
    rend_nth_frame = rt.rendNThFrame
    rend_export_to_ass = rt.renderers.current.export_to_ass
    rend_ass_file_path = rt.renderers.current.ass_file_path
    rend_abort_on_error = rt.renderers.current.abort_on_error
    try:
        rend_compatibility_mode = rt.renderers.current.legacy_3ds_max_map_support
    except AttributeError:
        try:
            rend_compatibility_mode = rt.renderers.current.compatibility_mode
        except AttributeError:
            rend_compatibility_mode = 0
    try:
        yield
    finally:
        rt.rendTimeType = rend_time_type
        rt.rendPickupFrames = rend_pickup_frames
        rt.rendNThFrame = rend_nth_frame
        rt.renderers.current.export_to_ass = rend_export_to_ass
        rt.renderers.current.ass_file_path = rend_ass_file_path
        rt.renderers.current.abort_on_error = rend_abort_on_error
        try:
            rt.renderers.current.compatibility_mode = rend_compatibility_mode
        except AttributeError:
            try:
                rt.renderers.current.legacy_3ds_max_map_support = rend_compatibility_mode
            except AttributeError:
                pass


def main(dialog, *args):
    """
    Export assets needed for a ass render.

    We need the ass files, and we need file that defines mappings between the
    Windows paths and linux paths on the render nodes. This mapping is always
    simply removing a drive letter.
    """
    prefix = args[0]
    export_ass_files(dialog, prefix)
    write_remap_file(dialog, prefix)

    return amendments(dialog, *args)


def amendments(dialog, *args):
    """
    Return payload amendments only.

    Payload amendments consist of ass filenames, a remap file, and an environment variable that
    points to the remap file.
    """
    prefix = args[0]
    remap_filename = "{}.json".format(prefix.strip("."))

    main_sequence = dialog.main_tab.section("FramesSection").main_sequence
    ass_filenames = main_sequence.expand("{}####.ass".format(prefix))

    upload_paths = ass_filenames + [remap_filename]

    # NOTE environment must be the following object list, not: bash, i.e. NAME=value1:value2
    # merge_policy can be exclusive|append
    environment = [
        {
            "name": "ARNOLD_PATHMAP",
            "value": Path(remap_filename).fslash(with_drive=False),
            "merge_policy": "exclusive",
        }
    ]

    return {"upload_paths": upload_paths, "environment": environment}


def export_ass_files(dialog, ass_file_prefix):
    """
    Write ass files with the given prefix.

    NOTE The prefix should probably include a trailing dot since kick doesn't
    add one before the frame numbers.
    """
    render_scope = dialog.render_scope
    if not render_scope.__class__.__name__ == "ArnoldRenderScope":
        raise TypeError(
            "If you want to export ass files, please set the current renderer to Arnold."
        )

    main_sequence = dialog.main_tab.section("FramesSection").main_sequence

    camera_name = dialog.main_tab.section("GeneralSection").camera_component.combobox.currentText()
    print("Set the current view to look through camera: {}", format(camera_name))
    rt.viewport.setCamera(rt.getNodeByName(camera_name))

    print("Ensure directory is available for ass files")
    _ensure_directory_for(ass_file_prefix)

    print("Closing render setup window if open...")
    if rt.renderSceneDialog.isOpen():
        rt.renderSceneDialog.close()

    with preserve_state():
        print("Setting render time type to use a specified sequence...")
        rt.rendTimeType = 4

        print("Setting the frame range...")
        rt.rendPickupFrames = "{}-{}".format(main_sequence.start, main_sequence.end)

        print("Setting the by frame to 1...")
        rt.rendNThFrame = 1

        print("Setting ass export to on...")
        rt.renderers.current.export_to_ass = True

        print("Setting the ass filepath to", "{}.ass".format(ass_file_prefix))
        rt.renderers.current.ass_file_path = "{}.ass".format(ass_file_prefix)

        print("Setting abort on error to off...")
        rt.renderers.current.abort_on_error = False

        print("Setting compatibility_mode to Arnold compliant...")
        rt.renderers.current.compatibility_mode = 0

        print("Exporting ass files...")
        rt.render(fromFrame=main_sequence.start, toFrame=main_sequence.end, vfb=False)

        # return list of ass files
        print("Done writing ass files")
        ass_filenames = main_sequence.expand("{}####.ass".format(ass_file_prefix))

    print("Removing color manager entries from ass files...")
    sw_version = dialog.main_tab.section("SoftwareSection").component.combobox.currentText()
    if sw_version.split()[1].startswith("5"):
        for filename in ass_filenames:
            remove_color_manager(filename)
    print("Done removing color manager entries from ass files")
    return ass_filenames


def remove_color_manager(fn):
    """
    Arnold 7.x puts an unwanted color manager block in the ass.

    On linux, it causes the render to fail. This code removes it and the line in options that
    referrs to it.

    Logic for each line:
        * If we're done replacing stuff, just write the line.
        * If we are removing (started but not finished) then don't write the line, but check for the
          end marker and if present, flip to done stage.
        * Otherwise, we haven't started yet, so search fro the start marker. Also in this stage,
          remove the reference in the options block.
    """
    stage = CM_SEARCHING
    with fileinput.input(fn, inplace=True) as fileobj:
        for line in fileobj:
            if stage == CM_DONE:
                sys.stdout.write(line)
            elif stage == CM_REMOVING:
                if line.startswith(CM_END):
                    stage = CM_DONE
            else:  # stage == CM_SEARCHING
                if line.startswith(CM_START):
                    stage = CM_REMOVING
                else:
                    if not line.startswith(CM_OPT):
                        sys.stdout.write(line)


def write_remap_file(_, prefix):
    """
    Write a json file that tells Arnold to strip drive letters.

    This was introduced in Arnold 6.0.4.0 (mtoa 4.0.4). The file is pointed to
    by the ARNOLD_PATHMAP environment variable.
    """

    remap_filename = "{}.json".format(prefix.strip("."))

    lines = []
    lines.append("{\n")
    lines.append('\t"linux": {\n')
    lines.append('\t\t"^[A-Za-z]:": "",\n')
    lines.append('\t\t"^//":"/"\n')
    lines.append("\t}\n")
    lines.append("}\n")

    with open(remap_filename, "w") as fn:
        fn.writelines(lines)

    print("Wrote Arnold remapPathFile file to", remap_filename)

    return remap_filename


def _ensure_directory_for(path):
    """
    Ensure that the parent directory of `path` exists
    """
    dirname = os.path.dirname(path)
    if not os.path.isdir(dirname):
        os.makedirs(dirname)
