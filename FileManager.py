from threading import Thread
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QThread, pyqtSignal
from File import File
from time import sleep as delay


class FileManager:
    def __init__(self, folder_input, progress_bar, progress_label):
        self.progress_bar = progress_bar
        self.progress_label = progress_label
        self.file = File(progress_bar)
        self.config = self.file.load_config()
        self.folder_input = folder_input
        self.translate = QtCore.QCoreApplication.translate
        self.set_folder()
        self.start_progress_sequence()

    def select_folder(self):
        dialog = QtWidgets.QFileDialog()
        self.file.folder = dialog.getExistingDirectory(
            caption='Select save directory')
        self.config['folder'] = self.file.folder
        self.set_folder()
        self.file.save_config(self.config)

    def change_folder(self):
        self.file.folder = self.folder_input.text()
        print(self.file.folder)
        self.config['folder'] = self.file.folder
        self.file.save_config(self.config)

    def set_folder(self):
        self.folder_input.setText(
            self.translate("SlowRecord", self.file.folder))

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
