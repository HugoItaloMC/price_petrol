import pstats

from test_pipe import WorkFlow
from test_helper import pool_queue


class QueueLine:

    def __init__(self, queue):
        self._queue = queue

    async def executor(self):
        await pool_queue(self._queue, _class=WorkFlow())

        work = await self._queue.get()

        if work:
            process = work.pipe('process')
            await process.get_()

            parser = work.pipe('parser')
            await parser.get_()


if __name__ == '__main__':
    import asyncio
    import cProfile
    import io
    from pstats import SortKey

    profile = cProfile.Profile()
    profile.enable()

    queue = QueueLine(asyncio.Queue())
    asyncio.run(queue.executor())

    profile.disable()

    _str = io.StringIO()
    _stats = pstats.Stats(profile, stream=_str).sort_stats(SortKey.TIME)  # Verificando tempo de chamadas
    _stats.print_stats()
    print(_str.getvalue())
