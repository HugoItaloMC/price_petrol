""" Módulo responsável por delegar cada tarefa em sua camda de execucão na aplicacão
 Analisando o argumento passado por linha de comando e delegando o queue para gerar o pipeline """

# Imports
import os, json
from apps import ApplicationPipeRequest, ApplicationPipeRecv, ApplicationPipeFrame
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
            self.app_request_ = ApplicationPipeRequest()
            post_urls_ = await self.pool_queue(_class=self.app_request_)
            await post_urls_._switch(_cmd=CMD)

            self.app_recv_ = ApplicationPipeRecv()
            take_urls_ = await self.pool_queue(_class=self.app_recv_)
            await take_urls_._spider(_path='tmp/response_body.html')

            if _prompt == 'frame_data_':
                self.app_frame = ApplicationPipeFrame()
                post_xlsx_ = await self.pool_queue(_class=self.app_frame)
                await post_xlsx_._xlsx(inpath_='tmp/file_url.csv', outpath_='tmp', to_drop_=False)


    def __iter__(self):
        yield from {"_attrs": {attr: getattr(self, attr) for attr in self.__dict__.keys()}}.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__
