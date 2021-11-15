import pathlib
from tkinter import filedialog
from datetime import datetime
from functionality.directory_tree import DirectoryTree, TreeController


def now():
    date_time = datetime.now()
    return date_time.strftime(f"%d-%m-%Y-%H:%M:%S")


def reset_output_file_name(variable):
    variable.set(f"{now()}-tree.md")


def set_dir_path(variable):
    path = filedialog.askdirectory()
    if not path:
        variable.set(".")
        return

    variable.set(path)


def create_tree(root_dir_path: str, dir_only: bool) -> TreeController:
    root_dir_path = pathlib.Path(root_dir_path)
    if not root_dir_path.is_dir():
        raise NotADirectoryError(f"Directory {root_dir_path} does not exist!")

    return TreeController(DirectoryTree(root_dir_path, dir_only).generate())


def export(tree, render) -> None:
    try:
        file = filedialog.asksaveasfile(mode="w", defaultextension=".md")
    except PermissionError:
        message = f"You have no permission to save '' in ''"
        render(message)
        return

    if not file:
        return

    filename = file.name.split('/')[-1]
    directory = '/'.join(file.name.split('/')[:-1])

    tree.export_tree_to_markdown_file(file)
    message = f"File '{filename}' exported successfully in\n'{directory}'"
    render(message)
