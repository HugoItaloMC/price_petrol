

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
        return lambda inpath_, outpath_, to_drop_: instance.pipeline_(inpath=inpath_, outpath=outpath_, to_drop=to_drop_)

    def __get__(self, instance, owner):
        return self.__set__(instance)
