import aiofiles, csv
import pandas as pd


class PipeFrame:
    @staticmethod
    async def clean_data_frame_(_frame, _to_drop: bool = False):
        if _to_drop and _to_drop in _frame.columns:
            _frame_droped = _frame.dropna(axis=0).drop(columns=[_to_drop])
            return _frame_droped
        else:
            cleaned_frame_ = _frame.dropna(axis=0)
            return cleaned_frame_

    async def input_exel_(self, _url, to_drop_: bool = False):
        async for line in _url:
            excel_ = next(line)
            print(excel_)
            frame_ = await self.clean_data_frame_(_frame=pd.read_excel(excel_), _to_drop=to_drop_)
            yield frame_

    async def pipe_excel_(self, _cleaned_frame, _out_folder):
        async for line in _cleaned_frame:
            line.to_excel('%s/output.xlsx' % _out_folder, index=False)

    async def upload_urls_(self, _path):
        async with aiofiles.open(_path, "r+") as filerr:
            urls_ = csv.DictReader(await filerr.readlines())
            count: int = 0
            yield (line['URL'] for line in urls_ if count < 1 and (count := count + 1))

    async def pipeline_(self, inpath_, outpath_, to_drop: bool = False):
        url_ = self.upload_urls_(_path=inpath_)
        cleaned_frame_ = self.input_exel_(_url=url_, to_drop_=to_drop)
        await self.pipe_excel_(_cleaned_frame=cleaned_frame_, _out_folder=outpath_)
