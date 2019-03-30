from djangoDemo.db.user_models.models import User


def get_user_json(user_object):
    return {
        'userName': user_object.userid,
        'firstName': user_object.fname,
        'middleName': user_object.mname,
        'lastName': user_object.lname,
        'createdOn': user_object.created_on.strftime('%d/%m/%Y'),
        'phone': user_object.phone
    }


def get_user_by_username(username):
    try:
        user_object = User.objects.get(userid=username)
        return user_object
    except:
        raise Exception()


def get_users_by_filter(criteria={}):
    return User.objects.filter(**criteria)


def create_user(body_param):
    try:
        user_object = User.objects.create(userid=body_param['username'],
                                          fname=body_param['firstName'],
                                          lname=body_param['lastName'],
                                          password=body_param['password'])
        return user_object
    except Exception as e:
        print e
        raise Exception()
