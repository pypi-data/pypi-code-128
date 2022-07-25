from dcentrapi.common import get_dapi_version


class Base:

    def __init__(self, stage, key):
        self.key = key
        self.headers = {'X-API-KEY': self.key}
        self.__version__ = get_dapi_version()

        if stage == 'develop':
            self.url = "https://test-api.dcentralab.com/"
        if stage == 'staging':
            self.url = "https://staging-api.dcentralab.com/"
