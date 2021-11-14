import pathlib
from easygui import diropenbox
from datetime import datetime
from functionality.directory_tree import DirectoryTree, TreeController


def create_tree(root_dir_path: str, dir_only: bool):
    root_dir_path = pathlib.Path(root_dir_path)
    if not root_dir_path.is_dir():
        raise NotADirectoryError(f"Directory {root_dir_path} does not exist!")

    return TreeController(DirectoryTree(root_dir_path, dir_only))


def open_window():
    path = diropenbox(msg=f"Choose directory")
    if path is None:
        return "."
    return path


def now():
    date_time = datetime.now()
    return date_time.strftime(f"%d-%m-%Y-%H:%M:%S")
