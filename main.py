from networksecurity.components.data_ingestion import DataIngestion
#from networksecurity.components.data_validation import DataValidation
#from networksecurity.components.data_transformation import DataTransformation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.loging import logging
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig,DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

import sys

#from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.entity.config_entity import ModelTrainerConfig

if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig) 
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data initiation Completed")
        print(dataingestionartifact) 
        

    except Exception as e:
        raise NetworkSecurityException(e,sys)