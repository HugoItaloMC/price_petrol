from flask import request, jsonify

from src.api.core.controller import APIMeta


class API(APIMeta):

    def __init__(self):
        super().__init__()

    def get_task(self, body):
        if body.get('frameData'):
            _frame = self.run_(op=body.get('frameData'))
            _frame.runner()
        elif body.get('plottingData'):
            _plotting = self.run_(op=body.get('plottingData'))
            _plotting.runner()

    def sender_header(self, content_type):
        xstr = lambda ss: ss or ''
        content_json = 'json' in xstr(content_type)

        while op := request.method:
            if op == 'POST':
                label = request.get_json(force=True) or request.get_json() or request.form.to_dict()
                fields = request.json if content_json else label
                return self.get_task(body=fields)
