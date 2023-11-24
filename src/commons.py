

class DescritorPipeRequest:

    def __set__(self, instance):
        return lambda _cmd: instance.request_(cmd=_cmd)

    def __get__(self, instance, owner):
        return self.__set__(instance)


class DescritorPipeRecv:

    def __set__(self, instance):
        return lambda _path: instance.soup_(_path_file=_path)

    def __get__(self, instance, owner):
        return self.__set__(instance)


class DescritorPipeFrame:

    def __set__(self, instance):
        return lambda inpath_, outpath, _to_drop: instance.pipeline_(inpath_=inpath_, to_drop=_to_drop, outpath_=outpath)

    def __get__(self, instance, owner):
        return self.__set__(instance)
