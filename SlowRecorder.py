from PyQt5 import QtWidgets
from PyQt5.QtGui import QValidator, QIntValidator
from LanguageManager import LanguageManager
from PrinterManager import PrinterManager
from UI.QT_Engine import Ui_SlowRecord
from CameraManager import CameraManager
from FileManager import FileManager
from time import sleep as delay
import sys
import threading


class SlowRecorder():

    def __init__(self):
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

        # Print time params
        self.time_params = {
            "print_time_input": self.ui.print_time_input,
            "print_time_selector": self.ui.print_time_selector,
            "duration_time_input": self.ui.duration_input,
            "duration_time_selector": self.ui.duration_time_selector,
        }
        self.setValidators()

        # config
        self.camera_selector = self.ui.camera_selector
        self.camera_viewer = self.ui.camera_viewer
        self.folder_input = self.ui.output_folder_input

        # Buttons
        self.watch_button = self.ui.watch_button
        self.select_folder_button = self.ui.output_folder_tool
        self.start_button = self.ui.start_button
        self.cancel_button = self.ui.cancel_button

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
        self.printer_manager = PrinterManager(
            self.time_params, self.file_manager, self.camera_manager)
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
        self.start_button.clicked.connect(self.printer_manager.start_record)
        self.cancel_button.clicked.connect(self.printer_manager.cancel_record)
        # self.time_params['print_time_input'].textChanged.connect(
        #     self.setValidators)

    def setValidators(self):
        self.time_params['print_time_input'].setValidator(
            QIntValidator(0, 1000))
        self.time_params['duration_time_input'].setValidator(
            QIntValidator(0, 1000))
# duration_time_input
