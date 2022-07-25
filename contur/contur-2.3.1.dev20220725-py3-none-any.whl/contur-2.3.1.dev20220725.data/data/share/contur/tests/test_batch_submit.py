try:
    import yoda, rivet, contur
except:
    print("Exiting test suite, could not find the dependencies of YODA, Rivet or contur in PYTHONPATH")
    raise

import os
import shutil

import pytest
import yaml

from test_executables import build_executable_cmd
from contur.run.run_batch_submit import batch_submit
from contur.run.arg_utils import get_args
from contur.util.utils import generate_rivet_anas
import contur.config.config as cfg


test_dir = os.path.dirname(os.path.abspath(__file__))

args_path = os.path.join(test_dir, 'sources/batch_cl_args.yaml')
with open(args_path, 'r') as f:
    arguments_examples = yaml.load(f, yaml.FullLoader)

output_dir = os.path.join(test_dir,"tmp_batch")
try:
    os.makedirs(output_dir) #, exist_ok=True) #< exist_ok requires Py > 3.2
except:
    pass

@pytest.mark.first
def test_generate_rivet_anas():
    cfg.output_dir = output_dir
    # Set up logger
    cfg.setup_logger("contur_mkana.log")
    generate_rivet_anas(False)

main_run_cmds = {}

for k,v in arguments_examples.items():
    cmd = build_executable_cmd(v)
    parser = get_args(cmd[1:],'batchsub')
    main_run_cmds[k] = get_args(cmd[1:],'batchsub')

@pytest.mark.parametrize("fixture", main_run_cmds.values(), ids=main_run_cmds.keys())
def test_run_main(fixture):
    batch_submit(fixture)

@pytest.mark.last
def test_teardown_module():
    """Clean up test area"""
    shutil.rmtree(os.path.join(test_dir, 'tmp_batch'))
