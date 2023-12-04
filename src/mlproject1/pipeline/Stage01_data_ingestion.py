from src.mlproject1.config.configuration import ConfigurationManager
from src.mlproject1.entity.config_entity import DataIngestionConfig
from src.mlproject1.components.data_ingestion import DataIngestion
from src.mlproject1 import logger

STAGE_NAME="Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        conf=ConfigurationManager()
        data_ingest=conf.get_data_ingestion_config()
        data_in=DataIngestion(data_ingest)
        data_in.download_data()
        data_in.extract_zip_file()

if __name__=='__main__':
    try:
        logger.info(f"{STAGE_NAME} started...")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} completed..")

    except Exception as e:
        raise e