import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "this-is-not-my-production")
    DATABASE_PATH = os.path.join(BASE_DIR, "database.db")
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    PORT = 9900
    DATABASE_PATH = os.path.join(BASE_DIR, "dev_database.db")
    SECRET_KEY = os.environ.get("DEV_SECRET_KEY", "this-is-a-dev-secret")

class ProductionConfig(Config):
    DEBUG = False
    PORT = int(os.environ.get("PORT", 8000))
    DATABASE_PATH = os.path.join(BASE_DIR, "prod_database.db")
    SECRET_KEY = os.environ.get("PROD_SECRET_KEY", "this-is-a-prod-secret") 

config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}   
key = Config.SECRET_KEY

# Note: Remember to set appropriate environment variables for SECRET_KEY in production.
# Also, ensure that the PORT variable is set correctly in the production environment.
