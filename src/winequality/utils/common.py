import os
import json
import yaml
import joblib
from src.winequality import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from box.exceptions import BoxValueError
from typing import Any

## function to read yaml file
@ensure_annotations
def real_yaml(path_to_yaml: Path)->ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f" yaml file {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ("yaml file is empty")
    except Exception as e:
        raise e
    
## function to create file/directories
@ensure_annotations
def create_directories(path_to_directories:list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info("created directory at: {path}")

## function to save data in json file
@ensure_annotations
def save_json(path:Path, data:dict):
    with open(path,"w") as f:
        json.dump(data,f,indent=4)
    logger.info(f"json file saved at : {path}")

## function to load json file
@ensure_annotations
def load_json(path:Path)->ConfigBox:
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded successfully from : {path}")
    return ConfigBox(content)

## save model using joblib
@ensure_annotations
def save_bin(data:Any,path:Path):
    joblib.dump(value=data,filename=Path)
    logger.info(f"Binary file saved at : {path}")

## load model using joblib
@ensure_annotations
def load_bin(path:Path)->Any:
    data = joblib.load(path)
    logger.info(f"Binary file loaded from : {path}")
    return data