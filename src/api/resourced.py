from flask_restx import Resource

from src.api.core.api import API


class ResourceMain(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.api = API()