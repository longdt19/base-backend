import uuid
from flask import jsonify, g

from .models import Account
from .errors import *


class AccountBL(object):
    def get(self):
        print('vao day')
        account = g.session.query(Account).all()
        print('hihi', account)
        return 'hihi'
    
    def post(self, username, password, email=None):
        id = uuid.uuid4()
        ed_user = Account(id=id, username=username, password=password, email=email)
        g.session.add(ed_user)
        g.session.commit()
        print('123', g.session.query(Account).all())
        return '123'

user_bl = AccountBL()
