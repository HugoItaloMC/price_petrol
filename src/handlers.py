import asyncio
from src.apps import ApplicationPipeRequest, ApplicationPipeRecv, ApplicationPipeFrame, ApplicationPipePlotting


class MetaHandler(type):

    def __new__(meta, *args, **kwargs):
        return type.__new__(meta, *args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '__instance'):
            cls.__instance = super(MetaHandler, cls).__call__(*args, **kwargs)
        return cls.__instance


class Handler(metaclass=MetaHandler):

    def __init__(self):
        self._queue = asyncio.Queue()

        self._app_request = ApplicationPipeRequest()
        self._app_recv = ApplicationPipeRecv()
        self._app_frame = ApplicationPipeFrame('tmp/file_url.csv')
        self._app_plotting = ApplicationPipePlotting('tmp/output.xlsx')

    def __getattr__(self, attr):
        valur = attr
        setattr(self, attr, valur)
        return valur

    async def pool_queue(self, _class):
        await self._queue.put(_class)
        return await self._queue.get()
