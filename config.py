import os

class Config:    
    PROPAGATE_EXCEPTIONS = True
    FLASK_DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///expense_tracker.db'
    ##SQLALCHEMY_DATABASE_URI = f"postgresql://{os.environ.get('POSTGRES_USER', 'user')}:" \
    ##                          f"{os.environ.get('POSTGRES_PASSWORD', 'mysecurepassword')}@" \
    ##                          f"{os.environ.get('DB_HOST', 'localhost')}/" \
    ##                          f"{os.environ.get('POSTGRES_DB', 'finance_app')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_TITLE = "Finance REST API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
