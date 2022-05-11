from os import environ
from dotenv import load_dotenv

# Загрузка значений переменных окружения
load_dotenv()

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
SESSION_STRING = environ.get('SESSION_STRING')
SOURCE_CHANNEL = environ.get('SOURCE_CHANNEL')
TARGET_CHANNEL = environ.get('TARGET_CHANNEL')
