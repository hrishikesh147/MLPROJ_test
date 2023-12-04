import os
from pathlib import Path
from src.mlproject1 import logger
import urllib.request as request
import zipfile
from src.mlproject1.entity.config_entity import DataIngestionConfig
from src.mlproject1.utils.common import create_directories,read_yaml
from src.mlproject1.constants import *  

class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config
        print(f"DataIngestion Config: {config}")

    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            filename,header=request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloadad")

        else:
            logger.info(f"File already exists")

    def extract_zip_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file,'r') as zipf:
            zipf.extractall(unzip_path)