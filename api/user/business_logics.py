from flask import jsonify

from .models import User
from .errors import *


class UserBL(object):
    def get(self):
        print (User.objects())
        return 'hihi'
    
    def post(self, username, password, email=None):
        if username == 'Longdt1':
            raise NameCannotBeCreated
        
        user = User.objects().filter(username=username)
        if user:
            raise NameAlreadyExists
            
        new_user = User(username=username, password=password).save()
        
        return jsonify(new_user)

user_bl = UserBL()
