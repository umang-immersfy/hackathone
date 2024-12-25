import logging.config
import os
import traceback
import yaml

def initialize_logger(logger_name: str) -> logging.Logger:
    """Utility function to initialize and return a logging object."""
    pwd = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    config_path = os.path.join(pwd, "preset/logging/config.yaml")
    
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found at: {config_path}")

    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
        logging.config.dictConfig(config)
    
    return logging.getLogger(logger_name)


def log_exceptions(logger: logging.Logger, exceptionObj: Exception):
    """Utility to add exceptions related logs."""
    err_trace = "\n".join(
        traceback.format_exception(
            exceptionObj, value=exceptionObj, tb=exceptionObj.__traceback__
        )
    )
    logger.error(f"The full traceback is:\n{err_trace}")
