class DescritorProcessAssets:

    def __set__(self, instance):
        return lambda _cmd: instance.begin_(cmd=_cmd)

    def __get__(self, instance, owner):
        return self.__set__(instance)


class DescritorParserAssets:

    def __set__(self, instance):
        return lambda _path: instance.soup_(_path_file=_path)

    def __get__(self, instance, owner):
        return self.__set__(instance)
