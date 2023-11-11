# Execucão da aplicacão, gerando arquivo com base e retorna seu caminho


# Imports
import os
import csv

from src.run import Task


def asset() -> str:
    tas = Task()

    work_dir = os.path.join(os.environ['HOME'], os.getcwd())  # Current Dir
    src_dir = os.path.join(work_dir, 'src')  # Path to src/

    if not os.getcwd() == src_dir:  # Move to src/ dir
        os.chdir(src_dir)

    return os.getcwd()


if __name__ == '__main__':
    print("%s" % asset())  # Test move to src/ dir
    # Test path src/ >> OK
    # Test current dir >> OK
