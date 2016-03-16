# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/neil/openmolar/openmolar1/src/openmolar/qt-designer/diary_widget.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from gettext import gettext as _
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(732, 551)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.diary_tabWidget = QtWidgets.QTabWidget(Form)
        self.diary_tabWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.diary_tabWidget.sizePolicy().hasHeightForWidth())
        self.diary_tabWidget.setSizePolicy(sizePolicy)
        self.diary_tabWidget.setObjectName("diary_tabWidget")
        self.tab_dayview = QtWidgets.QWidget()
        self.tab_dayview.setObjectName("tab_dayview")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_dayview)
        self.horizontalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_18 = QtWidgets.QFrame(self.tab_dayview)
        self.frame_18.setMinimumSize(QtCore.QSize(220, 0))
        self.frame_18.setMaximumSize(QtCore.QSize(220, 16777215))
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_19.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.dayCalendar_frame = QtWidgets.QWidget(self.frame_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dayCalendar_frame.sizePolicy().hasHeightForWidth())
        self.dayCalendar_frame.setSizePolicy(sizePolicy)
        self.dayCalendar_frame.setMinimumSize(QtCore.QSize(200, 180))
        self.dayCalendar_frame.setMaximumSize(QtCore.QSize(16777215, 200))
        self.dayCalendar_frame.setObjectName("dayCalendar_frame")
        self.verticalLayout_19.addWidget(self.dayCalendar_frame)
        self.goTodayPushButton = QtWidgets.QPushButton(self.frame_18)
        self.goTodayPushButton.setEnabled(True)
        self.goTodayPushButton.setMaximumSize(QtCore.QSize(16777215, 24))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/agt_reload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.goTodayPushButton.setIcon(icon)
        self.goTodayPushButton.setObjectName("goTodayPushButton")
        self.verticalLayout_19.addWidget(self.goTodayPushButton)
        self.day_view_control_frame = QtWidgets.QFrame(self.frame_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.day_view_control_frame.sizePolicy().hasHeightForWidth())
        self.day_view_control_frame.setSizePolicy(sizePolicy)
        self.day_view_control_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.day_view_control_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.day_view_control_frame.setLineWidth(0)
        self.day_view_control_frame.setObjectName("day_view_control_frame")
        self.verticalLayout_19.addWidget(self.day_view_control_frame)
        self.horizontalLayout_3.addWidget(self.frame_18)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.dayView_splitter = QtWidgets.QSplitter(self.tab_dayview)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dayView_splitter.sizePolicy().hasHeightForWidth())
        self.dayView_splitter.setSizePolicy(sizePolicy)
        self.dayView_splitter.setMinimumSize(QtCore.QSize(0, 300))
        self.dayView_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.dayView_splitter.setObjectName("dayView_splitter")
        self.gridLayout_2.addWidget(self.dayView_splitter, 1, 0, 1, 1)
        self.emergency_dayview_scroll_bar = QtWidgets.QScrollBar(self.tab_dayview)
        self.emergency_dayview_scroll_bar.setOrientation(QtCore.Qt.Vertical)
        self.emergency_dayview_scroll_bar.setObjectName("emergency_dayview_scroll_bar")
        self.gridLayout_2.addWidget(self.emergency_dayview_scroll_bar, 1, 1, 1, 1)
        self.appt_notes_webView = QtWebKitWidgets.QWebView(self.tab_dayview)
        self.appt_notes_webView.setMinimumSize(QtCore.QSize(0, 150))
        self.appt_notes_webView.setMaximumSize(QtCore.QSize(16777215, 200))
        self.appt_notes_webView.setProperty("url", QtCore.QUrl("about:blank"))
        self.appt_notes_webView.setObjectName("appt_notes_webView")
        self.gridLayout_2.addWidget(self.appt_notes_webView, 2, 0, 1, 2)
        self.daymemo_label = QtWidgets.QLabel(self.tab_dayview)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.daymemo_label.sizePolicy().hasHeightForWidth())
        self.daymemo_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.daymemo_label.setFont(font)
        self.daymemo_label.setAlignment(QtCore.Qt.AlignCenter)
        self.daymemo_label.setObjectName("daymemo_label")
        self.gridLayout_2.addWidget(self.daymemo_label, 0, 0, 1, 2)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.diary_tabWidget.addTab(self.tab_dayview, "")
        self.tab_weekview = QtWidgets.QWidget()
        self.tab_weekview.setObjectName("tab_weekview")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab_weekview)
        self.gridLayout_11.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_11.setSpacing(1)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.frame_8 = QtWidgets.QFrame(self.tab_weekview)
        self.frame_8.setMinimumSize(QtCore.QSize(220, 0))
        self.frame_8.setMaximumSize(QtCore.QSize(220, 16777215))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.weekCalendar_frame = QtWidgets.QWidget(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weekCalendar_frame.sizePolicy().hasHeightForWidth())
        self.weekCalendar_frame.setSizePolicy(sizePolicy)
        self.weekCalendar_frame.setMinimumSize(QtCore.QSize(30, 180))
        self.weekCalendar_frame.setMaximumSize(QtCore.QSize(16777215, 200))
        self.weekCalendar_frame.setObjectName("weekCalendar_frame")
        self.verticalLayout_3.addWidget(self.weekCalendar_frame)
        self.goto_current_week_PushButton = QtWidgets.QPushButton(self.frame_8)
        self.goto_current_week_PushButton.setEnabled(True)
        self.goto_current_week_PushButton.setMaximumSize(QtCore.QSize(16777215, 24))
        self.goto_current_week_PushButton.setIcon(icon)
        self.goto_current_week_PushButton.setObjectName("goto_current_week_PushButton")
        self.verticalLayout_3.addWidget(self.goto_current_week_PushButton)
        self.week_view_control_frame = QtWidgets.QFrame(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.week_view_control_frame.sizePolicy().hasHeightForWidth())
        self.week_view_control_frame.setSizePolicy(sizePolicy)
        self.week_view_control_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.week_view_control_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.week_view_control_frame.setLineWidth(0)
        self.week_view_control_frame.setObjectName("week_view_control_frame")
        self.verticalLayout_3.addWidget(self.week_view_control_frame)
        self.gridLayout_11.addWidget(self.frame_8, 0, 0, 2, 1)
        self.weekView_splitter = QtWidgets.QSplitter(self.tab_weekview)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weekView_splitter.sizePolicy().hasHeightForWidth())
        self.weekView_splitter.setSizePolicy(sizePolicy)
        self.weekView_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.weekView_splitter.setObjectName("weekView_splitter")
        self.layoutWidget = QtWidgets.QWidget(self.weekView_splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.day1_frame = QtWidgets.QFrame(self.layoutWidget)
        self.day1_frame.setMinimumSize(QtCore.QSize(0, 60))
        self.day1_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.day1_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.day1_frame.setLineWidth(2)
        self.day1_frame.setObjectName("day1_frame")
        self.gridLayout.addWidget(self.day1_frame, 0, 0, 1, 1)
        self.day2_frame = QtWidgets.QFrame(self.layoutWidget)
        self.day2_frame.setMinimumSize(QtCore.QSize(0, 40))
        self.day2_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.day2_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.day2_frame.setLineWidth(2)
        self.day2_frame.setObjectName("day2_frame")
        self.gridLayout.addWidget(self.day2_frame, 0, 1, 1, 1)
        self.day3_frame = QtWidgets.QFrame(self.layoutWidget)
        self.day3_frame.setMinimumSize(QtCore.QSize(0, 40))
        self.day3_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.day3_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.day3_frame.setLineWidth(2)
        self.day3_frame.setObjectName("day3_frame")
        self.gridLayout.addWidget(self.day3_frame, 0, 2, 1, 1)
        self.day4_frame = QtWidgets.QFrame(self.layoutWidget)
        self.day4_frame.setMinimumSize(QtCore.QSize(0, 40))
        self.day4_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.day4_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.day4_frame.setLineWidth(2)
        self.day4_frame.setObjectName("day4_frame")
        self.gridLayout.addWidget(self.day4_frame, 0, 3, 1, 1)
        self.day5_frame = QtWidgets.QFrame(self.layoutWidget)
        self.day5_frame.setMinimumSize(QtCore.QSize(0, 40))
        self.day5_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.day5_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.day5_frame.setLineWidth(2)
        self.day5_frame.setObjectName("day5_frame")
        self.gridLayout.addWidget(self.day5_frame, 0, 4, 1, 1)
        self.appt_OV_Frame1 = QtWidgets.QFrame(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.appt_OV_Frame1.sizePolicy().hasHeightForWidth())
        self.appt_OV_Frame1.setSizePolicy(sizePolicy)
        self.appt_OV_Frame1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.appt_OV_Frame1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.appt_OV_Frame1.setObjectName("appt_OV_Frame1")
        self.gridLayout.addWidget(self.appt_OV_Frame1, 1, 0, 1, 1)
        self.appt_OV_Frame2 = QtWidgets.QFrame(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.appt_OV_Frame2.sizePolicy().hasHeightForWidth())
        self.appt_OV_Frame2.setSizePolicy(sizePolicy)
        self.appt_OV_Frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.appt_OV_Frame2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.appt_OV_Frame2.setObjectName("appt_OV_Frame2")
        self.gridLayout.addWidget(self.appt_OV_Frame2, 1, 1, 1, 1)
        self.appt_OV_Frame3 = QtWidgets.QFrame(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.appt_OV_Frame3.sizePolicy().hasHeightForWidth())
        self.appt_OV_Frame3.setSizePolicy(sizePolicy)
        self.appt_OV_Frame3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.appt_OV_Frame3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.appt_OV_Frame3.setObjectName("appt_OV_Frame3")
        self.gridLayout.addWidget(self.appt_OV_Frame3, 1, 2, 1, 1)
        self.appt_OV_Frame4 = QtWidgets.QFrame(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.appt_OV_Frame4.sizePolicy().hasHeightForWidth())
        self.appt_OV_Frame4.setSizePolicy(sizePolicy)
        self.appt_OV_Frame4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.appt_OV_Frame4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.appt_OV_Frame4.setObjectName("appt_OV_Frame4")
        self.gridLayout.addWidget(self.appt_OV_Frame4, 1, 3, 1, 1)
        self.appt_OV_Frame5 = QtWidgets.QFrame(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.appt_OV_Frame5.sizePolicy().hasHeightForWidth())
        self.appt_OV_Frame5.setSizePolicy(sizePolicy)
        self.appt_OV_Frame5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.appt_OV_Frame5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.appt_OV_Frame5.setObjectName("appt_OV_Frame5")
        self.gridLayout.addWidget(self.appt_OV_Frame5, 1, 4, 1, 1)
        self.layoutWidget_2 = QtWidgets.QWidget(self.weekView_splitter)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.day6_frame = QtWidgets.QFrame(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.day6_frame.sizePolicy().hasHeightForWidth())
        self.day6_frame.setSizePolicy(sizePolicy)
        self.day6_frame.setMinimumSize(QtCore.QSize(0, 40))
        self.day6_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.day6_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.day6_frame.setLineWidth(2)
        self.day6_frame.setObjectName("day6_frame")
        self.verticalLayout_23.addWidget(self.day6_frame)
        self.appt_OV_Frame6 = QtWidgets.QFrame(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.appt_OV_Frame6.sizePolicy().hasHeightForWidth())
        self.appt_OV_Frame6.setSizePolicy(sizePolicy)
        self.appt_OV_Frame6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.appt_OV_Frame6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.appt_OV_Frame6.setObjectName("appt_OV_Frame6")
        self.verticalLayout_23.addWidget(self.appt_OV_Frame6)
        self.day7_frame = QtWidgets.QFrame(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.day7_frame.sizePolicy().hasHeightForWidth())
        self.day7_frame.setSizePolicy(sizePolicy)
        self.day7_frame.setMinimumSize(QtCore.QSize(0, 40))
        self.day7_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.day7_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.day7_frame.setLineWidth(2)
        self.day7_frame.setObjectName("day7_frame")
        self.verticalLayout_23.addWidget(self.day7_frame)
        self.appt_OV_Frame7 = QtWidgets.QFrame(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.appt_OV_Frame7.sizePolicy().hasHeightForWidth())
        self.appt_OV_Frame7.setSizePolicy(sizePolicy)
        self.appt_OV_Frame7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.appt_OV_Frame7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.appt_OV_Frame7.setObjectName("appt_OV_Frame7")
        self.verticalLayout_23.addWidget(self.appt_OV_Frame7)
        self.gridLayout_11.addWidget(self.weekView_splitter, 0, 1, 1, 1)
        self.diary_tabWidget.addTab(self.tab_weekview, "")
        self.tab_monthview = QtWidgets.QWidget()
        self.tab_monthview.setObjectName("tab_monthview")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_monthview)
        self.gridLayout_5.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.monthView_scrollArea = QtWidgets.QScrollArea(self.tab_monthview)
        self.monthView_scrollArea.setWidgetResizable(True)
        self.monthView_scrollArea.setObjectName("monthView_scrollArea")
        self.scrollAreaWidgetContents_14 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_14.setGeometry(QtCore.QRect(0, 0, 702, 456))
        self.scrollAreaWidgetContents_14.setObjectName("scrollAreaWidgetContents_14")
        self.monthView_scrollArea.setWidget(self.scrollAreaWidgetContents_14)
        self.gridLayout_5.addWidget(self.monthView_scrollArea, 0, 0, 1, 4)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem)
        self.aptOVprevmonth = QtWidgets.QPushButton(self.tab_monthview)
        self.aptOVprevmonth.setMaximumSize(QtCore.QSize(28, 20))
        self.aptOVprevmonth.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aptOVprevmonth.setIcon(icon1)
        self.aptOVprevmonth.setObjectName("aptOVprevmonth")
        self.horizontalLayout_22.addWidget(self.aptOVprevmonth)
        self.label_65 = QtWidgets.QLabel(self.tab_monthview)
        self.label_65.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_65.setAlignment(QtCore.Qt.AlignCenter)
        self.label_65.setObjectName("label_65")
        self.horizontalLayout_22.addWidget(self.label_65)
        self.aptOVnextmonth = QtWidgets.QPushButton(self.tab_monthview)
        self.aptOVnextmonth.setMaximumSize(QtCore.QSize(28, 20))
        self.aptOVnextmonth.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aptOVnextmonth.setIcon(icon2)
        self.aptOVnextmonth.setObjectName("aptOVnextmonth")
        self.horizontalLayout_22.addWidget(self.aptOVnextmonth)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem1)
        self.gridLayout_5.addLayout(self.horizontalLayout_22, 1, 2, 1, 1)
        self.printMonth_pushButton = QtWidgets.QPushButton(self.tab_monthview)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/ps.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.printMonth_pushButton.setIcon(icon3)
        self.printMonth_pushButton.setObjectName("printMonth_pushButton")
        self.gridLayout_5.addWidget(self.printMonth_pushButton, 1, 3, 1, 1)
        self.monthClinicians_checkBox = QtWidgets.QCheckBox(self.tab_monthview)
        self.monthClinicians_checkBox.setChecked(True)
        self.monthClinicians_checkBox.setObjectName("monthClinicians_checkBox")
        self.gridLayout_5.addWidget(self.monthClinicians_checkBox, 1, 0, 1, 1)
        self.monthView_clinicians_pushButton = QtWidgets.QPushButton(self.tab_monthview)
        self.monthView_clinicians_pushButton.setObjectName("monthView_clinicians_pushButton")
        self.gridLayout_5.addWidget(self.monthView_clinicians_pushButton, 1, 1, 1, 1)
        self.diary_tabWidget.addTab(self.tab_monthview, "")
        self.tab_yearview = QtWidgets.QWidget()
        self.tab_yearview.setObjectName("tab_yearview")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.tab_yearview)
        self.gridLayout_22.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.year_textBrowser = QtWidgets.QTextBrowser(self.tab_yearview)
        self.year_textBrowser.setMaximumSize(QtCore.QSize(16777215, 200))
        self.year_textBrowser.setObjectName("year_textBrowser")
        self.gridLayout_22.addWidget(self.year_textBrowser, 0, 0, 1, 3)
        self.yearView_frame = QtWidgets.QFrame(self.tab_yearview)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yearView_frame.sizePolicy().hasHeightForWidth())
        self.yearView_frame.setSizePolicy(sizePolicy)
        self.yearView_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.yearView_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.yearView_frame.setObjectName("yearView_frame")
        self.gridLayout_22.addWidget(self.yearView_frame, 1, 0, 1, 3)
        self.yearClinicians_checkBox = QtWidgets.QCheckBox(self.tab_yearview)
        self.yearClinicians_checkBox.setChecked(True)
        self.yearClinicians_checkBox.setObjectName("yearClinicians_checkBox")
        self.gridLayout_22.addWidget(self.yearClinicians_checkBox, 2, 0, 1, 1)
        self.yearView_clinicians_pushButton = QtWidgets.QPushButton(self.tab_yearview)
        self.yearView_clinicians_pushButton.setObjectName("yearView_clinicians_pushButton")
        self.gridLayout_22.addWidget(self.yearView_clinicians_pushButton, 2, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.aptOVprevyear = QtWidgets.QPushButton(self.tab_yearview)
        self.aptOVprevyear.setMaximumSize(QtCore.QSize(28, 20))
        self.aptOVprevyear.setText("")
        self.aptOVprevyear.setIcon(icon1)
        self.aptOVprevyear.setObjectName("aptOVprevyear")
        self.horizontalLayout_2.addWidget(self.aptOVprevyear)
        self.label_64 = QtWidgets.QLabel(self.tab_yearview)
        self.label_64.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_64.setAlignment(QtCore.Qt.AlignCenter)
        self.label_64.setObjectName("label_64")
        self.horizontalLayout_2.addWidget(self.label_64)
        self.aptOVnextyear = QtWidgets.QPushButton(self.tab_yearview)
        self.aptOVnextyear.setMaximumSize(QtCore.QSize(28, 20))
        self.aptOVnextyear.setText("")
        self.aptOVnextyear.setIcon(icon2)
        self.aptOVnextyear.setObjectName("aptOVnextyear")
        self.horizontalLayout_2.addWidget(self.aptOVnextyear)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout_22.addLayout(self.horizontalLayout_2, 2, 2, 1, 1)
        self.diary_tabWidget.addTab(self.tab_yearview, "")
        self.tab_agenda = QtWidgets.QWidget()
        self.tab_agenda.setObjectName("tab_agenda")
        self.gridLayout_agenda = QtWidgets.QGridLayout(self.tab_agenda)
        self.gridLayout_agenda.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_agenda.setSpacing(3)
        self.gridLayout_agenda.setObjectName("gridLayout_agenda")
        self.agenda_calendar_frame = QtWidgets.QWidget(self.tab_agenda)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agenda_calendar_frame.sizePolicy().hasHeightForWidth())
        self.agenda_calendar_frame.setSizePolicy(sizePolicy)
        self.agenda_calendar_frame.setMinimumSize(QtCore.QSize(220, 180))
        self.agenda_calendar_frame.setMaximumSize(QtCore.QSize(220, 200))
        self.agenda_calendar_frame.setObjectName("agenda_calendar_frame")
        self.gridLayout_agenda.addWidget(self.agenda_calendar_frame, 0, 0, 1, 1)
        self.agenda_frame = QtWidgets.QFrame(self.tab_agenda)
        self.agenda_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.agenda_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.agenda_frame.setObjectName("agenda_frame")
        self.gridLayout_agenda.addWidget(self.agenda_frame, 0, 1, 3, 1)
        self.agenda_goTodayPushButton = QtWidgets.QPushButton(self.tab_agenda)
        self.agenda_goTodayPushButton.setEnabled(False)
        self.agenda_goTodayPushButton.setMinimumSize(QtCore.QSize(220, 0))
        self.agenda_goTodayPushButton.setMaximumSize(QtCore.QSize(220, 24))
        self.agenda_goTodayPushButton.setIcon(icon)
        self.agenda_goTodayPushButton.setObjectName("agenda_goTodayPushButton")
        self.gridLayout_agenda.addWidget(self.agenda_goTodayPushButton, 1, 0, 1, 1)
        self.agenda_control_frame = QtWidgets.QFrame(self.tab_agenda)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agenda_control_frame.sizePolicy().hasHeightForWidth())
        self.agenda_control_frame.setSizePolicy(sizePolicy)
        self.agenda_control_frame.setMinimumSize(QtCore.QSize(220, 0))
        self.agenda_control_frame.setMaximumSize(QtCore.QSize(220, 16777215))
        self.agenda_control_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.agenda_control_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.agenda_control_frame.setLineWidth(0)
        self.agenda_control_frame.setObjectName("agenda_control_frame")
        self.gridLayout_agenda.addWidget(self.agenda_control_frame, 2, 0, 1, 1)
        self.diary_tabWidget.addTab(self.tab_agenda, "")
        self.horizontalLayout.addWidget(self.diary_tabWidget)

        self.retranslateUi(Form)
        self.diary_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.goTodayPushButton.setText(_("Go To Today"))
        self.daymemo_label.setText(_("TextLabel"))
        self.diary_tabWidget.setTabText(self.diary_tabWidget.indexOf(self.tab_dayview), _("Day View"))
        self.goto_current_week_PushButton.setText(_("View Current Week"))
        self.diary_tabWidget.setTabText(self.diary_tabWidget.indexOf(self.tab_weekview), _("Week View"))
        self.label_65.setText(_("Month"))
        self.printMonth_pushButton.setText(_("Print Month View"))
        self.monthClinicians_checkBox.setText(_("All Clinicians"))
        self.monthView_clinicians_pushButton.setText(_("Select Clinicians"))
        self.diary_tabWidget.setTabText(self.diary_tabWidget.indexOf(self.tab_monthview), _("Month View"))
        self.yearClinicians_checkBox.setText(_("All Clinicians"))
        self.yearView_clinicians_pushButton.setText(_("Select Clinicians"))
        self.label_64.setText(_("Year"))
        self.diary_tabWidget.setTabText(self.diary_tabWidget.indexOf(self.tab_yearview), _("Year View"))
        self.agenda_goTodayPushButton.setText(_("Go To Today"))
        self.diary_tabWidget.setTabText(self.diary_tabWidget.indexOf(self.tab_agenda), _("Agenda"))

from gettext import gettext as _
from PyQt5 import QtWebKitWidgets
from openmolar.qt4gui import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

