# Módulo de execucão do programa

# Imports
from asyncio import Queue, get_event_loop, gather

from src.queue import QueueLine


class Task:

    def __init__(self):
        self._queue = Queue()
        self._make = get_event_loop()

    def main(self):
        _line = QueueLine()
        task_by = self._make.create_task(_line.executor())
        group = gather(task_by)
        self._make.run_until_complete(group)

    def __call__(self, *args, **kwargs):
        return self.main()
