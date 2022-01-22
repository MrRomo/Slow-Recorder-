import cv2


class Camera:
    def __init__(self, index=0):
        self.index = index

    def take_picture(self):
        # video capture source camera (Here webcam of laptop)
        cap = cv2.VideoCapture(self.index)
        frame = cap.read()
        cap.release()
        return frame

def list_cameras ():
    index = 0
    arr = []
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            arr.append(index)
        cap.release()
        index += 1
    return arr

if __name__ == "__main__":
    camera = Camera(0)
    ret, frame = camera.take_picture()
    print(list_cameras())
