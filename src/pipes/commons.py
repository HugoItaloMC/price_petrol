from src.pipes.pipe_requests import PipeRequest, PipeRecv
from src.pipes.pipe_frame import PipeFrame
from src.pipes.pipe_plotting import PipePlotting

class DescritorPipes:
    _method = None

    def __set__(self, instance):
        if isinstance(instance, PipeRequest):
            self._method = lambda _cmd: instance.request_(cmd=_cmd)
        elif isinstance(instance, PipeRecv):
            self._method = lambda _path: instance.soup_(_path_file=_path)
        elif isinstance(instance, PipeFrame):
            self._method = lambda outpath: instance.pipeline_(outpath_=outpath)
        elif isinstance(instance, PipePlotting):
            self._method = lambda : instance.plot_data_view()
        return self._method

    def __get__(self, instance, owner):
        return self.__set__(instance)
