import os
import logging
from logging.config import dictConfig
from utils.config import config

### Add Trace lvl for uvicorn
TRACE_LEVEL = 5
logging.addLevelName(TRACE_LEVEL, "TRACE")

def trace(self, message, *args, **kwargs):
    if self.isEnabledFor(TRACE_LEVEL):
        self._log(TRACE_LEVEL, message, args, **kwargs)

logging.Logger.trace = trace

def parse_size_string(size_string: str) -> int:
    size_units = {'KB': 1024, 'MB': 1024 ** 2, 'GB': 1024 ** 3}
    
    size_string = size_string.upper().strip()
    
    for unit in size_units.keys():
        if size_string.endswith(unit):
            size_part = size_string[:-len(unit)]
            try:
                return int(size_part) * size_units[unit]
            except ValueError:
                raise ValueError(f"Invalid size number: {size_part}")
    raise ValueError(f"Invalid logs_rotation_size format: {size_string}")

def set_up_logger(
    log_lvl: str = "INFO",
    log_save: bool = False,
    log_path: str = "logs/logs.log",
    log_rotation: bool = True,
    log_rotation_size: str = '50MB',
    log_backups_count: int = 5

) -> logging.Logger:

    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "[\033[90m%(asctime)s\033[m]%(log_color)s |%(log_color)-10s%(levelname)-8s|%(reset)s \033[1;97m%(message)s\033[m",
                "datefmt": "%Y-%m-%d %H:%M:%S",
                "()": "colorlog.ColoredFormatter",
                "log_colors": {
                    'INFO': 'bold_green',
                    'WARNING': 'bold_yellow',
                    'ERROR': 'bold_red',
                    'CRITICAL': 'bold_purple',
                    'DEBUG': 'bold_cyan',
                    'TRACE': 'bold_light_blue'
                },
            },
            "file": {
                "format": "[{asctime}] [{levelname}]: {message} - {filename}",
                "datefmt": "%Y-%m-%d %H:%M:%S",
                "style": "{",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
                "level": log_lvl.upper(),
            },
        },
        "loggers": {
            "": {
                "handlers": ["console"],
                "level": log_lvl.upper(),
                "propagate": False,
            },
            "uvicorn": {
                "handlers": ["console"],
                "level": log_lvl.upper(),
                "propagate": False,
            },
            "uvicorn.error": {
                "handlers": ["console"],
                "level": log_lvl.upper(),
                "propagate": False,
            },
            "uvicorn.access": {
                "handlers": ["console"],
                "level": log_lvl.upper(),
                "propagate": False,
            },
        },
    }

    if log_save:
        if log_rotation:
            logging_config["handlers"]["file"] = {
                "class": "logging.handlers.RotatingFileHandler",
                "formatter": "file",
                "filename": log_path,
                "maxBytes": parse_size_string(log_rotation_size),
                "backupCount": log_backups_count,
                "level": log_lvl.upper(),
                "encoding": "utf-8",
            }
        else:
            logging_config["handlers"]["file"] = {
                "class": "logging.FileHandler",
                "formatter": "file",
                "filename": log_path,
                "level": log_lvl.upper(),
                "encoding": "utf-8",
            }
        
        for logger_name in logging_config["loggers"]:
            logging_config["loggers"][logger_name]["handlers"].append("file")
        
        logs_dir = os.path.dirname(log_path)
        if logs_dir and not os.path.exists(logs_dir):
            os.makedirs(logs_dir)

    dictConfig(logging_config)
    logger = logging.getLogger(__name__)
    logger.info("------------------------------------------------------")
    logger.info(config)

    logger.info("------------------------------------------------------")
    if log_save:
        logger.info(f"📝 Log save is enabled. Logs will be saved to {log_path} file")
        logger.info("------------------------------------------------------")
        if log_rotation:
            logger.warning(f"🔥 Log file size to trigger the rotation: {log_rotation_size}.")
            logger.info("------------------------------------------------------")
            logger.warning(f"📂 Log file backups count: {log_backups_count}")
        else:
            logger.warning(f"❗ Log file will not be rotated.")
    else:
        logger.info(f"❗ Built in log backups are disabled")
    logger.info("------------------------------------------------------")

    return logger

logger = set_up_logger(log_lvl=config.Logs.level,
                        log_save=config.Logs.save,
                        log_path=os.getenv("CONFIG_PATH") or config.Logs.file_path,
                        log_rotation=config.Logs.rotation,
                        log_rotation_size=config.Logs.rotation_size,
                        log_backups_count=config.Logs.backups_count,
                        )
