#!/usr/bin/env python3
# tree_gui.py

"""This module provides Directory Tree Generator entry point GUI script."""


from GUI.canvas import setup
from GUI.views import DirectoryTreeView

if __name__ == '__main__':
    root = setup()
    tree_view = DirectoryTreeView(root)
    tree_view.render()
    root.mainloop()
