import cv2 
from Camera import Camera, list_cameras
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QThread, Qt, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from time import sleep as delay
from collections import deque as dq


class QueueThreadList(QThread):
    # Create a counter thread
    change_value = pyqtSignal(list)

    def run(self):
        self.queue = dq(maxlen=200)
        while 1:
            if(len(self.queue)):
                msg = self.queue[0]
                self.queue.popleft()
                self.change_value.emit(msg)
            delay(1)

class ThreadWatch(QThread):
    changePixmap = pyqtSignal(QImage)

    def run(self):
        cap = cv2.VideoCapture(0)
        print('run watch')
        while True:
            ret, frame = cap.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)

class CameraManager:

    def __init__(self, camera_selector, timelapse_start, camera_viewer):
        self.camera_selector = camera_selector
        self.timelapse_start = timelapse_start
        self.camera_viewer = camera_viewer
        self.camera_selector_thread = QueueThreadList()
        self.camera_selector_thread.change_value.connect(
            self.updateCameraSelector)
        self.camera_selector_thread.start()
        cameras = list_cameras()
        self.camera_selector_thread.queue.append(cameras)
        self.current_camera = cameras[0]
        self.translate = QtCore.QCoreApplication.translate
        th = ThreadWatch()
        th.changePixmap.connect(self.setImage)
        th.start()


    def refresh_cameras(self):
        self.camera_selector_thread.queue.append(list_cameras())

    def updateCameraSelector(self, list_cameras):
        self.camera_selector.clear()
        for idx in list_cameras:
            self.camera_selector.addItem("")
            self.camera_selector.setItemText(
                idx, self.translate("MainWindow", f'Camera {idx}'))
        self.camera_selector.setCurrentIndex(0)

    def change_camera(self):
        print(self.camera_selector.currentIndex())
        # self.current_camera = self.ports[self.camera_selector.currentIndex()]['port']

    def setImage(self, image):
        self.camera_viewer.setPixmap(QPixmap.fromImage(image))