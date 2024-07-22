import os,sys 
from src.compoenets.data_ingestion import DataIngestionConfig,DataIngestion   
from src.Logging import logging
from src.Exception import CustomException 

injector = DataIngestion() 

injector.initialize_data_ingestion() 