#  Módulo Responsável por capturar body da página contendo os links
# Gerar ficheiros de armazenamento no sistema
# Mais informacões em README.md

# Imports
import csv, subprocess, os, shlex, asyncio
from dotenv import load_dotenv

from bs4 import BeautifulSoup

from src.helper import mk_csv_file


class ProcessAssets:

    # Tarefas no Sistema

    @staticmethod
    async def mk_folder(path):
        """

        :param path:
            Caminho para criar nova pasta se a mesma ñ existir
        :return:
            None
        """

        print('Chamando corotina mk_folder da classe ProcessAssets\nAtributo recebido %s' % path)

    @staticmethod
    async def _environ():
        """
          Criar ficheiros e arquivos no sistema, buscar informacões em variáveis de ambiente
        necessárias para execucão de processos
        :return:
            String
        """
        await ProcessAssets.mk_folder('TESTE _mk_folder')
        print('Chamando corotina _environ da classe ProcessAssets')

    async def _process(self):
        """
            Executa sub processo de um shell comando, uma request para buscar o código html
         da página web contendo url de arquivos .xlsx
        :return:
            None
        """
        await self._environ()
        print("Chamando corotina _process da classe ProcessAssets")

    async def get_(self):
        await self._process()
        print("Chamando corotina get_ da classe ProcessAssets")


class ParserAssets:
    # Analisador do código html da página web requisitada

    async def _parser_html(self, _path_file):
        """

        :param _path_file:
            Caminho do árquivo html da página web contendo links para arquivos .xlsx
        :return:
            None
        """
        await mk_csv_file('TESTE _mk_csv_file')
        print("Atributo recebido %s " % _path_file)
        print("Chamando corotina _parser_html da classe ParserAssets")

    async def get_(self):
        print("Chamando corotina get_ da classe ParserAssets")
        await self._parser_html("TESTE _parser_html")


class WorkFlow:

    def _process_assets(self):
        return ProcessAssets()

    def _parser_assets(self):
        return ParserAssets()

    def pipe(self, prompt):

        if prompt.lower() == 'process':
            return self._process_assets()

        elif prompt.lower() == 'parser':
            return self._parser_assets()
