from PyQt5 import QtWidgets
from UI.QT_Engine import Ui_SlowRecord
from CameraManager import CameraManager, ThreadWatch
from time import sleep as delay
import sys
import threading


class SlowRecorder():

    def __init__(self):
        self.ports = []
        self.MainWindow = None
        self.ui = None

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

        # self.translate = self.ui.translate
        # self.portSelector = self.ui.portSelector
        # self.baudSelector = self.ui.baudSelector
        # self.hexBox = self.ui.hexBox
        # self.console = self.ui.console_thread

        # #Buttons
        # self.connectButton = self.ui.connectButton
        # self.flashButton = self.ui.flashButton
        # self.eraseButton = self.ui.eraseButton
        # self.sendButton = self.ui.sendButton
        # #acciotns
        # self.openFile = self.ui.actionOpen

        # Init Managers
        delay(1)
        self.camera_manager = CameraManager(
            self.camera_selector, self.timelapse_started, self.camera_viewer)
        # self.serialManager = SerialManager(self.consoleManager, self.ui, self.app)
        # self.fileManager = FileManager(self.hexBox, self.ui)
        # self.burnerManager = BurnerManager(self.serialManager, self.fileManager, self.ui.progressBar, self.consoleManager)
        self.startSignals()
        # self.startThreads()

    def startThread(self, function):
        threading.Thread(target=function, daemon=True).start()

    # def startQThread(self, signal, object, callback):
    #     th = ThreadWatch(object)
    #     signal = getattr(ThreadWatch, signal)
    #     signal(th).connect(callback)
    #     th.start()

    def startSignals(self):
        self.camera_selector.currentIndexChanged.connect(
            self.camera_manager.change_camera)
    #     self.connectButton.clicked.connect(self.serialManager.connect)
    #     self.eraseButton.clicked.connect(self.serialManager.change_port)
    #     self.flashButton.clicked.connect(self.burnerManager.burn)
    #     self.sendButton.clicked.connect(self.serialManager.send_write)
    #     self.openFile.triggered.connect(self.fileManager.open_file)

    # def startThreads(self):
    #     self.startQThread(
    #         'changePixmap', self.camera_manager.setImage, self.camera_manager.setImage)
    #     # self.startThread(self.camera_manager.active_watch)
        # self.startThread(self.serialManager.port_selector_observer)
        # self.startThread(self.serialManager.read_port)
        # self.startThread(self.burnerManager.burn_task)
