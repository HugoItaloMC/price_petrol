# Módulo de execucão do programa

# Imports
from asyncio import new_event_loop, gather, create_task

from queueline import QueueLine


class Task:

    def __init__(self, op: str = ''):
        self._op = op

<<<<<<< HEAD
    def main(self):
        _line = QueueLine()
        task_by = self._make.create_task(_line.execute_(_prompt='frame_data_'))
        group = gather(task_by)
        self._make.run_until_complete(group)
=======
    async def _task_frame_data(self):
        line_frame_data = QueueLine()
        yield line_frame_data.execute_(_prompt='frame_data')

    async def _task_plotting(self):
        line_plotting = QueueLine()
        yield line_plotting.execute_(_prompt='plotting')

    async def run_async(self):
        tasks: list = []
        if self._op == 'frame_data':
            async for line in self._task_frame_data():
                task = create_task(line)
                tasks.append(task)

        elif self._op == 'plotting':
            async for line in self._task_plotting():
                task = create_task(line)
                tasks.append(task)
        await gather(*tasks)

    def runner(self):
        _make = new_event_loop()
        _make.run_until_complete(self.run_async())
>>>>>>> main

    def __call__(self, *args, **kwargs):
        return self.runner()


if __name__ == '__main__':
    _run_frame = Task('frame_data')
    _run_frame()

    _run_plotting = Task('plotting')
    _run_plotting()
