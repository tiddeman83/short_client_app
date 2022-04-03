from flask import Blueprint
from flask_restx import Api, Resource

views = Blueprint('api', __name__)
view = Api(views)


@view.route('/')
class HomePage(Resource):
    def get(self):
        return {'hello': 'world'}
