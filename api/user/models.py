from api.common.base_models import db, BaseDocument

class User(BaseDocument):
    username = db.StringField(max_length=20, required=True, unique=True)
    password = db.StringField(required=True)
    email = db.StringField()
