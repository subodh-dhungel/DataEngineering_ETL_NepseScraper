import logging
import os
from config import get_env_variable

LOG_LEVEL = get_env_variable("LOG_LEVEL", "INFO")

logging.basicConfig(
    level = LOG_LEVEL,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    handlers={
        logging.FileHandler("scraper.log"),
        logging.StreamHandler() 
    }
)

logger = logging.getLogger(__name__)