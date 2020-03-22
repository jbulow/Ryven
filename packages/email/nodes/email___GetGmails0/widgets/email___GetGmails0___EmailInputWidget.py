from PySide2.QtWidgets import QLineEdit
# from PySide2.QtCore import ...
from PySide2.QtGui import QFont, QFontMetrics


class EmailInputWidget_PortInstanceWidget(QLineEdit):
    def __init__(self, parent_port_instance, parent_node_instance):
        super(EmailInputWidget_PortInstanceWidget, self).__init__()

        # leave these lines ------------------------------
        self.parent_port_instance = parent_port_instance
        self.parent_node_instance = parent_node_instance
        # ------------------------------------------------

        self.setStyleSheet('''
            QLineEdit{
                border-radius: 10px;
                background-color: transparent;
                border: 1px solid #404040;
                color: #aaaaaa;
                padding: 3px;
            }
        ''')

        self.setFont(QFont('Corbel', 10))

        self.textChanged.connect(self.email_text_changed)


    def email_text_changed(self):
        fm = QFontMetrics(self.font())
        text_width = fm.width(self.text())
        new_width = text_width+2*10
        self.setFixedWidth(new_width if new_width > 150 else 150)
        self.parent_node_instance.update_shape()

    def get_val(self):
        return self.text()


    def get_data(self):
        data = {'text': self.text()}
        return data

    def set_data(self, data):
        self.setText(data['text'])


    def removing(self):
        pass # remove log here etc. ...
