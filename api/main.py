import jwt
from flask import Flask, request, abort, g, make_response, jsonify
from itsdangerous import URLSafeTimedSerializer

from config import Config

from api.extensions import api, db, cors

from .endpoints import ENDPOINTS
from .flask_session import ItsdangerousSessionInterface

__all__ = ['create_app']

def create_app(app_name=None):
    if not app_name:
        app_name = Config.APP_NAME

    app = Flask(app_name)

    # app.config.from_object(Config)
    # app.config['COOKIE_SERIALIZER'] = URLSafeTimedSerializer(Config.CAS_KEY,
    #                                                          signer_kwargs={'key_derivation': 'hmac'})
    # 
    # app.session_interface = ItsdangerousSessionInterface()
    configure_hook(app)
    configure_extensions(app)
    configure_logging(app)
    configure_error_handlers(app)
    return app


def configure_extensions(app):
    # flask_restful api
    api.app = app
    for endpoint, data in ENDPOINTS.items():
        api.add_resource(data['resource'], endpoint)

    # database
    db.init_app(app)

    # cors
    cors.init_app(app)


def configure_logging(app):
    # app.logger.addHandler(file_handler)
    # app.logger.debug()
    pass


def configure_hook(app):
    """configure_hook regist hook in app like before_request, after_request
        :param app:
    """

    @app.before_request
    def before_request():
        """ ham nay chay truoc khi xu ly request """
        # serializer = app.config['COOKIE_SERIALIZER']
        # g.cookie_serializer = serializer
        # 
        # auth_data = request.headers.get('Authorization', None)
        # g.user = get_auth_user(auth_data=auth_data)
        # 
        # if is_required_auth(endpoint=request.path, method=request.method):
        #     try:
        #         user_info = serializer.loads(request.cookies['session'])
        #         email = user_info['email']
        #     except Exception as error:
        #         return abort(401)
        # 
        #     if not g.user:
        #         return abort(401)
        print ('before_request')
    
    # @app.after_request
    # def after_request():
    #     """ ham nay chay sau khi xu ly request"""
    #     print ('after_request')

def configure_error_handlers(app):
    @app.errorhandler(Exception)
    def handle_error(error):
        print ('error', app.debug)
        if hasattr(error, 'status_code'):
            response = make_response(str(error), error.status_code)

        elif hasattr(error, 'code'):
            response = make_response(str(error), error.code)

        else:
            if app.debug:
                raise error
            response = make_response(
                jsonify({'message': 'An unknown error happened - %s' % error}), 500)

        return response


def is_required_auth(endpoint, method):
    # don't require token for options method
    if method == 'OPTIONS':
        return False

    # if request endpoint is invalid
    if endpoint not in ENDPOINTS.keys():
        return False

    # if request endpoint is valid, then get its required auth methods
    required_auth_methods = ENDPOINTS[endpoint].get('required_auth_methods')

    if not required_auth_methods:
        return False

    if method in required_auth_methods:
        return True

    return False


def get_auth_user(auth_data=None):
    if not auth_data:
        return None

    try:
        bearer, access_token = auth_data.split(' ')
    except ValueError:
        return None

    if bearer != 'Bearer' or not access_token:
        return None
    try:
        token_data = jwt.decode(access_token, Config.SECRET_KEY, options={'verify_exp': False})

    except Exception as error:
        print('Check token error', error.args)
        return None

    return User.objects(id=token_data.get('id')).first()
