# -*- coding: utf8 -*-

from api.common.base_errors import Base as BaseError


class NameCannotBeCreated(BaseError):
    status_code = 999
    message = 'Cannot create user with this name'


class NameAlreadyExists(BaseError):
    status_code = 998
    message = 'Name already exists.'
