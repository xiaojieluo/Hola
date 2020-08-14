from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QObject, QFile


class BaseWindow(QObject):
    def __init__(self, ui_file=None, parent=None):
        super().__init__(parent)

    def load_ui(self, ui_file, parent=None):
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        # self.window = loader.load(ui_file)
        self.ui = loader.load(ui_file, parent)
        ui_file.close()