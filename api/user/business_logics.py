class UserBL(object):
    def get(self):
        return 'hihi'
    
    def post(self, username, password, email=None):
        print ('username', username)

user_bl = UserBL()
