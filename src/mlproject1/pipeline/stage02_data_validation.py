from src.mlproject1.config.configuration import ConfigurationManager
from src.mlproject1.entity.config_entity import DataValidationConfig
from src.mlproject1.components.data_validation import DataValidation
from src.mlproject1 import logger

STAGE_NAME="Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            con=ConfigurationManager()
            data_val=con.get_data_validation_config()
            data_v=DataValidation(config=data_val)
            data_v.validate_all_columns()
        except Exception as e:
            raise e
        
if __name__=='__main__':
    try:
        logger.info(f"{STAGE_NAME} started...")
        obj=DataValidationTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} completed...")

    except Exception as e:
        raise e