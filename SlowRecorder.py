from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QThread, QUrl
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

        self.MainWindow.show()

        # config
        self.camera_selector = self.ui.camera_selector
        self.camera_viewer = self.ui.camera_viewer
        self.folder = self.ui.output_folder_input

        # self.translate = self.ui.translate
        # self.portSelector = self.ui.portSelector
        # self.baudSelector = self.ui.baudSelector
        # self.hexBox = self.ui.hexBox
        # self.console = self.ui.console_thread

        # Buttons
        self.watch_button = self.ui.watch_button
        self.select_folder_button = self.ui.output_folder_tool
        # self.flashButton = self.ui.flashButton
        # self.eraseButton = self.ui.eraseButton
        # self.sendButton = self.ui.sendButton
        # #acciotns
        # self.openFile = self.ui.actionOpen

        # Init Managers
        delay(1)
        self.camera_manager = CameraManager(
            self.camera_selector, self.timelapse_started,
            self.camera_viewer, self.watch_button,
            self.watch_active)
        self.file_manager = FileManager(self.folder)
        # Init Signals
        self.startSignals()
    #   self.thread = QThread()
    #   self.worker = ThreadWatch()
    #   self.worker.moveToThread(self.thread)
    #     self.thread.started.connect(self.worker.run)
    #     self.worker.finished.connect(self.thread.quit)
    #     self.worker.changePixmap.connect(self.camera_manager.setImage)
    #     self.worker.active_watch.connect(self.camera_manager.setImage)
    #     self.thread.start()

    def startThread(self, function):
        threading.Thread(target=function, daemon=True).start()

    def startQThread(self, Worker, slot, callback):
        thread = QThread()
        worker = Worker()
        worker.moveToThread(thread)
        thread.started.connect(worker.run)
        signal = getattr(worker, slot)
        signal(worker).connect(callback)
        return thread

    def startSignals(self):
        self.camera_selector.currentIndexChanged.connect(
            self.camera_manager.change_camera)
        self.watch_button.clicked.connect(self.camera_manager.toggle_watch)
        self.select_folder_button.clicked.connect(self.file_manager.select_folder)

    def startThreads(self):
        self.setImageThread = self.startQThread(
            ThreadWatch, 'changePixmap', self.camera_manager.setImage)
        self.setImageThread.start()

        