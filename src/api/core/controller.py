from abc import ABCMeta, abstractmethod

from run import Task


class APIMeta(metaclass=ABCMeta):

    def __init__(self):
        self.run_ = Task

    @abstractmethod
    def get_task(self, args):
        raise NotImplementedError('Method Not Implemented')

    @abstractmethod
    def sender_header(self, args):
        raise NotImplementedError('Method Not Implemented')


class DescritorResource:

    def __set__(self, instance):
        return lambda content_type: instance.api.sender_header(content_type=content_type)

    def __get__(self, instance, owner):
        return self.__set__(instance)