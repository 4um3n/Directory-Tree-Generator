from tkinter import *
from GUI.helpers import create_tree, set_dir_path, export


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
        self._dir_only = BooleanVar()
        self._root_dir_path = StringVar()
        self._root_dir_path.set(".")

    def render(self, message: str = "") -> None:
        """Render tree view window"""

        """Scrollbar widgets"""
        # create a vertical Scrollbar - no need to write orient as it is by default vertical
        vertical_scrollbar = Scrollbar(
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
        horizontal_scrollbar = Scrollbar(
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
        text_widget = Text(
            self._root,
            bd=0,
            width=98,
            height=35,
            wrap=NONE,
            bg=self.__BG,
            fg=self.__FG,
            highlightbackground=self.__BG,
            xscrollcommand=horizontal_scrollbar.set,
            yscrollcommand=vertical_scrollbar.set
        )

        """Label widgets"""
        dir_only_label = Label(
            self._root,
            font=1,
            width=1,
            anchor="w",
            bg="grey10",
            fg=self.__FG,
            text=f"Check for directory-only tree",
        )
        error_label = Label(
            self._root,
            font=1,
            justify=LEFT,
            bg=self.__HBG,
            fg=self.__MESSAGE_FG,
        )

        """Checkbutton widgets"""
        dir_only_check_button = Checkbutton(
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
        choose_directory_button = Button(
            self._root,
            bd=0,
            font=1,
            bg=self.__BG,
            fg=self.__FG,
            text=f'Choose directory',
            activebackground=self.__ABG,
            activeforeground=self.__AFG,
            highlightbackground=self.__HBG,
            command=lambda: set_dir_path(self._root_dir_path),
        )
        generate_button = Button(
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
        export_button = Button(
            self._root,
            bd=0,
            font=1,
            bg=self.__BG,
            fg=self.__FG,
            text="Export",
            activebackground=self.__ABG,
            activeforeground=self.__AFG,
            highlightbackground=self.__HBG,
            command=lambda: export(self._tree, self.render)
        )

        # here command represents the method to be executed
        # xview is executed on object 'text_widget'
        # Here 'text_widget' may represent any widget
        horizontal_scrollbar.config(command=text_widget.xview)

        # here command represents the method to be executed
        # yview is executed on object 'text_widget'
        # Here 'text_widget' may represent any widget
        vertical_scrollbar.config(command=text_widget.yview)

        # if tree is not None than insert it's string representation in the Text widget
        # and set Text widget state to "disabled" so the user cannot change the text inside the widget
        text_widget.insert(END, str(self._tree) if self._tree is not None else "")
        text_widget.configure(state="disabled")

        # clear root window
        self.clear_view(self._root)

        # position all widgets in the root window
        vertical_scrollbar.grid(row=0, column=3, sticky="NWS")
        horizontal_scrollbar.grid(row=1, column=0, sticky="WNE", columnspan=4)
        text_widget.grid(row=0, column=0, columnspan=3, sticky="W")
        dir_only_label.grid(row=2, column=0, sticky="ENW")
        dir_only_check_button.grid(row=2, column=1, sticky="W", )
        choose_directory_button.grid(row=3, columnspan=4, sticky="WNE")
        generate_button.grid(row=4, column=0, columnspan=4, sticky="ENW", )

        if self._tree is not None:
            export_button.grid(row=7, columnspan=4, sticky="WNE")

        if message:
            error_label.configure(text=message)
            error_label.grid(row=8, columnspan=4, sticky="W")

    def _generate_tree(self) -> None:
        self._tree = create_tree(self._root_dir_path.get(), self._dir_only.get())
        self.render()
