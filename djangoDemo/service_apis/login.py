from flask import request, jsonify
from flask_restful import Resource

from djangoDemo.service_api_handler import user_handler, login_handler


class Login(Resource):
    def post(self):
        body_param = request.get_json()
        user_object = user_handler.get_user_by_username(body_param['username'])
        if user_object.password == body_param['password']:
            login_object = login_handler.create_login(user_object)
            return jsonify(
                {"login": login_handler.get_login_json(login_object)})

    def get(self, token=None):
        if token:
            login_object = login_handler.get_login_object_by_token(token)
            return jsonify(
                {"login": login_handler.get_login_json(login_object)})
        criteria = request.args
        req_filter = {}
        if 'username' in criteria:
            req_filter['user_id'] = criteria['username']
        if 'firstName' in criteria:
            req_filter['user__fname'] = criteria['firstName']

        login_objects = login_handler.get_login_objects_by_filter(req_filter)
        return jsonify({"logins": [login_handler.get_login_json(login) for login
                                   in login_objects]})
