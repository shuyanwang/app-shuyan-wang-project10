def user_has_permission(jwt_identity, the_user):
    return jwt_identity['email'] == str(the_user.email) or jwt_identity['role'] == 'admin'


def user_is_admin(jwt_identity):
    return jwt_identity['role'] == 'admin'
