import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

SECRET_KEY = os.getenv("SECRET_KEY", 'default_key')

DEBUG = True

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(',')
print(ALLOWED_HOSTS)
