from  setuptools import setup, find_packages 
from typing import List 


def get_packages(file_path:str)->List[str]:
    packages = [] 
    try :
        with open(file_path) as f :
            package = f.readlines()
        packages = [ req.replace("\n","") for req in package ]
        packages.remove("-e . ")

        return packages 

    except FileNotFoundError as e :
        print(f"File not found : {e}")  









setup(
    name="DiamodPricePrediction",
    version="1.0.0",
    author="Siddhart Dhole",
    author_email="shidhudhole9322@gmail.com",
    install_requires =get_packages('Requirements.txt') , 
    packages=find_packages(),
    description="Predicting Diamond Prices based on various factors",
    url="https://github.com/yourusername/DiamodPricePrediction",

)

