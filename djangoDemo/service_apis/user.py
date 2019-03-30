from flask import request, jsonify
from flask_restful import Resource

from djangoDemo.service_api_handler import user_handler


class User(Resource):
    def get(self, username=None):
        if username:
            user_object = user_handler.get_user_by_username(username)
            return jsonify({'user': user_handler.get_user_json(user_object)})
        else:
            user_objects = user_handler.get_users_by_filter()

            return jsonify({"users": [user_handler.get_user_json(user) for user
                                      in user_objects]})

    def post(self):
        body_param = request.get_json()

        user_object = user_handler.create_user(body_param)
        response = user_handler.get_user_json(user_object)

        return jsonify({"user": response})
