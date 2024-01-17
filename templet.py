import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s')

project_name = "MLflow"

list_of_files = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/component/__init__.py",
    f"src/{project_name}/component/data_ingestion.py",
    f"src/{project_name}/component/data_tranformation.py",
    f"src/{project_name}/component/model_trainer.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/train_pipeline.py",
    f"src/{project_name}/pipeline/predict_pipeline.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/utile.py",
    "requirment.txt",
    "setup.py"
    
    ]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info("file created")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info("created")
    else:
        logging.info('ready')