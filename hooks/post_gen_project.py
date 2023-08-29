import os
import shutil


def remove(filepath: str) -> None:
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


if not {{cookiecutter.generate_docs}}:
    remove(os.path.join(os.getcwd(), 'docs'))
