from src.mlproject1 import logger
from src.mlproject1.config.configuration import ConfigurationManager
from src.mlproject1.components.model_trainer import ModelTrainer

STAGE_NAME="MODE: TRAINER"

class ModelTrainertrainingpipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            con=ConfigurationManager()
            get_model_t=con.get_model_trainer()
            model_tr1=ModelTrainer(config=get_model_t)
            model_tr1.train()
        except Exception as e:
            raise e

if __name__=="__main__":
    logger.info(f"Stage {STAGE_NAME} started")
    obj=ModelTrainertrainingpipeline()
    obj.main()
    logger.info(f"Stage {STAGE_NAME} Completed...")