from app.pipe import ProcessAssets, ParserAssets

from src.commons import DescritorProcessAssets, DescritorParserAssets


class ApplicationProcessAssets(ProcessAssets):
    _switch = DescritorProcessAssets()


class ApplicationParserAssets(ParserAssets):
    _spider = DescritorParserAssets()
