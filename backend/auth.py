from flask import Blueprint, request, jsonify
from flask_restx import Resource, Api, fields, marshal
from .models import firstUsers
from .models import Users
import json

authenticate = Blueprint('auth', __name__)
auth = Api(authenticate)


# models relating to the forms used
eerstekeer_model = auth.model('firstUsers', {
    "username": fields.String(),
    "password": fields.String(),
    "unique_token": fields.String(),
    "token_used": fields.Boolean()
})

registratie_model = auth.model('registratie', {
    "username": fields.String(),
    "password": fields.String(),
    "email": fields.String(),
    "first_name": fields.String(),
    "middle_name": fields.String(),
    "last_name": fields.String(),
})


@auth.route('/eerstekeer')
class EersteKeer(Resource):
    def get(self):
        """Get all first time user, this method is to be removed"""
        pass

    @auth.marshal_with(eerstekeer_model)
    @auth.expect(eerstekeer_model)
    def post(self):
        data = request.get_json()
        gebruiker = data['username']
        print(gebruiker)
        ftu = firstUsers.query.filter_by(
            username=data['username']).first()

        print(ftu.username)
        if ftu is None:
            return {"username": "gebruikersnaam bestaat niet"}, 402

        # hier nog een methode toevoegen die zorgt dat de database op gebruikt komt te staan als de registratie is uitgevoerd
        # dat zou op zich ook nog in de registratiemethod zelf gedaan kunnen worden.

        data_json = marshal(ftu, eerstekeer_model)
        print(data_json)
        return data_json, 201

    def put(self):
        pass


@auth.route('/registratie')
class Registratie(Resource):
    @auth.marshal_with(registratie_model)
    @auth.expect(registratie_model)
    def post(self):
        data = request.get_json()

        username = data['username']
        password = data['password']
        email = data['email']
        first_name = data['first_name']
        middle_name = data['middle_name']
        last_name = data['last_name']

        user = Users.query.filter_by(username=username).first()

        if user is None:
            user = Users(username=username, password=password, email=email,
                         first_name=first_name, middle_name=middle_name, last_name=last_name)
            user.save()
            return marshal(user, registratie_model), 201

        return {"username": "gebruikersnaam bestaat al"}, 402
