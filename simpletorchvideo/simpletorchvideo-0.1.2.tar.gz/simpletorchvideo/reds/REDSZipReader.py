import numpy as np
from simpletorchvideo.reader import VideoReader, ZipImageReader
from .util import *


class REDSZipReader(VideoReader):
    def __init__(self, zip_path: str, root: str):
        """Read a Vimeo dataset zip file.
        :param zip_path: path to REDS dataset zip file.
        :param root: path to REDS dataset file in zip. its sub dir should be <video index>/<frame index>.png. e.g. "test/test_sharp_bicubic/X4" in test_sharp_bicubic.zip
        """
        super().__init__()
        self.reader = ZipImageReader(zip_path)
        self.root = self._format_path(root) + '/'
        assert self.valid(), "Not a valid REDS zip"

    def valid(self) -> bool:
        if not self.reader.valid():
            return False
        try:
            if self.reader.getinfo(self.root) is None:
                return False
            return True
        except:
            return False

    @staticmethod
    def _format_path(path):
        path = path.replace("\\", "/")
        path = path[1:] if path[0] == "/" else path
        path = path[0:-1] if path[-1] == "/" else path
        return path

    def read_images(self, paths: [str]) -> [np.ndarray]:
        return [self.reader.read_image(self.root + self._format_path(path)) for path in paths]

    def list_videos(self) -> [[str]]:
        return parse_video_list_from_image_list([p.replace(self.root, '') for p in self.reader.list_images(self.root)])
