from sklearn.linear_model import ElasticNet
import pandas as pd
from pathlib import Path
import joblib
import os
from src.mlproject1.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig):
        self.config=config
        
    def train(self):

        train_data=pd.read_csv("artifacts/data_transformation/train.csv")
        test_data=pd.read_csv("artifacts/data_transformation/test.csv")

        X_train=train_data.drop(['quality'],axis=1)
        y_train=train_data[['quality']]

        X_test=test_data.drop(['quality'],axis=1)
        y_test=test_data[['quality']]

        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
        lr.fit(X_train, y_train)

        joblib.dump(lr,os.path.join(self.config.root_dir,self.config.model_name))


