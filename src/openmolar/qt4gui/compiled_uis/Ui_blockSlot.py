# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/neil/openmolar/openmolar1/src/openmolar/qt-designer/blockSlot.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from gettext import gettext as _
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(345, 361)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 2, 1)
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 3, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 34, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 2)
        self.blockStart_frame = QtWidgets.QFrame(self.tab)
        self.blockStart_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.blockStart_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.blockStart_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.blockStart_frame.setObjectName("blockStart_frame")
        self.gridLayout.addWidget(self.blockStart_frame, 1, 1, 1, 1)
        self.blockEnd_frame = QtWidgets.QFrame(self.tab)
        self.blockEnd_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.blockEnd_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.blockEnd_frame.setObjectName("blockEnd_frame")
        self.gridLayout.addWidget(self.blockEnd_frame, 2, 1, 1, 1)
        self.length_label = QtWidgets.QLabel(self.tab)
        self.length_label.setAlignment(QtCore.Qt.AlignCenter)
        self.length_label.setObjectName("length_label")
        self.gridLayout.addWidget(self.length_label, 1, 2, 2, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 4)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setMinimumSize(QtCore.QSize(100, 0))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 3)
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setMinimumSize(QtCore.QSize(100, 0))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 3)
        self.pt_label = QtWidgets.QLabel(self.tab_2)
        self.pt_label.setMinimumSize(QtCore.QSize(0, 50))
        self.pt_label.setTextFormat(QtCore.Qt.AutoText)
        self.pt_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pt_label.setObjectName("pt_label")
        self.gridLayout_2.addWidget(self.pt_label, 3, 0, 1, 3)
        self.changePt_pushButton = QtWidgets.QPushButton(self.tab_2)
        self.changePt_pushButton.setObjectName("changePt_pushButton")
        self.gridLayout_2.addWidget(self.changePt_pushButton, 3, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 4, 0, 1, 3)
        self.reason_comboBox = QtWidgets.QComboBox(self.tab_2)
        self.reason_comboBox.setObjectName("reason_comboBox")
        self.gridLayout_2.addWidget(self.reason_comboBox, 4, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 99, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 5, 2, 1, 1)
        self.length_spinBox = QtWidgets.QSpinBox(self.tab_2)
        self.length_spinBox.setMinimum(-600)
        self.length_spinBox.setMaximum(600)
        self.length_spinBox.setSingleStep(5)
        self.length_spinBox.setObjectName("length_spinBox")
        self.gridLayout_2.addWidget(self.length_spinBox, 2, 3, 1, 1)
        self.startTime_frame = QtWidgets.QFrame(self.tab_2)
        self.startTime_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.startTime_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.startTime_frame.setObjectName("startTime_frame")
        self.gridLayout_2.addWidget(self.startTime_frame, 1, 3, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Options"))
        self.label.setText(_("Would you like to Block (or partially Block) this Slot?"))
        self.label_3.setText(_("Block Start"))
        self.label_4.setText(_("Bock End"))
        self.label_2.setText(_("Text to apply"))
        self.comboBox.setItemText(0, _("//Blocked//"))
        self.comboBox.setItemText(1, _("Emergency"))
        self.comboBox.setItemText(2, _("Reserved Clinical Time"))
        self.comboBox.setItemText(3, _("Out of Office"))
        self.comboBox.setItemText(4, _("Lunch"))
        self.comboBox.setItemText(5, _("Catch up time"))
        self.comboBox.setItemText(6, _("Phone Call"))
        self.length_label.setText(_("minutes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _("Insert a Block"))
        self.label_7.setText(_("Insert A Patient into this slot?"))
        self.label_5.setText(_("Start Time"))
        self.label_6.setText(_("Length"))
        self.pt_label.setText(_("Chosen Patient is<br />"))
        self.changePt_pushButton.setText(_("Change"))
        self.label_9.setText(_("Reason for appointment is"))
        self.length_spinBox.setSuffix(_(" minutes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _("Insert a Known Patient"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

