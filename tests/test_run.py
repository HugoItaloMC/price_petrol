# Imports
import pstats
from asyncio import Queue, get_event_loop, gather

from test_queue import QueueLine


class Task:

    def __init__(self):
        self._make = get_event_loop()

    def main(self):
        _line = QueueLine(Queue())
        task_by = self._make.create_task(_line.executor())
        group = gather(task_by)
        self._make.run_until_complete(group)

    def __call__(self, *args, **kwargs):
        return self.main()


if __name__ == '__main__':
    import io
    import cProfile
    from pstats import SortKey

    with cProfile.Profile() as profile:
        task_ = Task()
        task_()
        _str = io.StringIO()
        _stats = pstats.Stats(profile, stream=_str).sort_stats(SortKey.TIME)

        _stats.print_stats()
        print(_str.getvalue())
