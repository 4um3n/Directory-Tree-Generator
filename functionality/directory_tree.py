"""functionality main module"""

import os

PIPE = "│"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "


class _TreeGenerator:
    def __init__(self, root_dir, dir_only) -> None:
        self._root_dir = root_dir
        self._dir_only = dir_only
        self._tree = []

    def build_tree(self) -> list:
        self._build_tree_head()
        self._build_tree_body(self._root_dir)
        return self._tree

    def _build_tree_head(self):
        self._tree.append(f"{self._root_dir}{os.sep}")
        self._tree.append(PIPE)

    def _build_tree_body(self, directory, prefix="") -> None:
        entries = self._get_entries(directory)
        entries_count = len(entries)
        for index, entry in enumerate(entries):
            connector = ELBOW if index == entries_count - 1 else TEE
            if entry.is_dir():
                self._add_directory(entry, index, entries_count, prefix, connector)
            else:
                self._add_file(entry, prefix, connector)

    def _get_entries(self, directory):
        if self._dir_only:
            return list(entry for entry in sorted(directory.iterdir(), key=lambda ent: ent.name) if entry.is_dir())
        return list(sorted(directory.iterdir(), key=lambda ent: (ent.is_file(), ent.name)))

    def _add_directory(self, directory, index, entries_count, prefix, connector):
        self._tree.append(f"{prefix}{connector} {directory.name}{os.sep}")
        if index != entries_count - 1:
            prefix += PIPE_PREFIX
        else:
            prefix += SPACE_PREFIX
        self._build_tree_body(directory, prefix=prefix, )
        self._tree.append(prefix.rstrip())

    def _add_file(self, file, prefix, connector):
        self._tree.append(f"{prefix}{connector} {file.name}")


class DirectoryTree:
    def __init__(self, root_dir, dir_only=False) -> None:
        self._generator = _TreeGenerator(root_dir, dir_only)

    def generate(self) -> str:
        tree = self._generator.build_tree()
        return '\n'.join(tree)


class TreeController:
    def __init__(self, tree: str):
        self.tree = tree

    def export_tree_to_markdown_file(self, file):
        tree_data = '\n'.join(["```", self.tree, "```"])
        file.write(tree_data + '\n')
        file.close()

    def __str__(self):
        return self.tree
