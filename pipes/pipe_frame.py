import aiofiles, csv
import pandas as pd


class PipeFrame:

    def __init__(self, inpath: str):
        self._inpath = inpath

    @staticmethod
    async def handler_data_frame_(_frame):
        join_col_ = _frame.iloc[:, [2, 3, 7, 9, 10]]  # Indices de colunas
        _frame_load = join_col_.dropna(axis=0)  # Excluindo linhas nulas
        return _frame_load

    async def input_exel_(self, _url):
        async for line in _url:
            excel_ = next(line)
            print(excel_)
            frame_ = await self.handler_data_frame_(_frame=pd.read_excel(excel_))
            yield frame_

    async def pipe_excel_(self, _parser_frame, _out_folder):
        async for line in _parser_frame:
            line.to_excel('%s/output.xlsx' % _out_folder, index=False)

    async def upload_urls_(self, _path):
        async with aiofiles.open(_path, "r+") as filerr:
            urls_ = csv.DictReader(await filerr.readlines())
            count: int = 0
            yield (line['URL'] for line in urls_ if count < 1 and (count := count + 1))

    async def pipeline_(self, outpath_):
        url_ = self.upload_urls_(_path=self._inpath)
        parser_frame_ = self.input_exel_(_url=url_)
        await self.pipe_excel_(_parser_frame=parser_frame_, _out_folder=outpath_)
