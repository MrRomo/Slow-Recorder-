import json
import os
import cv2
from math import floor


class File:
    def __init__(self, progress):
        self.folder = None
        self.progress = progress

    def save_picture(self, name, img):
        url = f'{self.folder}/{name}.png'
        isDir = os.path.isdir(self.folder) 
        if(isDir):
            print("saving foto", img, url )
            cv2.imwrite(url, img)
        else:
            print('el directorio no existe')

    def save_video(self, name, n):
        self.progress = 0
        out = cv2.VideoWriter(
            f'{self.folder}/{name}.avi', -1, 20.0, (640, 480))

        for i in range(n):
            self.progress = floor(1/n*100)
            frame = cv2.imread(f'{self.folder}/{name}{i}.png')
            out.write(frame)
            
        self.progress = 100
        out.release()
    
    def load_config(self):
        try:        
            file = open('config.json', 'r')
            data = json.load(file)
        except FileNotFoundError:
            data = self.set_default_config()
        self.folder = data['folder']
        return data

    def set_default_config(self):
        default_config = {
            "lang": 'EN',
            "folder": os.getcwd()
        }
        self.save_config(default_config)
        return default_config

    def save_config(self, config):
        file = json.dumps(config)
        with open('config.json', 'w') as outfile:
            outfile.write(file)
        
