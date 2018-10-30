from api.common.base_resources import BaseResource

from .forms import ( CreateUserForm, UserListForm )

from .business_logics import user_bl

class UserResouce(BaseResource):
    POST_INPUT_SCHEMA = CreateUserForm()
    GET_INPUT_SCHEMA = UserListForm()
    
    def get(self):
        params = self.parse_request_params()
        return user_bl.get(**params)
    
    def post(self):
        params = self.parse_request_params()
        return user_bl.post(**params)
        
RESOURCES = {
    '/user': {
        'resource': UserResouce
    }
}
