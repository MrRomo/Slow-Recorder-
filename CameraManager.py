import cv2
from Camera import Camera, list_cameras
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from time import sleep as delay
from collections import deque as dq


class CameraManager:

    def __init__(self, camera_selector, timelapse_start, camera_viewer, watch_button, watch_active):
        self.switching = False
        self.camera_selector = camera_selector
        self.timelapse_start = timelapse_start
        self.camera_viewer = camera_viewer
        self.watch_active = watch_active
        self.watch_button = watch_button
        self.camera_selector_thread = QueueThreadList()
        self.camera_selector_thread.change_value.connect(
            self.updateCameraSelector)
        self.camera_selector_thread.start()
        cameras = list_cameras()
        self.camera_selector_thread.queue.append(cameras)
        self.current_camera = cameras[0]
        self.translate = QtCore.QCoreApplication.translate

        # th = ThreadWatch()
        # th.changePixmap.connect(self.setImage)
        # th.start()

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

    def start_watch(self):
        self.watch_thread = ThreadWatch()
        self.watch_thread.changePixmap.connect(self.setImage)
        self.watch_button.setText(self.translate("SlowRecord", "Stop watch"))
        self.watch_thread.start()

    def stop_watch(self):
        self.camera_viewer.setPixmap(QtGui.QPixmap("UI/sample.png"))
        self.watch_button.setText(self.translate("SlowRecord", "Start watch"))
        self.watch_thread.stop()

    def toggle_watch(self):
        if(not self.switching):
            print('toggle')
            self.switching = True
            if(self.watch_active):
                self.start_watch()
            else:
                self.stop_watch()
            self.watch_active = not self.watch_active
            self.switching = False


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
    finished = pyqtSignal()
    changePixmap = pyqtSignal(QImage)
    active_watch = pyqtSignal(bool)

    def run(self):
        self.cap = cv2.VideoCapture(0)
        while True:
            ret, frame = self.cap.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                p = QImage(rgbImage, w, h, bytesPerLine, QImage.Format_RGB888)
                self.changePixmap.emit(p)
            delay(0.01)

    def stop(self):
        self.cap.release()
        self.quit()
