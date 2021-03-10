#! /bin/env python
import os
from pathlib import Path

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)   # TODO: 2-3
TARGET = Path.cwd()


def inject_output_dir_path(path: Path) -> None:
    for node in path.iterdir():
        if node.is_dir():
            inject_output_dir_path(node)
        elif node.is_file():
            try:
                content = node.read_text()
            except UnicodeDecodeError:
                # Skip binary files
                return
            content = content.replace("$((INSTALL))", str(TARGET))
            node.write_text(content)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    inject_output_dir_path(TARGET)
