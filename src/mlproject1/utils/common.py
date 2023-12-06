from pathlib import Path
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
import yaml
import os
from src.mlproject1 import logger
import json
import joblib

@ensure_annotations
def read_yaml(path_yaml: Path) -> ConfigBox:
    try:
        with open(path_yaml) as yaml_f:
            yaml_content = yaml.safe_load(yaml_f)
            logger.info(f"read yaml file {path_yaml}")
            return ConfigBox(yaml_content)
        
    except BoxValueError:
        raise ValueError("yaml file in empty")
    
    except Exception as e:
        raise e
        
@ensure_annotations
def create_directories(path_dir: list,verbose=True):
    for i in path_dir:
        os.makedirs(i,exist_ok=True)
        if verbose:
            logger.info(f"created directory at {i}")


def save_json(data, json_path: Path):
    with open(json_path, 'w') as json_file:
        json.dump(data, json_file)


@ensure_annotations
def load_json(json_path : Path) -> ConfigBox:
    with open(json_path,'r') as f:
        content=json.load(f)

        logger.info(f"successfully loaded json path {f}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path):
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) ->str:
    size_kb=round(os.path.getsize(path)/1024)
    return f"size in kb : {size_kb}"


    

