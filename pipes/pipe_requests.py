#  Módulo Responsável por capturar body da página contendo os links
# Gerar ficheiros de armazenamento no sistema
# Mais informacões em doc/README.md e doc/DOC.info

# Imports
import asyncio, aiofiles

from hooks import mk_csv_file

from bs4 import BeautifulSoup



class PipeRequest:

    # Tarefas no Sistema

    async def _pipe(self, _cmd):
        """
            Executa sub processo de um shell comando, uma request para buscar o código html
         da página web contendo url de arquivos .xlsx
        :return:
            None
        """
        _task = await asyncio.create_subprocess_shell(_cmd)
        await _task.communicate()

    async def request_(self, cmd):
        await self._pipe(_cmd=cmd)


class PipeRecv:
    # Analisador do código html da página web requisitada

    async def _pipe(self, _aio_file):
        """

        :param _path_file:
            Caminho do árquivo html da página web contendo links para arquivos .xlsx
        :return:
            None
        """
        urls: list = []
        _soup = BeautifulSoup(_aio_file, 'html.parser')
        tag = _soup.select('a.internal-link')

        for line in tag:
            urls.append(line['href'])

        await mk_csv_file(_urls=urls)

    async def soup_(self, _path_file):
        async with aiofiles.open(_path_file) as htmlfilerr:
            await self._pipe(_aio_file=await htmlfilerr.read())
