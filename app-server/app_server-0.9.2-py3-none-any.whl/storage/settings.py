from os.path import abspath

API_ENDPOINT = "/storage/v1"
UPLOAD_API_ENDPOINT = "/upload/storage/v1"
BATCH_API_ENDPOINT = "/batch/storage/v1"
DOWNLOAD_API_ENDPOINT = "/download/storage/v1"

# pyfilesystem assumes OS fs within CWD as base
STORAGE_BASE = abspath("./")
STORAGE_DIR = ".cloudstorage"
