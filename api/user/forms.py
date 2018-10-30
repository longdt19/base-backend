from api.common.base_forms import BaseForm, BaseCreateForm, fields

class CreateUserForm(BaseForm):
    username = fields.String(required=True)
    password = fields.String(required=True)
    email = fields.String()
    
class UserListForm(BaseForm):
    pass
