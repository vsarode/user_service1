from djangoDemo.db.user_models.models import Login
from djangoDemo.service_api_handler import user_handler


def get_login_objects_by_filter(criteria={}):
    return Login.objects.filter(**criteria)


def create_login(user_object):
    login_object, _ = \
        Login.objects.get_or_create(user=user_object, is_logged_in=True)
    return login_object


def get_login_json(login_object):
    return {
        'token': login_object.token,
        'isLoggedIn': login_object.is_logged_in,
        'createdOn': login_object.created_on.strftime('%d/%m/%Y'),
        'loggerOutTime': login_object.loggedout_time.strftime('%d/%m/%Y') if login_object.loggedout_time else "",
        'user': user_handler.get_user_json(login_object.user)
    }


def get_login_object_by_token(token):
    try:
        login_object = Login.objects.get(token=token)
        return login_object
    except:
        raise Exception()
