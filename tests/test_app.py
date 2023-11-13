# Imports
from test_run import Task


def asset() -> ...:
    print('Chamando funcão asset() do módulo test_app.py')
    Task()


if __name__ == '__main__':
    import io
    import pstats
    from pstats import SortKey
    from cProfile import Profile

    with Profile() as profile:
        Task()
        _str = io.StringIO()
        _stats = pstats.Stats(profile, stream=_str).sort_stats(SortKey.TIME)
        _stats.print_stats()
        print(_str.getvalue())
