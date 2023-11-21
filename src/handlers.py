import asyncio


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

    def __getattr__(self, attr):
        valur = attr
        setattr(self, attr, valur)
        return valur

    async def pool_queue(self, _class):
        await self._queue.put(_class)
        return await self._queue.get()
