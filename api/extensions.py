from flask_mongoengine import MongoEngine
from flask_restful import Api
from flask_cors import CORS


cors = CORS(supports_credentials=True)
db = MongoEngine()
api = Api()
