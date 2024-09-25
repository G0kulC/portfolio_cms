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
PRODUCTION_SERVER = "https://portfolio-cms-jqgh.onrender.com"
SPECTACULAR_CONFIG = {
    "TITLE": "Portfolio CMS API",
    "DESCRIPTION": """
    Portfolio CMS API Documentation

    Welcome to the **Portfolio CMS API** documentation. This API allows you to manage user portfolios, including creating, updating, and deleting portfolio items.

    Key Features

    - **User Authentication**: Secure your API with JWT authentication.
    - **Portfolio Management**: CRUD operations for user portfolios.
    - **Learn Purpose Only**: This API is intended for educational purposes.

    """,
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "CONTACT": {
        "name": "Gokul C",
        "email": "gggokul865@gmail.com",
        "url": "https://gokuldev.netlify.app",
    },
    "LICENSE": {
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
    "TERMS_OF_SERVICE": "https://www.google.com/policies/terms/",
    "SERVERS": [
        {"url": PRODUCTION_SERVER, "description": "Production Server"},
        # {'url': 'http://localhost:8000', 'description': 'Local Development Server'},
    ],
    "SCHEMA_PATH_PREFIX": r"/api/",
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
        "defaultModelRendering": "model",
        "displayRequestDuration": True,
    },
    "SWAGGER_UI_DIST": "//unpkg.com/swagger-ui-dist@3.52.5",
    "SWAGGER_UI_FAVICON_HREF": "/static/images/favicon.ico",
    "REDOC_UI_SETTINGS": {
        "hideDownloadButton": True,
    },
    "PREPROCESSING_HOOKS": [],
    "POSTPROCESSING_HOOKS": [],
    "ENUM_NAME_OVERRIDES": {},
    "SORT_OPERATION_PARAMETERS": True,
    "COMPONENT_SPLIT_REQUEST": True,
    "SERVE_PERMISSIONS": ["rest_framework.permissions.AllowAny"],
    "SECURITY": [
        {"BearerAuth": ["Authorization"]},
    ],
    "SECURITY_SCHEMES": {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        },
    },
}
