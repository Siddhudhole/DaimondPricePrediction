import os,sys 
from src.compoenets.data_ingestion import DataIngestionConfig,DataIngestion   
from src.Logging import logging
from src.Exception import CustomException 

obj = DataIngestion()
train_data_path,test_data_path = obj.initialize_data_ingestion() 
print(train_data_path)
print(test_data_path) 