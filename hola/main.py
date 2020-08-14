from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import Qt

from hola.log import logger
from hola.utils import BaseWindow

class MainWindow(BaseWindow, QWidget):
    ui_file = 'hola/ui/main.ui'
    def __init__(self, ui_file=None, parent=None):
        super().__init__(parent)
        ui_file = self.ui_file or ui_file
        print(ui_file)
        # 设置窗口透明度
        self.setWindowOpacity(0.5)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint)
        self.load_ui(ui_file)
