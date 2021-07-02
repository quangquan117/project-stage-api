from extensions import db
from model import User


def create_user(data):
    new_user = User(
        email=(data['email']),
        password=(data['password'])
    )
    db.session.add(new_user)
    db.session.commit()


def get_all_user():
    users = User.query.all()
    output = []
    for user in users:
        user_data = {
            'id': user.id,
            'email': user.email,
            'password': user.password
        }
        output.append(user_data)
    return output


def get_one_user(all_user, id):
    user = User.query.filter_by(id=id).first()
    if not user:
        return False
    return all_user[id - 1]


def delete_user(id):
    user_to_delete = User.query.filter_by(id=id).first()
    if not user_to_delete:
        return False
    db.session.delete(user_to_delete)
    db.session.commit()
    return True


def update_user(id, data):
    user = get_one_user(get_all_user(), id)
    if not user:
        return False
    user = User.query.filter_by(id=id).first()
    user.email = data['email']
    user.password = data['password']
    db.session.commit()
    return True
