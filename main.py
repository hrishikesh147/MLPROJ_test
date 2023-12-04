from src.mlproject1 import logger
from src.mlproject1.pipeline.Stage01_data_ingestion import DataIngestionTrainingPipeline
from src.mlproject1.pipeline.stage02_data_validation import DataValidationTrainingPipeline


STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f"{STAGE_NAME} started...")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} completed...")

except Exception as e:
    logger.error(f"An error occured: {e}")
    raise e
    
STAGE_NAME="Data Validation Stage"

try:
        logger.info(f"{STAGE_NAME} started...")
        obj=DataValidationTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} completed...")

except Exception as e:
    raise e