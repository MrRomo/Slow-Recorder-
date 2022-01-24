
from PyQt5.QtCore import QThread, pyqtSignal
from time import sleep as delay


class IntervalLoopThread(QThread):

    take_picture = pyqtSignal()
    check_loop = pyqtSignal()

    def run(self):
        while True:
            self.take_picture.emit()
            self.check_loop.emit()
            delay(self.delay)

    def stop(self):
        self.terminate()


class PrinterManager:
    def __init__(self, time_params, file_manager, camera_manager):
        self.time_params = time_params
        self.file_manager = file_manager
        self.camera_manager = camera_manager
        self.time = 0
        self.fps = 60
        self.takes = 0

    def calculate_time(self):
        self.print_format = self.time_params['print_time_selector'].currentText(
        )
        self.duration_format = self.time_params['duration_time_selector'].currentText(
        )
        self.print_time = self.convert_time(
            self.time_params['print_time_input'].text(), self.print_format)
        self.duration_time = self.convert_time(
            self.time_params['duration_time_input'].text(), self.duration_format)
        print(self.print_time, self.duration_time)
        self.interval = self.print_time / self.duration_time

    def start_record(self):
        print('starting record')
        self.calculate_time()
        self.takes = 0
        self.interval_loop_thread = IntervalLoopThread()
        self.interval_loop_thread.delay = self.interval
        self.interval_loop_thread.take_picture.connect(self.take_picture)
        self.interval_loop_thread.check_loop.connect(self.check_loop)
        self.interval_loop_thread.start()
        pass

    def convert_time(self, time, format):
        print(time, format)
        convertions = {
            's': lambda x: x,
            'm': lambda x: x*60,
            'h': lambda x: x*60*60,
        }
        return convertions[format](int(time))

    def cancel_record(self):
        pass

    def stop_record(self):
        pass

    def update_params(self):
        pass

    def disable_buttons(self):
        pass

    def take_picture(self):
        ret, frame = self.camera_manager.camera.take_picture()
        if(ret):
            self.file_manager.file.save_picture(f'nombre_{self.takes}', frame)
            self.takes += 1
            print("picture taked")
        pass

    def check_loop(self):
        print('checking loop')
        pass
