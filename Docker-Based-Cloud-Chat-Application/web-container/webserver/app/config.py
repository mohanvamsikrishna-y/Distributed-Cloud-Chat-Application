import os

SECRET_KEY = 'xZxM5GMQ37CQw9kf6SRS33LadZTpSKt6'
MONGO_HOST = os.environ.get('MONGO_HOST', 'db-service')
MONGODB_SETTINGS = {'db': 'mongodb', 'host': MONGO_HOST, 'port': 27017}

