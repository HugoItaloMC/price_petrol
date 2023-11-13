""" Módulo responsável por delegar cada tarefa em sua camda de execucão na aplicacão
 Analisando o argumento passado por linha de comando e delegando o queue para gerar o pipeline """

# Imports

from src.pipe import WorkFlow
from src.helper import pool_queue


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



