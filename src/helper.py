

async def pool_queue(queue, _class):
    await queue.put(_class)


async def mk_csv_file(path):
    print("Atributo Recebido %s " % path)
    print("Chamando corotina mk_csv_file do módulo helper.py")