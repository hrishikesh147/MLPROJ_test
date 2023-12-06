from src.mlproject1 import logger
from src.mlproject1.pipeline.Stage01_data_ingestion import DataIngestionTrainingPipeline
from src.mlproject1.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from src.mlproject1.pipeline.stage03_data_transformation import Datatransformationtrainingpipeline
from src.mlproject1.pipeline.stage02_model_trainer import ModelTrainertrainingpipeline
from src.mlproject1.pipeline.stage05_model_evaluation import ModelEvaluationTrainingPipeline


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


STAGE_NAME="Data Transformation Stage"

try:
    logger.info(f"{STAGE_NAME} started...")
    obj=Datatransformationtrainingpipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} completed...")

except Exception as e:
    raise e


STAGE_NAME="MODEL TRAINER"

try:
    logger.info(f"{STAGE_NAME} started...")
    obj=ModelTrainertrainingpipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} completed...")
except Exception as e:
    raise e

STAGE_NAME="Data Evaluation Stage"

try:
    logger.info(f"{STAGE_NAME} started...")
    obj=ModelEvaluationTrainingPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} completed...")
except Exception as e:
    raise e



