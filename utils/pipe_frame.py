import aiofiles, csv
import pandas as pd


class PipeFrame:
    @staticmethod
    async def clean_data_frame_(_frame, _to_drop=False):
        if _to_drop:
            if _to_drop in _frame.columns:
                _frame = _frame.drop(columns=[_to_drop])
                _clear_frame = _frame.dropna(axis=1)
                return _clear_frame
        _clear_frame = _frame.dropna(axis=1)
        return _clear_frame

    @staticmethod
    async def frame_to_excel_(_data, _outpath):
        idx = 0
        for frame in _data:
            idx += 1
            _outfiler = '%s/output_%s.xlsx' % (_outpath, idx)
            await frame.to_excel(_outfiler, index=False)


    async def upload_urls__(self, _path):
        async with aiofiles.open(_path, "r+") as filerr:
            urls_ = csv.DictReader(await filerr.readlines())
            for line in urls_:
                yield line['URL']

    async def pipeline_(self, inpath, outpath, to_drop: bool = False):
        _frame = self.upload_urls__(_path=inpath)
        cleaned_frame_ = [self.clean_data_frame_(_frame=url, _to_drop=to_drop) async for url in _frame]
        await self.frame_to_excel_(_data=cleaned_frame_, _outpath=outpath)
