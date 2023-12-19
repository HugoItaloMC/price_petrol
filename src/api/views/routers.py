from flask import Flask
from flask_restx import Api

from src.api.views.rest import RestFrameData, RestPlotting

app = Flask(__name__)

class Router:

    @staticmethod
    def args_routers():
        parser_router = Api(app)
        parser_router.add_resource(RestFrameData, '/frame_data', methods=['POST'])
        parser_router.add_resource(RestPlotting, '/plotting', methods=['POST'])


begin = Router()
begin.args_routers()
