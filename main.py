""" Módulo responsável por delegar cada tarefa em sua camda de execucão na aplicacão
 Analisando o argumento passado por linha de comando e delegando o queue para gerar o pipeline """

# Imports
import os, json
from app.apps import ApplicationProcessAssets, ApplicationParserAssets
from src.handlers import Handler

from dotenv import load_dotenv

load_dotenv()
CMD=os.getenv('COMMAND')


class QueueLine(Handler):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getattr__(self, attr):
        return super().__getattr__(attr)

    async def execute_(self, _prompt):

        if _prompt:
            self.app_process_ = ApplicationProcessAssets()
            post_urls_ = await self.pool_queue(_class=self.app_process_)
            await post_urls_._switch(_cmd=CMD)

            self.app_parser_ = ApplicationParserAssets()
            take_urls_ = await self.pool_queue(_class=self.app_parser_)
            await take_urls_._spider(_path='tmp/response_body.html')

    def __iter__(self):
        yield from {"_attrs": {attr: getattr(self, attr) for attr in self.__dict__.keys()}}.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__
