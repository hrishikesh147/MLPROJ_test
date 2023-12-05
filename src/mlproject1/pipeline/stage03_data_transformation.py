from src.mlproject1.config.configuration import ConfigurationManager
from src.mlproject1.components.data_transformation import DataTransformation
from pathlib import Path
from src.mlproject1 import logger

STAGE_NAME="DATA TRANSFORMATION"

class Datatransformationtrainingpipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"),'r') as f:
                status=f.read().split(" ")[-1]

            if status=="True":
                conf=ConfigurationManager()
                data_trans=conf.get_data_transformation_config()
                data_t=DataTransformation(config=data_trans)
                data_t.train_test_split()
            else:
                logger.info("Schema is not correct, Cannot Proceed...")
        except Exception as e:
            raise e

        
