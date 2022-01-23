from threading import Thread
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QThread, pyqtSignal
from File import File
from time import sleep as delay


class FileManager:
    def __init__(self, folder_input, progress_bar, progress_label):
        self.folder = ''
        self.progress_bar = progress_bar
        self.progress_label = progress_label
        self.file = File(self.folder, progress_bar)
        self.folder_input = folder_input
        self.translate = QtCore.QCoreApplication.translate
        self.start_progress_sequence()

    def select_folder(self):
        dialog = QtWidgets.QFileDialog()
        self.folder = dialog.getExistingDirectory(
            caption='Select save directory')
        self.folder_input.setText(self.translate("SlowRecord", self.folder))

    def start_progress_sequence(self):
        self.progress_thread = ThreadProgress()
        self.progress_thread.progress.connect(self.set_progress_value)
        self.progress_thread.msg.connect(self.set_progress_msg)
        self.progress_thread.start()

    def set_progress_value(self, i):
        self.progress_bar.setProperty("value", i)
    
    def set_progress_msg(self, msg):
        self.progress_label.setText(self.translate("SlowRecord", msg))


class ThreadProgress(QThread):
    progress = pyqtSignal(int)
    msg = pyqtSignal(str)

    def run(self):
        delay(2)
        for i in range(100):
            self.progress.emit(i)
            self.msg.emit(f'Loading {i}%')
            delay(0.005)

        for i in range(100):
            self.progress.emit(100-i)
            self.msg.emit(f'Loading {100-i}%')
            delay(0.001)

        self.progress.emit(0)
        self.msg.emit(f'Ready')
        