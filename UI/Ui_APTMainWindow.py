# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\Ui_APTMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import UI.UI_APTMainWindow_Images


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1002, 745)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_2.setMaximumSize(QtCore.QSize(200, 30))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_1.setMaximumSize(QtCore.QSize(200, 30))
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout_2.addWidget(self.pushButton_1, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_7, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem, 1, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_6.setMinimumSize(QtCore.QSize(50, 25))
        self.pushButton_6.setMaximumSize(QtCore.QSize(75, 30))
        self.pushButton_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_7.addWidget(self.pushButton_6, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_6, 3, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame_2, 2, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 71, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem1, 1, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 71, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem2, 3, 2, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_9.setObjectName("gridLayout_9")
        spacerItem3 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem3, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setObjectName("label_3")
        self.gridLayout_9.addWidget(self.label_3, 1, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.frame_4)
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_9.addWidget(self.progressBar, 3, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame_4, 3, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableView = QtWidgets.QTableView(self.frame_3)
        self.tableView.setObjectName("tableView")
        self.gridLayout_3.addWidget(self.tableView, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame_3, 1, 0, 2, 1)
        self.frame_9 = QtWidgets.QFrame(self.frame)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(308, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 0, 0, 1, 1)
        self.frame_8 = QtWidgets.QFrame(self.frame_9)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_5 = QtWidgets.QLabel(self.frame_8)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/newPrefix/Logo.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_8, 0, 1, 1, 1)
        self.gridLayout_8.addWidget(self.frame_9, 0, 0, 1, 4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 71, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem5, 3, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem6, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1002, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionOpenMatFile = QtWidgets.QAction(MainWindow)
        self.actionOpenMatFile.setObjectName("actionOpenMatFile")
        self.actionChange_Destination_Directory = QtWidgets.QAction(MainWindow)
        self.actionChange_Destination_Directory.setObjectName("actionChange_Destination_Directory")
        self.actionMAnual = QtWidgets.QAction(MainWindow)
        self.actionMAnual.setObjectName("actionMAnual")
        self.actionSemi_Auto_OCR = QtWidgets.QAction(MainWindow)
        self.actionSemi_Auto_OCR.setObjectName("actionSemi_Auto_OCR")
        self.menuMenu.addAction(self.actionOpenMatFile)
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LHT-Image Analyzer"))
        self.pushButton_1.setText(_translate("MainWindow", "View DataFrame"))
        self.pushButton_6.setText(_translate("MainWindow", "Next"))
        self.label_3.setText(_translate("MainWindow", "Calculating OCR in Progress.."))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionOpenMatFile.setText(_translate("MainWindow", "Open .mat file"))
        self.actionChange_Destination_Directory.setText(_translate("MainWindow", "Change Destination Directory"))
        self.actionMAnual.setText(_translate("MainWindow", "Manual"))
        self.actionSemi_Auto_OCR.setText(_translate("MainWindow", "Semi-Auto (OCR)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
