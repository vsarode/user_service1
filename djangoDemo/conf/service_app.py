from flask import Flask
from flask_restful import Api
import django; django.setup()
from djangoDemo.service_apis.login import Login
from djangoDemo.service_apis.user import User

app = Flask(__name__)
api = Api(app, prefix='/userservice/')

api.add_resource(User, 'user', 'user/<username>')
api.add_resource(Login, 'login', 'login/<token>')

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
