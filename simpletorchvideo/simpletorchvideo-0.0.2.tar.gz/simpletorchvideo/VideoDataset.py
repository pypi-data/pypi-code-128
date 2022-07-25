import logging
import random

from torch.utils.data import Dataset

from .reader import VideoReader

logger = logging.getLogger('VideoDataset')


class VideoDataset(Dataset):
    """
    Reading the training Vimeo dataset
    key example: train/00001/0001/im1.png
    """

    def __init__(self, video_reader: VideoReader, num_frames=7, random_reverse=True):
        super(VideoDataset, self).__init__()
        self.reader = video_reader
        self.num_frames = num_frames

        # temporal augmentation
        self.random_reverse = random_reverse
        logger.info('Temporal augmentation with random reverse is {}.'.format(self.random_reverse))

        self.video_list = self.reader.list_videos()
        self.len = sum([len(video) // num_frames for video in self.video_list])

    def __len__(self):
        return self.len

    def __getitem__(self, index):
        frame_index = index * self.num_frames

        # Get frame list
        frames = []
        for i in range(len(self.video_list)):
            if 0 <= frame_index <= len(self.video_list[i]) - self.num_frames:
                image_paths = self.video_list[i][frame_index:frame_index + self.num_frames]
                logger.debug("Reading images: %s" % image_paths)
                frames.extend(self.reader.read_images(image_paths))
                break
            else:
                frame_index = frame_index - (len(self.video_list[i]) - len(self.video_list[i]) % self.num_frames)
        if self.random_reverse and random.random() < 0.5:
            frames.reverse()
        return frames
