from PyQt5.QtWidgets import QMainWindow

from core.kiwoom import Kiwoom


class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.kiwoom = Kiwoom()
