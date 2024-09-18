import yaml
import os
from pydantic import BaseModel, HttpUrl, ValidationError, Field
from typing_extensions import Annotated
from typing import Literal

class App(BaseModel):
    version: str
    # host: str
    # port: Annotated[int, Field(ge=0, le=65535)]
    swagger: bool = True
    swagger_path: str
    swagger_title: str
    swagger_description: str

class Chain(BaseModel):
    rpc: HttpUrl

class Logs(BaseModel):
    level: Literal['TRACE', 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    save: bool
    file_path: Annotated[str, Field(min_length=1, description="Path to the log file")]
    rotation: bool
    rotation_size: Annotated[str, Field(pattern=r'^\d+(KB|MB|GB)$', description="Log size to trigger the rotation [KB/MB/GB]")]
    backups_count: int

class Config(BaseModel):
    App: App
    Chain: Chain
    Logs: Logs

def load_config(file_path) -> Config: 
    try:
        with open(file_path, 'r') as file:
            config_dict = yaml.safe_load(file)
            return Config(**config_dict)
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file '{file_path}' not found.")
    except ValidationError as e:
        raise ValidationError(f"Configuration validation error: {e}")
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"YAML parsing error: {e}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred while loading the configuration: {e}")

config = load_config(os.getenv('CONFIG_PATH') or 'config.yaml')