import argparse
import os.path
import pathlib
import sys

from functionality import __version__
from functionality.directory_tree import DirectoryTree, TreeController


def parse_cmd_line_arguments():
    parser = argparse.ArgumentParser(
        prog="tree",
        description="'Directory Tree', a directory tree generator",
    )
    parser.version = f"version => {__version__}"
    parser.add_argument("-v", "--version", action="version")
    parser.add_argument(
        "-d",
        "--dir-only",
        action="store_true",
        help="ignore files and get only directories ",
    )
    parser.add_argument(
        "root_dir",
        metavar="ROOT_DIR",
        nargs="?",
        default=".",
        help="Generate a full directory tree starting at ROOT_DIR",
    )
    parser.add_argument(
        "-f",
        "--file",
        metavar="OUTPUT_FILE",
        nargs="?",
        default=sys.stdout,
        help="Store the generated tree to file in markdown format",
    )

    return parser.parse_args()


def main():
    args = parse_cmd_line_arguments()
    root_dir = pathlib.Path(args.root_dir)

    if not root_dir.is_dir():
        print("The specified root directory doesn't exist")
        sys.exit()

    tree_controller = TreeController(DirectoryTree(root_dir, args.dir_only))

    if args.file != sys.stdout:
        save_directory = input(f"Enter directory for saving the file: ").strip()
        name = "current-dir" if args.root_dir == "." else os.path.split(args.root_dir)[-1]
        file_name = f"{name}-tree.md" if not args.file else args.file
        if file_name.split(".")[-1] != "md":
            file_name += ".md"

        tree_controller.export_tree_to_markdown_file(save_directory, file_name)
        exit()

    print(tree_controller)


