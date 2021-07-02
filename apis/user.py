from flask import request
from flask_restplus import Namespace, Resource, fields

from core.user import create_user, get_all_user, get_one_user, delete_user, update_user

api = Namespace('users', description='CRUD for users')

user_create_input = api.model(
    'User', {
        'email': fields.String(required=True, description='The user email'),
        'password': fields.String(required=True, description='The user password'),
    }
)


@api.route('/')
class User(Resource):
    @api.expect(user_create_input)
    def post(self):
        data = request.get_json()
        create_user(data)
        return {"message": "User created"}

    def get(self):
        return get_all_user()


@api.route('/<int:id>')
class UserId(Resource):
    def get(self, id):
        user = get_one_user(get_all_user(), id)
        if not user:
            return {"message": "No user find!"}
        return user

    @api.expect(user_create_input)
    def put(self, id):
        data = request.get_json()
        if update_user(id, data):
            return {"message": "user was be update"}
        else:
            return {"message": "No user find!"}

    def delete(self, id):
        if delete_user(id):
            return {"message": "user deleted"}
        else:
            return {"message": "No user find!"}
