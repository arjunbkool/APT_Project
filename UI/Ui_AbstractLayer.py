# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_AbstractLayer.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(953, 733)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame)
        self.pushButton_15.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_15.setMaximumSize(QtCore.QSize(200, 30))
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_2.addWidget(self.pushButton_15, 3, 5, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setMaximumSize(QtCore.QSize(200, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.frame)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 3, 6, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.frame)
        self.pushButton_14.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_14.setMaximumSize(QtCore.QSize(200, 30))
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_2.addWidget(self.pushButton_14, 3, 3, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.frame)
        self.pushButton_16.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_16.setMaximumSize(QtCore.QSize(200, 30))
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_2.addWidget(self.pushButton_16, 3, 4, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(100, 30))
        self.textEdit.setMaximumSize(QtCore.QSize(100, 30))
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_4.addWidget(self.textEdit, 0, 1, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(100, 30))
        self.lineEdit_7.setMaximumSize(QtCore.QSize(100, 30))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_4.addWidget(self.lineEdit_7, 3, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMinimumSize(QtCore.QSize(100, 30))
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 4, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setMaximumSize(QtCore.QSize(200, 30))
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_4.addWidget(self.pushButton_11, 4, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QtCore.QSize(200, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.lineEdit_8.setMinimumSize(QtCore.QSize(100, 30))
        self.lineEdit_8.setMaximumSize(QtCore.QSize(100, 30))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_4.addWidget(self.lineEdit_8, 4, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QtCore.QSize(100, 30))
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 1, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(100, 30))
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QtCore.QSize(100, 30))
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 3, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_5.setMaximumSize(QtCore.QSize(100, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_4.addWidget(self.pushButton_5, 5, 2, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_4.addWidget(self.radioButton, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 2, 2)
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setMinimumSize(QtCore.QSize(500, 500))
        self.widget.setObjectName("widget")
        self.gridLayout_2.addWidget(self.widget, 0, 2, 3, 5)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_15.setToolTip(_translate("Dialog", "Export the final analyzed file for review later"))
        self.pushButton_15.setText(_translate("Dialog", "Export Final H5 file"))
        self.pushButton_3.setToolTip(_translate("Dialog", "Input the peak mapped file"))
        self.pushButton_3.setText(_translate("Dialog", "Input H5 file"))
        self.pushButton_14.setToolTip(_translate("Dialog", "Option to add ions to decompose as elements during count"))
        self.pushButton_14.setText(_translate("Dialog", "Decompose List*"))
        self.pushButton_16.setToolTip(_translate("Dialog", "The plot along with the counts are exported as Word report"))
        self.pushButton_16.setText(_translate("Dialog", "Report of Ion Counts (.docx)"))
        self.textEdit.setToolTip(_translate("Dialog", "Enter the ion using periodic table"))
        self.lineEdit_7.setToolTip(_translate("Dialog", "Min no: of points to form a dense region"))
        self.label_15.setText(_translate("Dialog", "Sigma"))
        self.pushButton_11.setToolTip(_translate("Dialog", "Plot the noises as red or after an invert function"))
        self.pushButton_11.setText(_translate("Dialog", "Plot Ions*"))
        self.pushButton_2.setToolTip(_translate("Dialog", "Plot the ion (if exact name exist)"))
        self.pushButton_2.setText(_translate("Dialog", "Plot Ions"))
        self.lineEdit_8.setToolTip(_translate("Dialog", "How close the points should be to be treated as single cluster"))
        self.label_13.setToolTip(_translate("Dialog", "Optional method to remove noises not needed in the ion cloud"))
        self.label_13.setText(_translate("Dialog", "Noise Removal using DBScan -> (optional*)"))
        self.label.setText(_translate("Dialog", "Layer Element"))
        self.label_14.setText(_translate("Dialog", "Min Points"))
        self.pushButton_5.setToolTip(_translate("Dialog", "Plot an envelope of the shape with the outside vertices of the cloud"))
        self.pushButton_5.setText(_translate("Dialog", "Plot Convex Hull"))
        self.radioButton.setToolTip(_translate("Dialog", "Possibility to reverse noises and detected clusters"))
        self.radioButton.setText(_translate("Dialog", "Invert DBScan"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
