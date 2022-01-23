# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/QT_Engine.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SlowRecord(object):
    def setupUi(self, SlowRecord):
        SlowRecord.setObjectName("SlowRecord")
        SlowRecord.setWindowModality(QtCore.Qt.NonModal)
        SlowRecord.resize(657, 507)
        self.viewer_title = QtWidgets.QLabel(SlowRecord)
        self.viewer_title.setGeometry(QtCore.QRect(120, 20, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.viewer_title.setFont(font)
        self.viewer_title.setAlignment(QtCore.Qt.AlignCenter)
        self.viewer_title.setObjectName("viewer_title")
        self.config_title = QtWidgets.QLabel(SlowRecord)
        self.config_title.setGeometry(QtCore.QRect(400, 20, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.config_title.setFont(font)
        self.config_title.setAlignment(QtCore.Qt.AlignCenter)
        self.config_title.setObjectName("config_title")
        self.line = QtWidgets.QFrame(SlowRecord)
        self.line.setGeometry(QtCore.QRect(380, 60, 21, 241))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.camera_selector = QtWidgets.QComboBox(SlowRecord)
        self.camera_selector.setGeometry(QtCore.QRect(490, 70, 131, 26))
        self.camera_selector.setObjectName("camera_selector")
        self.camera_selector.addItem("")
        self.camera_selector.addItem("")
        self.device_label = QtWidgets.QLabel(SlowRecord)
        self.device_label.setGeometry(QtCore.QRect(410, 70, 60, 21))
        self.device_label.setObjectName("device_label")
        self.duration_label = QtWidgets.QLabel(SlowRecord)
        self.duration_label.setGeometry(QtCore.QRect(410, 110, 60, 21))
        self.duration_label.setObjectName("duration_label")
        self.output_title = QtWidgets.QLabel(SlowRecord)
        self.output_title.setGeometry(QtCore.QRect(230, 330, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.output_title.setFont(font)
        self.output_title.setAlignment(QtCore.Qt.AlignCenter)
        self.output_title.setObjectName("output_title")
        self.line_2 = QtWidgets.QFrame(SlowRecord)
        self.line_2.setGeometry(QtCore.QRect(40, 310, 581, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.duration_input = QtWidgets.QLineEdit(SlowRecord)
        self.duration_input.setGeometry(QtCore.QRect(490, 110, 61, 21))
        self.duration_input.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.duration_input.setObjectName("duration_input")
        self.duration_time_selector = QtWidgets.QComboBox(SlowRecord)
        self.duration_time_selector.setGeometry(QtCore.QRect(560, 109, 61, 26))
        self.duration_time_selector.setObjectName("duration_time_selector")
        self.duration_time_selector.addItem("")
        self.duration_time_selector.addItem("")
        self.duration_time_selector.addItem("")
        self.print_time_input = QtWidgets.QLineEdit(SlowRecord)
        self.print_time_input.setGeometry(QtCore.QRect(490, 150, 61, 21))
        self.print_time_input.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.print_time_input.setObjectName("print_time_input")
        self.print_time_selector = QtWidgets.QComboBox(SlowRecord)
        self.print_time_selector.setGeometry(QtCore.QRect(560, 149, 61, 26))
        self.print_time_selector.setObjectName("print_time_selector")
        self.print_time_selector.addItem("")
        self.print_time_selector.addItem("")
        self.print_time_selector.addItem("")
        self.print_time_label = QtWidgets.QLabel(SlowRecord)
        self.print_time_label.setGeometry(QtCore.QRect(410, 150, 71, 21))
        self.print_time_label.setObjectName("print_time_label")
        self.camera_viewer = QtWidgets.QLabel(SlowRecord)
        self.camera_viewer.setGeometry(QtCore.QRect(50, 60, 331, 241))
        self.camera_viewer.setText("")
        self.camera_viewer.setPixmap(QtGui.QPixmap("UI/sample.png"))
        self.camera_viewer.setScaledContents(True)
        self.camera_viewer.setObjectName("camera_viewer")
        self.output_folder_label = QtWidgets.QLabel(SlowRecord)
        self.output_folder_label.setGeometry(QtCore.QRect(60, 370, 101, 20))
        self.output_folder_label.setObjectName("output_folder_label")
        self.output_folder_input = QtWidgets.QLineEdit(SlowRecord)
        self.output_folder_input.setGeometry(QtCore.QRect(150, 370, 401, 21))
        self.output_folder_input.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.output_folder_input.setObjectName("output_folder_input")
        self.output_folder_tool = QtWidgets.QToolButton(SlowRecord)
        self.output_folder_tool.setGeometry(QtCore.QRect(560, 370, 26, 22))
        self.output_folder_tool.setObjectName("output_folder_tool")
        self.start_button = QtWidgets.QPushButton(SlowRecord)
        self.start_button.setGeometry(QtCore.QRect(410, 210, 113, 32))
        self.start_button.setObjectName("start_button")
        self.cancel_button = QtWidgets.QPushButton(SlowRecord)
        self.cancel_button.setGeometry(QtCore.QRect(520, 210, 113, 32))
        self.cancel_button.setObjectName("cancel_button")
        self.progressBar = QtWidgets.QProgressBar(SlowRecord)
        self.progressBar.setGeometry(QtCore.QRect(60, 400, 531, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.output_folder_label_2 = QtWidgets.QLabel(SlowRecord)
        self.output_folder_label_2.setGeometry(QtCore.QRect(240, 420, 161, 20))
        self.output_folder_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.output_folder_label_2.setObjectName("output_folder_label_2")
        self.watch_button = QtWidgets.QPushButton(SlowRecord)
        self.watch_button.setGeometry(QtCore.QRect(462, 250, 121, 32))
        self.watch_button.setObjectName("watch_button")

        self.retranslateUi(SlowRecord)
        self.duration_time_selector.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(SlowRecord)

    def retranslateUi(self, SlowRecord):
        _translate = QtCore.QCoreApplication.translate
        SlowRecord.setWindowTitle(_translate("SlowRecord", "Slow Recorder"))
        self.viewer_title.setText(_translate("SlowRecord", "Viewer"))
        self.config_title.setText(_translate("SlowRecord", "Config"))
        self.camera_selector.setItemText(0, _translate("SlowRecord", "Camara 1"))
        self.camera_selector.setItemText(1, _translate("SlowRecord", "Camara 2"))
        self.device_label.setText(_translate("SlowRecord", "Device"))
        self.duration_label.setText(_translate("SlowRecord", "Duration"))
        self.output_title.setText(_translate("SlowRecord", "Output"))
        self.duration_input.setText(_translate("SlowRecord", "15"))
        self.duration_time_selector.setItemText(0, _translate("SlowRecord", "h"))
        self.duration_time_selector.setItemText(1, _translate("SlowRecord", "m"))
        self.duration_time_selector.setItemText(2, _translate("SlowRecord", "s"))
        self.print_time_input.setText(_translate("SlowRecord", "6"))
        self.print_time_selector.setItemText(0, _translate("SlowRecord", "h"))
        self.print_time_selector.setItemText(1, _translate("SlowRecord", "m"))
        self.print_time_selector.setItemText(2, _translate("SlowRecord", "s"))
        self.print_time_label.setText(_translate("SlowRecord", "Print Time"))
        self.output_folder_label.setText(_translate("SlowRecord", "Ourput Folder"))
        self.output_folder_input.setText(_translate("SlowRecord", "/media/folder/app"))
        self.output_folder_tool.setText(_translate("SlowRecord", "..."))
        self.start_button.setText(_translate("SlowRecord", "Start"))
        self.cancel_button.setText(_translate("SlowRecord", "Cancel"))
        self.output_folder_label_2.setText(_translate("SlowRecord", "time left: 45:87:12"))
        self.watch_button.setText(_translate("SlowRecord", "Start watch"))
