from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QThread, QUrl
from LanguageManager import LanguageManager
from UI.QT_Engine import Ui_SlowRecord
from CameraManager import CameraManager, ThreadWatch
from FileManager import FileManager
from time import sleep as delay
import sys
import threading


class SlowRecorder():

    def __init__(self):
        self.ports = []
        self.MainWindow = None
        self.ui = None
        self.watch_active = True
        self.switching = False

    def startApp(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_SlowRecord()
        self.ui.setupUi(self.MainWindow)
        self.timelapse_started = False

        # config
        self.camera_selector = self.ui.camera_selector
        self.camera_viewer = self.ui.camera_viewer
        self.folder_input = self.ui.output_folder_input

        # Buttons
        self.watch_button = self.ui.watch_button
        self.select_folder_button = self.ui.output_folder_tool

        # indicators
        self.progress_bar = self.ui.progress_bar
        self.progress_label = self.ui.progress_label
        # #acciotns
        # self.openFile = self.ui.actionOpen

        # Init Managers
        self.camera_manager = CameraManager(
            self.camera_selector, self.timelapse_started,
            self.camera_viewer, self.watch_button,
            self.watch_active)
        self.file_manager = FileManager(
            self.folder_input, self.progress_bar, self.progress_label)
        self.language_manager = LanguageManager(self.ui)
        # Init Signals
        self.startSignals()

        # Init config
        self.config = self.file_manager.config
        
        # show ui
        self.MainWindow.show()

    def startThread(self, function):
        threading.Thread(target=function, daemon=True).start()

    def startSignals(self):
        self.camera_selector.currentIndexChanged.connect(
            self.camera_manager.change_camera)
        self.watch_button.clicked.connect(self.camera_manager.toggle_watch)
        self.select_folder_button.clicked.connect(
            self.file_manager.select_folder)
        self.folder_input.textChanged.connect(self.file_manager.change_folder)
