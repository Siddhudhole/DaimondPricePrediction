import os ,sys 
import pandas as pd 
from sklearn.model_selection import train_test_split 
from src.Logging import logging 
from src.Exception import CustomException 
from dataclasses import dataclass 


@dataclass
class DataIngestionConfig:
    raw_data_path = os.path.join('artifacts', 'raw_data.csv') 
    train_data_path = os.path.join('artifacts','train_data.csv')
    test_data_path = os.path.join('artifacts','test_data.csv')


class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig()

    
    def initialize_data_ingestion(self):
        try:
            logging.info("Initializing data ingestion") 
            df = pd.read_csv("Notebook\\Dataset\\diamonds.csv") 

        except Exception as e :
            logging.error(f"Error initializing data ingestion : {e}") 
            raise CustomException(e,sys)   
        
        else :
            os.makedirs('artifacts',exist_ok=True,)
            df.to_csv(self.config.raw_data_path, index=False)
            logging.info("Data ingestion initialized successfully") 
            train_data,test_data = train_test_split(df,test_size=0.2,random_state=123)   
            train_data.to_csv(self.config.train_data_path, index=False)
            test_data.to_csv(self.config.test_data_path, index=False) 
            logging.info("Data split into training and test sets") 
            return self.config.train_data_path,self.config.test_data_path  
            






        
 