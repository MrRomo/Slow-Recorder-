import imp
from PyQt5 import QtWidgets, QtCore

class FileManager:
    def __init__(self, folder_input):
        self.folder = ''
        self.folder_input = folder_input
        self.translate = QtCore.QCoreApplication.translate

    def select_folder(self):
        dialog = QtWidgets.QFileDialog()
        self.folder = dialog.getExistingDirectory(caption='Select save directory')
        self.folder_input.setText(self.translate("SlowRecord", self.folder))


