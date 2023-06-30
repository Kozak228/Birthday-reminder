from os.path import isfile, abspath, exists, join
from os import environ, mkdir
from pathlib import Path


def proverka_file(file_name, path_file):
    full_path_file = f"{path_file}{file_name}.json"

    return True if isfile(full_path_file) else False


def proverka_dir(path_dir):
    if path_dir != "":
        if path_dir[-1] != "\\":
            path_dir += "\\"
    else:
        path_dir = abspath("Birthday reminder.exe")
        path_dir = path_dir[:path_dir.rindex("\\") + 1]

    return path_dir


def path_for_autorun():
    full_path_file = abspath("Birthday reminder.exe")
    name_app = Path(full_path_file).stem

    return full_path_file, name_app


def proverka_path_in_config(name_dir, proverka_dir=False):
    path_file = join(join(environ['USERPROFILE']), 'Documents')

    path_file += "\\"

    path_file += name_dir

    if proverka_dir:
        return True if exists(path_file) else False

    else:
        if exists(path_file):
            path_file += "\\"
            return path_file
        else:
            mkdir(path_file)
            path_file += "\\"
            return path_file


def proverka_path_in_icons_dir():
    path_dir = abspath("Icons for app Birthday reminder")

    path_dir += "\\"

    return path_dir