from utils.pipe_requests import PipeRequest, PipeRecv
from utils.pipe_frame import PipeFrame
from src.commons import DescritorPipeRequest, DescritorPipeRecv, DescritorPipeFrame


class ApplicationPipeRequest(PipeRequest):
    _switch = DescritorPipeRequest()


class ApplicationPipeRecv(PipeRecv):
    _spider = DescritorPipeRecv()


class ApplicationPipeFrame(PipeFrame):
    _xlsx = DescritorPipeFrame()
