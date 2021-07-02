from flask_restplus import Api

from .hello import api as ns_hello
from .user import api as ns_create_user

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'x-access-token'
    }
}

api = Api(
    title='Project Api',
    version='0.8',
    description='Api for learn how it\'s works',
    authorizations=authorizations
)

api.add_namespace(ns_hello)
api.add_namespace(ns_create_user)
