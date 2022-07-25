"""Authors: Cody Baker and Ben Dichter."""
from abc import abstractmethod, ABC
from typing import Optional

from pynwb import NWBFile

from .utils import get_base_schema, get_schema_from_method_signature


class BaseDataInterface(ABC):
    """Abstract class defining the structure of all DataInterfaces."""

    @classmethod
    def get_source_schema(cls):
        """Infer the JSON schema for the source_data from the method signature (annotation typing)."""
        return get_schema_from_method_signature(cls.__init__, exclude=["source_data"])

    @classmethod
    def get_conversion_options_schema(cls):
        """Infer the JSON schema for the conversion options from the method signature (annotation typing)."""
        return get_schema_from_method_signature(cls.run_conversion, exclude=["nwbfile", "metadata"])

    def __init__(self, **source_data):
        self.source_data = source_data

    def get_metadata_schema(self):
        """Retrieve JSON schema for metadata."""
        metadata_schema = get_base_schema(
            id_="metadata.schema.json",
            root=True,
            title="Metadata",
            description="Schema for the metadata",
            version="0.1.0",
        )
        return metadata_schema

    def get_metadata(self):
        """Child DataInterface classes should override this to match their metadata."""
        return dict()

    def get_conversion_options(self):
        """Child DataInterface classes should override this to match their conversion options."""
        return dict()

    @abstractmethod
    def run_conversion(
        self,
        nwbfile_path: Optional[str] = None,
        nwbfile: Optional[NWBFile] = None,
        metadata: Optional[dict] = None,
        overwrite: bool = False,
        **conversion_options,
    ):
        """
        Run the NWB conversion for the instantiated data interface.

        Parameters
        ----------
        nwbfile_path: FilePathType
            Path for where to write or load (if overwrite=False) the NWBFile.
            If specified, the context will always write to this location.
        nwbfile: NWBFile, optional
            An in-memory NWBFile object to write to the location.
        metadata: dict, optional
            Metadata dictionary with information used to create the NWBFile when one does not exist or overwrite=True.
        overwrite: bool, optional
            Whether or not to overwrite the NWBFile if one exists at the nwbfile_path.
            The default is False (append mode).
        verbose: bool, optional
            If 'nwbfile_path' is specified, informs user after a successful write operation.
            The default is True.
        """
        raise NotImplementedError("The run_conversion method for this DataInterface has not been defined!")
