"""Script to download HadCRUT5 version 5.0.1.0 from its webpage."""
import logging
import os

from esmvaltool.cmorizers.data.downloaders.wget import WGetDownloader

logger = logging.getLogger(__name__)


def download_dataset(config, dataset, dataset_info, start_date, end_date,
                     overwrite):
    """Download dataset.

    Parameters
    ----------
    config : dict
        ESMValTool's user configuration
    dataset : str
        Name of the dataset
    dataset_info : dict
         Dataset information from the datasets.yml file
    start_date : datetime
        Start of the interval to download
    end_date : datetime
        End of the interval to download
    overwrite : bool
        Overwrite already downloaded files
    """
    downloader = WGetDownloader(
        config=config,
        dataset=dataset,
        dataset_info=dataset_info,
        overwrite=overwrite,
    )

    os.makedirs(downloader.local_folder, exist_ok=True)
    downloader.download_file(
        "https://crudata.uea.ac.uk/cru/data/temperature/"
        "HadCRUT.5.0.1.0.analysis.anomalies.ensemble_mean.nc",
        wget_options=[])
    downloader.download_file(
        "https://crudata.uea.ac.uk/cru/data/temperature/"
        "absolute_v5.nc",
        wget_options=[])
    downloader.download_file(
        "https://crudata.uea.ac.uk/cru/data/temperature/"
        "HadCRUT.5.0.1.0.anomalies.ensemble_mean.nc",
        wget_options=[])
    downloader.download_file(
        "https://crudata.uea.ac.uk/cru/data/temperature/absolute.nc",
        wget_options=[])
