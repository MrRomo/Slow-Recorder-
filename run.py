from SlowRecorder import SlowRecorder
import sys


if __name__ == "__main__":

    app = SlowRecorder()
    app.startApp()
    sys.exit(app.app.exec_())