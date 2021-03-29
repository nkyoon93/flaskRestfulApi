from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)


class RegistUser(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=int)
        args = parser.parse_args()

        name = args['name']

        return {'name': name}

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('Hostname', type=str)
        args = parser.parse_args()

        Hostname = args['Hostname']
#NTP server hostname. Either an IP address or a hostname must be configured. Read-only once the resource is created.
        return {'Hostname' : Hostname}


api.add_resource(RegistUser, '/user')

if __name__ == '__main__':
    app.run(debug=True) #add url to method