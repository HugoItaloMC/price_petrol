""" Módulo responsável por delegar cada tarefa em sua camda de execucão na aplicacão
 Analisando o argumento passado por linha de comando e delegando o queue para gerar o pipeline """

# Imports
import os, json
<<<<<<< HEAD:main.py
from apps import ApplicationPipeRequest, ApplicationPipeRecv, ApplicationPipeFrame
=======
>>>>>>> main:queueline.py
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
        self.post_urls_ = await self.pool_queue(_class=self._app_request)
        self.take_urls_ = await self.pool_queue(_class=self._app_recv)
        self.post_xlsx_ = await self.pool_queue(_class=self._app_frame)
        self.post_plotting = await self.pool_queue(_class=self._app_plotting)
        if _prompt:
<<<<<<< HEAD:main.py
            self.app_request_ = ApplicationPipeRequest()
            post_urls_ = await self.pool_queue(_class=self.app_request_)
            await post_urls_._switch(_cmd=CMD)

            self.app_recv_ = ApplicationPipeRecv()
            take_urls_ = await self.pool_queue(_class=self.app_recv_)
            await take_urls_._spider(_path='tmp/response_body.html')
=======
            await self.post_urls_._switch(_cmd=CMD)
            await self.take_urls_._spider(_path='tmp/response_body.html')

            if _prompt == 'frame_data_':
                await self.post_xlsx_._xlsx(outpath='tmp')

            if _prompt == 'plotting':
                 await self.post_plotting._plot()
>>>>>>> main:queueline.py

            if _prompt == 'frame_data_':
                self.app_frame = ApplicationPipeFrame('tmp/file_url.csv')
                post_xlsx_ = await self.pool_queue(_class=self.app_frame)
                await post_xlsx_._xlsx(outpath='tmp')


    def __iter__(self):
        yield from {"_attrs": {attr: getattr(self, attr) for attr in self.__dict__.keys()}}.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__
