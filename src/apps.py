from src.pipes.pipe_requests import PipeRequest, PipeRecv
from src.pipes.pipe_frame import PipeFrame
from src.pipes.pipe_plotting import PipePlotting
from src.pipes.commons import DescritorPipes


class ApplicationPipeRequest(PipeRequest):
    _switch = DescritorPipes()


class ApplicationPipeRecv(PipeRecv):
    _spider = DescritorPipes()


class ApplicationPipeFrame(PipeFrame):
    _xlsx = DescritorPipes()


class ApplicationPipePlotting(PipePlotting):
    _plot = DescritorPipes()
