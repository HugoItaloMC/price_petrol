import pstats


async def pool_queue(queue, _class):
    await queue.put(_class)


async def mk_csv_file(path):
    print("Atributo Recebido %s " % path)
    print("Chamando corotina mk_csv_file do módulo helper.py")

if __name__ == '__main__':
    import io
    from asyncio import run, Queue
    from cProfile import Profile
    from pstats import SortKey


    class Test_poll_queue:
        ...

    with Profile() as profile:
        run(mk_csv_file('TESTE____'))
        run(pool_queue(Queue(), Test_poll_queue()))
        _str = io.StringIO()
        _stats = pstats.Stats(profile, stream=_str).sort_stats(SortKey.TIME)
        _stats.print_stats()
        print(_str.getvalue())

