import logging
import os
from dotenv import load_dotenv

LOGLEVEL = os.environ.get("LOGLEVEL", "DEBUG")
DB_LOGLEVEL = os.environ.get("DB_LOGLEVEL", "INFO")

logging.basicConfig(level=LOGLEVEL, format="%(asctime)s %(levelname)8s %(message)s")
logger = logging.getLogger(__name__)

ENV_NAME = os.environ.get("ENV_NAME", "config")
ENV_FILE = f"{os.path.join(os.getcwd(), ENV_NAME)}.env"

if os.path.exists(ENV_FILE):
    logger.info("Loading env file from %s", ENV_FILE)
    load_dotenv(ENV_FILE)
else:
    logger.info("No %s.env file found. Relying on system env", ENV_NAME)


def create_secret_key():
    from django.core.management.utils import get_random_secret_key
    logger.info("Creating secret key...")
    return get_random_secret_key()

DB_HOST = os.environ.get("DB_HOST", "")
DB_PORT = os.environ.get("DB_PORT", 5432)
DB_NAME = os.environ.get("DB_NAME", "")
DB_UNAME = os.environ.get("DB_UNAME", "")
DB_PWORD = os.environ.get("DB_PWORD", "")
SECRET_KEY = create_secret_key()
DEBUG = os.environ.get("DEBUG", False)

