# Execucão da aplicacão, gerando arquivo com base e retorna seu caminho


# Imports
import os
import csv

from src.run import Task


def asset() -> ...:
    task = Task()

    work_dir = os.path.join(os.environ['HOME'], os.getcwd())  # Current Dir
    src_dir = os.path.join(work_dir, 'src')  # Path to src/

    if not os.getcwd() == src_dir:  # Move to src/ dir
        os.chdir(src_dir)
    task()


if __name__ == '__main__':
    asset()
    # Testing coroutine calls with queues and pipes in execute line >> OK
    # Test from class Task() need running coroutine >> OK
    # Test move to src/ dir >> OK
    # Test path src/ >> OK
    # Test current dir >> OK
