# Módulo de execucão do programa

# Imports
from asyncio import Queue, get_event_loop, gather

from main import QueueLine


class Task:

    def __init__(self):
        self._make = get_event_loop()

    def main(self):
        _line = QueueLine()
        task_by = self._make.create_task(_line.execute_(_prompt='plot_data_'))
        group = gather(task_by)
        self._make.run_until_complete(group)
        print(next(map(str, _line)))

    def __call__(self, *args, **kwargs):
        return self.main()


if __name__ == '__main__':
    _run = Task()
    _run()
