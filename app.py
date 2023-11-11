# Execucão da aplicacão, gerando arquivo com base e retorna seu caminho


# Imports
import os
import csv

from src.run import Task


def asset() -> str:
    work_dir = os.path.join(os.environ['HOME'], os.getcwd())
    return work_dir


if __name__ == '__main__':
    print("%s" % asset())  # Test current dir