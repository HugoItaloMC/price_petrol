from flask import request, jsonify

from src.api.core.controller import DescritorResource
from src.api.resourced import ResourceMain

class RestFrameData(ResourceMain):
    _method = DescritorResource()

    def post(self):
        self._method(content_type=request.headers.get('content-type'))
        return jsonify({"status": 200})


class RestPlotting(ResourceMain):
    _method = DescritorResource()

    def post(self):
        self._method(content_type=request.headers.get('content-type'))
        return jsonify({"status": 200})