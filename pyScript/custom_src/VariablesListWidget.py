from PySide2.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLineEdit
from PySide2.QtCore import Qt

import json

from custom_src.VarsList_VarWidget import VarsList_VarWidget
from custom_src.GlobalAccess import GlobalStorage


class VariablesCustomListWidget(QWidget):
    def __init__(self, variables):
        super(VariablesCustomListWidget, self).__init__()

        self.variables = variables
        self.widgets = []
        self.currently_edited_var = ''
        self.ignore_name_line_edit_signal = False  # because disabling causes firing twice otherwise
        # self.data_type_line_edits = []  # same here

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(main_layout)

        self.recreate_ui()


    def recreate_ui(self):
        for w in self.widgets:
            w.hide()
            del w

        self.widgets.clear()
        # self.data_type_line_edits.clear()

        for v in self.variables:
            new_widget = VarsList_VarWidget(self, v)
            new_widget.name_le_editing_finished.connect(self.name_line_edit_editing_finished)
            self.widgets.append(new_widget)

        self.rebuild_ui()


    def rebuild_ui(self):
        for i in range(self.layout().count()):
            self.layout().removeItem(self.layout().itemAt(0))

        for w in self.widgets:
            self.layout().addWidget(w)


    def name_line_edit_editing_finished(self):
        var_widget: VarsList_VarWidget = self.sender()
        var_widget.name_line_edit.setEnabled(False)

        # search for name problems
        new_var_name = var_widget.name_line_edit.text()
        for v in self.variables:
            if v.name == new_var_name:
                var_widget.name_line_edit.setText(self.currently_edited_var.name)
                return

        var_widget.var.name = new_var_name


    def del_variable(self, var, var_widget):
        self.widgets.remove(var_widget)
        var_widget.setParent(None)
        del self.variables[self.variables.index(var)]
        self.recreate_ui()