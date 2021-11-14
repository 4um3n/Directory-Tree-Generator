from tkinter import *
from GUI.helpers import create_tree, open_window, now


class View:
    """Base class for all view classes"""

    def __init__(self, root: Tk) -> None:
        self._root = root

    @staticmethod
    def clear_view(root) -> None:
        for slave in root.grid_slaves():
            slave.destroy()


class DirectoryTreeView(View):
    __ABG = "gray"
    __AFG = "black"
    __BG = "gray14"
    __HBG = "gray10"
    __FG = "snow2"
    __MESSAGE_FG = "IndianRed2"

    def __init__(self, root: Tk) -> None:
        super().__init__(root)
        self._top = None
        self._tree = None
        self._root_dir_path = "."
        self._output_dir_path = "."
        self._dir_only = BooleanVar()
        self._output_file_name = StringVar()
        self._reset_output_file_name()

    def render(self, message: str = "") -> None:
        """Render tree view window"""

        """Scrollbar widgets"""
        # create a vertical Scrollbar - no need to write orient as it is by default vertical
        _vertical_scrollbar = Scrollbar(
            self._root,
            bd=0,
            bg=self.__ABG,
            elementborderwidth=0,
            highlightthickness=0,
            troughcolor=self.__BG,
            highlightcolor=self.__BG,
            activebackground=self.__ABG,
            highlightbackground=self.__BG,
        )
        # create a horizontal Scrollbar by setting orient to horizontal
        _horizontal_scrollbar = Scrollbar(
            self._root,
            bd=0,
            bg=self.__ABG,
            orient='horizontal',
            elementborderwidth=0,
            highlightthickness=0,
            troughcolor=self.__BG,
            highlightcolor=self.__BG,
            activebackground=self.__ABG,
            highlightbackground=self.__BG,
        )

        """Text widgets"""
        # create a Text widget for displaying the generated tree of directories
        _text_widget = Text(
            self._root,
            bd=0,
            width=98,
            height=35,
            wrap=NONE,
            bg=self.__BG,
            fg=self.__FG,
            highlightbackground=self.__BG,
            xscrollcommand=_horizontal_scrollbar.set,
            yscrollcommand=_vertical_scrollbar.set
        )

        """Label widgets"""
        _dir_only_label = Label(
            self._root,
            font=1,
            width=1,
            anchor="w",
            bg="grey10",
            fg=self.__FG,
            text=f"Check for directory-only tree",
        )
        _error_label = Label(
            self._root,
            font=1,
            justify=LEFT,
            bg=self.__HBG,
            fg=self.__MESSAGE_FG,
        )

        """Checkbutton widgets"""
        _dir_only_check_button = Checkbutton(
            self._root,
            bd=0,
            fg=self.__AFG,
            bg=self.__HBG,
            onvalue=True,
            offvalue=False,
            highlightthickness=0,
            variable=self._dir_only,
            activebackground=self.__BG,
        )

        """Button widgets"""
        _choose_directory_button = Button(
            self._root,
            bd=0,
            font=1,
            bg=self.__BG,
            fg=self.__FG,
            text=f'Choose directory',
            activebackground=self.__ABG,
            activeforeground=self.__AFG,
            highlightbackground=self.__HBG,
            command=lambda: self._get_root_dir_path(),
        )
        _generate_button = Button(
            self._root,
            bd=0,
            font=1,
            bg=self.__BG,
            fg=self.__FG,
            text='Generate',
            activebackground=self.__ABG,
            activeforeground=self.__AFG,
            highlightbackground=self.__HBG,
            command=lambda: self._generate_tree(),
        )
        _output_file_name_button = Button(
            self._root,
            bd=0,
            font=1,
            bg=self.__BG,
            fg=self.__FG,
            text=f"Choose file name (current: '{self._output_file_name.get()}')",
            activebackground=self.__ABG,
            activeforeground=self.__AFG,
            highlightbackground=self.__HBG,
            command=lambda: self._render_file_name_pop_up(),
        )
        _export_button = Button(
            self._root,
            bd=0,
            font=1,
            bg=self.__BG,
            fg=self.__FG,
            text="Export",
            activebackground=self.__ABG,
            activeforeground=self.__AFG,
            highlightbackground=self.__HBG,
            command=lambda: self._get_output_file_path(),
        )

        # here command represents the method to be executed
        # xview is executed on object 'text_widget'
        # Here 'text_widget' may represent any widget
        _horizontal_scrollbar.config(command=_text_widget.xview)

        # here command represents the method to be executed
        # yview is executed on object 'text_widget'
        # Here 'text_widget' may represent any widget
        _vertical_scrollbar.config(command=_text_widget.yview)

        # if tree is not None than insert it's string representation in the Text widget
        # and set Text widget state to "disabled" so the user cannot change the text inside the widget
        _text_widget.insert(END, str(self._tree) if self._tree is not None else "")
        _text_widget.configure(state="disabled")

        # clear root window
        self.clear_view(self._root)

        # position all widgets in the root window
        _vertical_scrollbar.grid(row=0, column=3, sticky="NWS")
        _horizontal_scrollbar.grid(row=1, column=0, sticky="WNE", columnspan=4)
        _text_widget.grid(row=0, column=0, columnspan=3, sticky="W")
        _dir_only_label.grid(row=2, column=0, sticky="ENW")
        _dir_only_check_button.grid(row=2, column=1, sticky="W", )
        _choose_directory_button.grid(row=3, columnspan=4, sticky="WNE")
        _generate_button.grid(row=4, column=0, columnspan=4, sticky="ENW", )

        if self._tree is not None:
            _output_file_name_button.grid(row=6, columnspan=4, sticky="WNE")
            _export_button.grid(row=7, columnspan=4, sticky="WNE")

        if message:
            _error_label.configure(text=message)
            _error_label.grid(row=8, columnspan=4, sticky="W")

    def _generate_tree(self,) -> None:
        #  Try to generate directory tree. If provided directory path is not a directory
        #  call tree view with error else assign the generated tree to self._tree attribute
        try:
            self._tree = create_tree(self._root_dir_path, self._dir_only.get())
        except NotADirectoryError:
            self.render(f"Directory {self._root_dir_path} does not exist!")
            return

        self.render()

    def _export(self) -> None:
        # Try to export generated tree in markdown format file
        # and generate a message for the render method
        if not self._output_file_name.get():
            self._reset_output_file_name()

        directory, file = self._output_dir_path, self._output_file_name.get()
        try:
            self._tree.export_tree_to_markdown_file(directory, file)
            message = f"File '{file}' exported successfully in\n'{directory}'"
        except FileNotFoundError:
            message = f"'{directory}' directory does not exist"
        except FileExistsError:
            message = f"'{file}' already exists in '{directory}'"
        except PermissionError:
            message = f"You have no permission to save '{file}' in '{directory}'"

        self._reset_output_file_name()
        self.render(message=message)

    def _get_root_dir_path(self):
        self._root_dir_path = open_window()

    def _get_output_file_path(self):
        self._output_dir_path = open_window()
        self._export()

    def _render_file_name_pop_up(self):
        self._top = Toplevel(
            self._root,
            bg=self.__BG,
        )
        self._top.wm_transient(self._root)
        self._top.geometry("800x200")
        self._top.title("Enter File Name")
        self._top.wm_resizable(False, False)
        self._top.protocol("WM_DELETE_WINDOW", self._validate_output_file_name)

        entry = Entry(
            self._top,
            bd=0,
            font=1,
            width=70,
            bg=self.__BG,
            fg=self.__FG,
            insertbackground=self.__FG,
            highlightcolor=self.__FG,
            textvariable=self._output_file_name,
        )
        exit_button = Button(
            self._top,
            bd=0,
            font=1,
            text="OK",
            bg=self.__BG,
            fg=self.__FG,
            width=7,
            activebackground=self.__ABG,
            activeforeground=self.__AFG,
            command=lambda: self._validate_output_file_name(),
        )

        self._output_file_name.set("")
        entry.grid(row=0, column=0, sticky="NS")
        exit_button.grid(row=0, column=1, sticky="W")

    def _validate_output_file_name(self):
        file_name = self._output_file_name.get()
        bad_characters = "!@#$%^&*()+{}[],:;'\"/\\"
        if any([char in file_name for char in bad_characters]):
            message = f"File name cannot contain any of these characters:" \
                      f"\n{' '.join(bad_characters)}"
            self._reset_output_file_name()
            self._top.destroy()
            self._top = None
            self.render(message)
            return

        if not file_name:
            self._reset_output_file_name()

        if self._output_file_name.get().split(".")[-1] != "md":
            self._output_file_name.set(file_name + ".md")

        self._top.destroy()
        self._top = None
        self.render()

    def _reset_output_file_name(self):
        self._output_file_name.set(f"{now()}-dir-tree.md")
