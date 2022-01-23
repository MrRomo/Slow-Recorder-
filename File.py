import cv2
from math import floor


class File:
    def __init__(self, folder, progress):
        self.folder = folder
        self.progress = progress

    def save_picture(self, name, img):
        cv2.imwrite(f'{self.folder}/{name}', img)

    def save_video(self, name, n):
        self.progress = 0
        out = cv2.VideoWriter(
            f'{self.folder}/{name}.avi', -1, 20.0, (640, 480))

        for i in range(n):
            self.progress = floor(1/n*100)
            frame = cv2.imread(f'{self.folder}/{name}{i}.jpg')
            out.write(frame)
            
        self.progress = 100
        out.release()
