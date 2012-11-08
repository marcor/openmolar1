# -*- coding: utf-8 -*-
# Copyright (c) 2009 Neil Wallace. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. See the GNU General Public License
# for more details.

'''
provides one class - the appointment widget
the canvas is a subclass of this
'''

from __future__ import division
import pickle
from PyQt4 import QtGui, QtCore
from openmolar.settings import localsettings
from openmolar.qt4gui import colours
from openmolar.qt4gui.dialogs import blockslot

BGCOLOR = QtCore.Qt.transparent
FREECOLOR = colours.APPT_Background
LINECOLOR = colours.APPT_LINECOLOUR
APPTCOLORS = colours.APPTCOLORS
TRANSPARENT = colours.TRANSPARENT

class AppointmentWidget(QtGui.QFrame):
    '''
    a custom widget to for a dental appointment book
    useage is (startTime,finishTime, parentWidget - optional)
    startTime,finishTime in format HHMM or HMM or HH:MM or H:MM
    slotDuration is the minimum slot length - typically 5 minutes
    textDetail is the number of slots to draw before writing the time text
    parentWidget =optional
    '''
    selected_serialno = None
    def __init__(self, sTime, fTime, om_gui):
        QtGui.QFrame.__init__(self, om_gui)

        self.header_frame = QtGui.QFrame(self)
        self.om_gui = om_gui
        self.printButton = QtGui.QPushButton("", self.header_frame)
        self.printButton.setMaximumWidth(50)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ps.png"),
        QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.printButton.setIcon(icon)

        self.connect(self.printButton, QtCore.SIGNAL("clicked()"),
        self.printme)

        self.header_label = QtGui.QLabel("dent", self.header_frame)
        self.header_label.setAlignment(QtCore.Qt.AlignCenter)

        font = QtGui.QFont("Sans",14,75)
        self.header_label.setFont(font)

        self.memo_lineEdit = QtGui.QLineEdit(self)
        self.memo_lineEdit.setText("hello")
        self.memo_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.memo_lineEdit.setMaxLength(30) # due to schema restrictions :(

        font = QtGui.QFont("Sans",12,75,True)
        self.memo_lineEdit.setFont(font)
        #self.memo_lineEdit.setStyleSheet("background:white")

        self.dentist = "DENTIST"
        self.apptix = 0
        glay = QtGui.QGridLayout(self.header_frame)
        glay.setSpacing(2)
        glay.setMargin(2)
        glay.addWidget(self.printButton,0,1)
        glay.addWidget(self.header_label,0,0)
        glay.addWidget(self.memo_lineEdit,1,0,1,2)

        self.scrollArea = QtGui.QScrollArea()
        self.scrollArea.setWidgetResizable(True)

        self.canvas = appointmentCanvas(om_gui, self)
        self.scrollArea.setWidget(self.canvas)

        self.setDayStartTime(sTime)
        self.setStartTime(sTime)
        self.setDayEndTime(fTime)
        self.setEndTime(fTime)

        self.OOlabel = QtGui.QLabel(_("Out Of Office"))
        self.OOlabel.setWordWrap(True)
        self.OOlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.OOlabel.setSizePolicy(QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding))

        lay = QtGui.QVBoxLayout(self)
        lay.setSpacing(0)
        lay.setMargin(2)
        lay.addWidget(self.header_frame)
        lay.addWidget(self.OOlabel)
        lay.addWidget(self.scrollArea)

        self.outofoffice = False
        self.setOutOfOffice(False)

        self.setMinimumSize(self.minimumSizeHint())
        self.setMaximumSize(self.maximumSizeHint())
        self.signals()

    def setOutOfOffice(self, val):
        '''
        toggle out of office
        '''
        self.outofoffice = val
        self.OOlabel.setVisible(val)
        self.scrollArea.setVisible(not val)

    def setDentist(self, apptix):
        '''
        update the dentist the widget relates to
        '''
        self.apptix = apptix
        self.dentist = localsettings.apptix_reverse.get(apptix, "??")

    def sizeHint(self):
        '''
        set an (arbitrary) size for the widget
        '''
        return QtCore.QSize(400, 700)

    def minimumSizeHint(self):
        '''
        set an (arbitrary) minimum size for the widget
        '''
        return QtCore.QSize(120, 300)

    def maximumSizeHint(self):
        '''
        widget looks daft if too wide
        '''
        return QtCore.QSize(500, 16777215)

    def setDayStartTime(self, sTime):
        '''
        a public method to set the Practice Day Start
        '''
        self.canvas.setDayStartTime(sTime)

    def setDayEndTime(self, fTime):
        '''
        a public method to set the Practice Day End
        '''
        self.canvas.setDayEndTime(fTime)

    def setStartTime(self, sTime):
        '''
        a public method to set the earliest appointment available
        '''
        self.canvas.setStartTime(sTime)

    def setEndTime(self, fTime):
        '''
        a public method to set the end of the working day
        '''
        self.canvas.setEndTime(fTime)

    def setCurrentTime(self, t):
        '''
        send it a value like "HHMM" or "HH:MM" to draw a marker at that time
        '''
        return self.canvas.setCurrentTime(t)

    def clearAppts(self):
        '''
        resets - the widget values - DOES NOT REDRAW THE WIDGET
        '''
        self.canvas.appts = []
        self.canvas.doubleAppts = []
        self.canvas.rows = {}

    def printme(self):
        '''
        emits a signal when the print button is clicked
        '''
        self.emit(QtCore.SIGNAL("print_me"), self.apptix,
        self.om_gui.ui.dayCalendar.selectedDate())

    def newMemo(self):
        '''
        user has edited the memo line Edit - emit a signal so the
        gui can handle it
        '''
        if not self.memo_lineEdit.hasFocus():
            self.emit(QtCore.SIGNAL("new_memo"),
            (self.dentist, str(self.memo_lineEdit.text().toAscii())))

    def signals(self):
        '''
        set up the widget's signals and slots
        '''
        self.connect(self.memo_lineEdit,
        QtCore.SIGNAL("editingFinished()"), self.newMemo)

    def showEvent(self, event=None):
        if self.om_gui.pt:
            self.selected_serialno = self.om_gui.pt.serialno
        else:
            self.selected_serialno = None

    def update(self):
        if not self.outofoffice:
            self.canvas.update()

    def setAppointment(self, app):
        '''
        adds an appointment to the widget dictionary of appointments
        typical useage is instance.setAppointment
        ("0820","0900","NAME","serialno","trt1",
        "trt2","trt3","Memo", modtime)
        NOTE - this also appts to the widgets
        dictionary which has
        row number as key, used for signals when appts are clicked

        (5, 915, 930, 'MCPHERSON I', 6155L, 'EXAM', '', '', '', 1, 73, 0, 0,
        timestamp)
        (5, 1100, 1130, 'EMERGENCY', 0L, '', '', '', '', -128, 0, 0, 0,
        timestamp)
        '''
        (start, finish, name, sno, trt1, trt2, trt3, memo, flag, cset,
        modtime) = (str(app[1]), str(app[2]), app[3], app[4],
        app[5], app[6], app[7], app[8], app[9], chr(app[10]), app[13])

        startcell = self.canvas.getCell_from_time(start)
        endcell = self.canvas.getCell_from_time(finish)
        if endcell == startcell: #double and family appointments!!
            endcell += 1

            self.canvas.doubleAppts.append((startcell, endcell, start, finish,
            name, sno, trt1, trt2, trt3, memo, flag, cset, modtime))
        else:
            self.canvas.appts.append((startcell, endcell, start, finish,
            name, sno, trt1, trt2, trt3, memo, flag, cset, modtime))
        if sno == 0:
            sno = self.canvas.duplicateNo
            self.canvas.duplicateNo -= 1
        for row in range(startcell, endcell):
            if self.canvas.rows.has_key(row):
                self.canvas.rows[row].append(sno)
            else:
                self.canvas.rows[row] = [sno]

class appointmentCanvas(QtGui.QWidget):
    '''
    the canvas for me to draw on
    '''
    def __init__(self, om_gui, pWidget):
        super(appointmentCanvas, self).__init__()
        self.setSizePolicy(QtGui.QSizePolicy(
        QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding))

        self.setMinimumSize(self.minimumSizeHint())
        self.pWidget = pWidget
        self.slotDuration = 5 # 5 minute slots
        self.textDetail = 3   # time printed every 3 slots
        self.slotNo = 12
        self.dayEndTime=60
        self.dayStartTime=0
        self.startTime=0
        self.endTime=60
        self.appts = []
        self.doubleAppts = []
        self.rows = {}
        self.setTime = None
        self.selected = (0,0)
        self.setMouseTracking(True)
        self.duplicateNo = -1 #use this for serialnos =0
        self.om_gui = om_gui
        self.dragging = False
        self.drag_appt = None
        self.drop_time = None
        self.setAcceptDrops(True)
        self.qmenu = None

    def setDayStartTime(self, sTime):
        '''
        a public method to set the Practice Day Start
        '''
        self.dayStartTime = self.minutesPastMidnight(sTime)

    def setDayEndTime(self, fTime):
        '''
        a public method to set the Practice Day End
        '''
        self.dayEndTime = self.minutesPastMidnight(fTime)
        self.calcSlotNo()

    def setStartTime(self, sTime):
        '''
        a public method to set the earliest appointment available
        '''
        self.startTime = self.minutesPastMidnight(sTime)
        self.firstSlot = self.getCell_from_time(sTime)+1

    def setEndTime(self, fTime):
        '''
        a public method to set the end of the working day
        '''
        self.endTime = self.minutesPastMidnight(fTime)
        self.lastSlot = self.getCell_from_time(fTime)

    def calcSlotNo(self):
        '''
        work out how many 'slots' there are given the lenght of day
        and length of slots
        '''
        self.slotNo = (
        self.dayEndTime - self.dayStartTime) // self.slotDuration

    def minutesPastMidnight(self, t):
        '''
        converts a time in the format of
        'HHMM' or 'H:MM' (both strings) to minutes
        past midnight
        '''
        hour, minute = int(t) // 100, int(t) % 100
        return hour * 60 + minute

    def humanTime(self, t):
        '''
        converts minutes past midnight(int) to format "HH:MM"
        '''
        hour, minute = t // 60, int(t) % 60
        return "%s:%02d"% (hour, minute)

    def setslotDuration(self, arg):
        '''
        set the slotDuration (default is 5 minutes)
        '''
        self.slotDuration = arg

    def setTextDetail(self, arg):
        '''
        set the number of rows between text time slots
        '''
        self.textDetail = arg

    def sizeHint(self):
        '''
        set an (arbitrary) size for the widget
        '''
        return QtCore.QSize(800, 800)

    def minimumSizeHint(self):
        '''
        set an (arbitrary) minimum size for the widget
        '''
        return QtCore.QSize(100, 200)

    def setCurrentTime(self, t):
        '''
        send it a value like "HHMM" or "HH:MM" to draw a marker at that time
        '''
        self.setTime = t
        if t and self.startTime < self.minutesPastMidnight(t) < self.endTime:
            return True

    def qTime(self, t):
        '''
        converts minutes past midnight(int) to a QTime
        '''
        hour, minute = t // 60, int(t) % 60
        return QtCore.QTime(hour, minute)

    def getCell_from_time(self, t):
        '''
        send a time - return the row number of that time
        '''
        return int((self.minutesPastMidnight(t) - self.dayStartTime)
            / self.slotDuration)

    def getTime_from_Cell(self, row):
        '''
        you know the row.. what time is that
        '''
        mpm = self.slotDuration * row + self.dayStartTime
        return localsettings.minutesPastMidnightToPyTime(mpm)

    def getPrev(self, arg):
        '''
        what slot is the previous appt?
        '''
        lower = arg
        while lower >= self.firstSlot:
            if self.rows.has_key(lower):
                lower += 1
                break
            lower -= 1
        return lower

    def getNext(self, arg):
        '''
        what slot is the next appt?
        '''
        upper = arg
        while upper < self.lastSlot:
            if self.rows.has_key(upper):
                break
            upper += 1
        return upper

    def getApptBounds(self, arg):
        '''
        get the start and finish of an appt
        '''
        upper = 0
        lower = self.slotNo
        sortedkeys = self.rows.keys()
        sortedkeys.sort()
        for key in sortedkeys:
            if self.rows[key]==arg:
                if key<lower:
                    lower=key
                if key>=upper:
                    upper=key
        return (lower,upper+1)

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("application/x-appointment"):
            data = event.mimeData()
            bstream = data.retrieveData("application/x-appointment",
            QtCore.QVariant.ByteArray)
            self.drag_appt = pickle.loads(bstream.toByteArray())

            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasFormat("application/x-appointment"):

            y = event.pos().y()
            yOffset = self.height() / self.slotNo
            self.drag_startrow = int(y//yOffset)

            if (self.drag_startrow < self.firstSlot-1 or
            self.drag_startrow >= self.lastSlot or
            self.rows.has_key(self.drag_startrow)):
                allowDrop = False
            else:
                n_rows = self.drag_appt.length // self.slotDuration
                self.drag_endrow = self.drag_startrow + n_rows
                #see if there's a long enough slot either side of the selected
                #row
                allowDrop = True
                for row in range(self.drag_startrow, self.drag_endrow):
                    if self.rows.has_key(row) or row >= self.lastSlot:
                        allowDrop = False
                        break
                if not allowDrop:
                    allowDrop = True
                    self.drag_startrow = row - n_rows
                    self.drag_endrow = row
                    for row in range(self.drag_startrow, row):
                        if self.rows.has_key(row) or row < self.firstSlot-1:
                            allowDrop = False
                            break

            if allowDrop:
                self.dragging = True
                self.drop_time = self.getTime_from_Cell(self.drag_startrow)
                self.update()
                event.accept()
            else:
                self.dragging = False
                self.update()
                event.ignore()
        else:
            self.update()
            event.accept()

    def dragLeaveEvent(self, event):
        self.dragging = False
        self.update()
        event.accept()

    def dropEvent(self, event):
        self.dragging = False
        self.emit(QtCore.SIGNAL("ApptDropped"), self.drag_appt,
            self.drop_time, self.pWidget.apptix)
        self.drag_appt = None
        self.dropOffset = 0
        event.accept()

    def mouseMoveEvent(self, event):
        y = event.y()
        yOffset = self.height() / self.slotNo
        row = int(y//yOffset)
        if not (self.firstSlot-1) < row < self.lastSlot:
            self.selected = (0, 0)
            self.update()
            QtGui.QToolTip.showText(event.globalPos(), "")
            return

        if self.rows.has_key(row):
            selectedPatients = self.rows[row]
            self.selected = self.getApptBounds(selectedPatients)
            self.update()
            feedback = "<html>"
            for patient in selectedPatients:
                for appt in self.appts + self.doubleAppts:
                    if appt[5] == patient:
                        feedback += '''%s<br /><b>%s - %s</b>'''%(
                            appt[4], appt[2], appt[3])
                        for val in (appt[6], appt[7], appt[8]):
                            if val != "":
                                feedback += '''
                                <br /><font color="red">%s</font>'''% val
                        if appt[9] != "":
                            feedback += "<br /><i>%s</i>"% appt[9]
                        try:
                            timestamp = appt[12]
                            datestamp = timestamp.date()
                            moddate = localsettings.readableDate(datestamp)
                            if datestamp == localsettings.currentDay():
                                feedback += "<br /><i>%s %s %s %s</i><hr />"% (
                                _("Made"), moddate, _("at"),
                                localsettings.pyTimeToHumantime(timestamp))
                            else:
                                feedback += "<br /><i>%s<br />%s</i><hr />"% (
                                _("Made on"), moddate)

                        except AttributeError:
                            feedback +="<hr />"
                            pass

            if feedback != "<html>":
                feedback = feedback[:feedback.rindex("<hr />")] + "</html>"
                x_pos = self.mapToGlobal(self.pos()).x()
                pos = QtCore.QPoint(x_pos, event.globalPos().y())
                QtGui.QToolTip.showText(pos, feedback)
            else:
                QtGui.QToolTip.showText(event.globalPos(), "")
        else:
            newSelection = (self.getPrev(row), self.getNext(row))
            if self.selected != newSelection:
                self.selected = newSelection
                self.update()

                start = int(self.dayStartTime + self.selected[0] * self.slotDuration)
                finish = int(self.dayStartTime + self.selected[1] * self.slotDuration)

                x_pos = self.mapToGlobal(self.pos()).x()
                pos = QtCore.QPoint(x_pos, event.globalPos().y())
                QtGui.QToolTip.showText(pos,
                    "SLOT %s minutes"% (finish - start))

    def mouseDoubleClickEvent(self,event):
        self.mousePressEvent(event)

    def mousePressEvent(self, event):
        '''
        catch the mouse press event -
        and if you have clicked on an appointment, emit a signal
        the signal has a LIST as argument -
        in case there are overlapping appointments or doubles etc...
        '''
        def rightClickMenuResult(result):
            if not result:
                return
            dent = localsettings.apptix.get(self.pWidget.dentist)
            if result.text() == _("Load Patient"):
                self.pWidget.emit(QtCore.SIGNAL("AppointmentClicked"),
                    tuple(selectedPatients))
            elif result.text() == _("Add/Edit Memo"):
                self.pWidget.emit(QtCore.SIGNAL("EditAppointmentMemo"),
                    tuple(selectedPatients), start, dent)
            elif result.text() == _("Cancel Appointment"):
                self.pWidget.emit(QtCore.SIGNAL("AppointmentCancel"),
                    tuple(selectedPatients), start, dent)

            elif result.text() == _("Clear Block"):
                self.pWidget.emit(QtCore.SIGNAL("ClearEmergencySlot"),
                (start, finish, dent))

            elif result.text() == _("Block or use this space"):
                self.block_use_space(qstart, qfinish)

        yOffset = self.height() / self.slotNo
        row=event.y()//yOffset

        actions = []

        if self.rows.has_key(row):
            start=self.humanTime(
            int(self.dayStartTime+self.selected[0]*self.slotDuration))

            finish=self.humanTime(
            int(self.dayStartTime+self.selected[1]*self.slotDuration))

            selectedPatients=self.rows[row]
            #ignore lunch and emergencies - serialno number is positive

            if selectedPatients[0]>0:
                actions.append(_("Load Patient"))
                actions.append(None)
                actions.append(_("Add/Edit Memo"))
                actions.append(_("Cancel Appointment"))

                self.pWidget.emit(QtCore.SIGNAL("PatientClicked"),
                    tuple(selectedPatients))
            else:
                actions.append(_("Clear Block"))

        else:
            #-- no-one in the book...
            qstart=self.qTime(
            int(self.dayStartTime+self.selected[0]*self.slotDuration))

            qfinish=self.qTime(
            int(self.dayStartTime+self.selected[1]*self.slotDuration))

            if (self.firstSlot-1) < row < self.lastSlot:
                actions.append(_("Block or use this space"))

        if self.qmenu and event.type() == QtCore.QEvent.MouseButtonDblClick:
            rightClickMenuResult(self.qmenu.defaultAction())
            self.qmenu.clear()
            return

        self.qmenu = QtGui.QMenu(self)
        for i, action in enumerate(actions):
            if action is None:
                self.qmenu.addSeparator()
                continue
            q_act = self.qmenu.addAction(action)
            if i == 0:
                self.qmenu.setDefaultAction(q_act)
        if event.button() == QtCore.Qt.RightButton:
            rightClickMenuResult(self.qmenu.exec_(event.globalPos()))

    def block_use_space(self, start, finish):
        Dialog=QtGui.QDialog(self)
        dl = blockslot.blockDialog(Dialog, self.om_gui)

        dl.setTimes(start, finish)
        dl.setPatient(self.om_gui.pt)

        if dl.exec_():
            adjstart = dl.start_timeEdit.time()
            adjfinish = dl.finish_timeEdit.time()
            if finish < start :
                QtGui.QMessageBox.information(self,
                _("Whoops!"), _("Bad Time Sequence!"))

            if dl.block == True:
                reason = str(
                dl.comboBox.currentText().toAscii())[:30]

                self.pWidget.emit(QtCore.SIGNAL("BlockEmptySlot"),
                (start, finish, adjstart, adjfinish ,
                localsettings.apptix.get(self.pWidget.dentist),
                reason))
            else:
                reason = dl.reason_comboBox.currentText().toAscii()
                self.pWidget.emit(
                QtCore.SIGNAL("Appointment_into_EmptySlot"),
                (start, finish, adjstart, adjfinish ,
                localsettings.apptix.get(self.pWidget.dentist),
                reason, dl.patient))

    def leaveEvent(self,event):
        self.mouse_down = False
        self.selected=[-1,-1]
        self.update()

    def paintEvent(self, event=None):
        '''
        draws the book - recalled at any point by instance.update()
        '''
        red_pen = QtGui.QPen(QtCore.Qt.red, 2)
        blue_pen = QtGui.QPen(QtCore.Qt.blue, 2)

        painter = QtGui.QPainter(self)
        currentSlot = 0
        myfont = QtGui.QFont(self.fontInfo().family(),
        localsettings.appointmentFontSize)

        fm = QtGui.QFontMetrics(myfont)
        timeWidth = fm.width(" 88:88 ")
        painter.setFont(myfont)
        slotHeight = fm.height()/self.textDetail

        if self.parent() and (slotHeight *
        self.slotNo < self.parent().height()):
            self.setMinimumHeight(self.parent().height())
            slotHeight = self.height() / self.slotNo
        else:
            self.setMinimumHeight(slotHeight * self.slotNo)

        #define and draw the white boundary

        painter.setBrush(colours.APPT_Background)
        painter.setPen(QtGui.QPen(colours.APPT_Background,1))

        top = (self.firstSlot-1) * slotHeight
        bottom = (self.lastSlot + 1 - self.firstSlot) * slotHeight

        colwidth = self.width()-timeWidth
        dragScale = slotHeight / self.slotDuration
        rect = QtCore.QRectF(timeWidth, top, colwidth, bottom)

        painter.drawRect(rect)

        # DRAW HORIZONTAL LINES AND TIMES

        while currentSlot < self.slotNo:

            textneeded = False
            if currentSlot%self.textDetail == 0:
                textneeded=True

            y = currentSlot*slotHeight

            #- code to check if within the appointment hours
            if self.firstSlot <= currentSlot <= self.lastSlot:
                painter.setPen(QtGui.QPen(LINECOLOR, 1))
                painter.drawLine(timeWidth+1, y, self.width()-1, y)
            if textneeded:
                trect=QtCore.QRectF(0, y,
                timeWidth,y + self.textDetail * slotHeight)

                painter.setPen(QtGui.QPen(QtCore.Qt.black,1))
                painter.drawLine(0, y, timeWidth, y)

                painter.drawText(trect,QtCore.Qt.AlignLeft,
                (QtCore.QString(self.humanTime(
                self.dayStartTime+(currentSlot*self.slotDuration)))))

            currentSlot += 1

        #####layout appts
        painter.save()
        painter.setPen(QtCore.Qt.black)
        option = QtGui.QTextOption(QtCore.Qt.AlignCenter)
        option.setWrapMode(QtGui.QTextOption.WordWrap)

        for appt in self.appts:
            (startcell, endcell, start, fin, name, sno, trt1, trt2,
            trt3, memo, flag, cset, modtime) = appt

            rect = QtCore.QRectF(timeWidth,startcell*slotHeight,
            self.width()-timeWidth, (endcell-startcell)*slotHeight)

            if sno !=0 and sno == self.pWidget.selected_serialno:
                painter.setBrush(QtGui.QColor("orange"))
            elif self.selected == (startcell, endcell):
                painter.setBrush(QtGui.QColor("#AAAAAA"))
            elif APPTCOLORS.has_key(cset):
                painter.setBrush(APPTCOLORS[cset])
            elif APPTCOLORS.has_key(name.upper()):
                painter.setBrush(APPTCOLORS[name.upper()])
            elif flag==-128:
                painter.setBrush(APPTCOLORS["BUSY"])
            else:
                painter.setBrush(APPTCOLORS["default"])

            if not (sno == 0 and (
            endcell < self.firstSlot or startcell > self.lastSlot)):
                painter.drawRect(rect)
                mytext = "%s %s %s %s %s"% (name.title(), trt1,
                trt2, trt3 ,memo)

                painter.drawText(rect, mytext, option)

            ##highlight any appointments booked today
            if (sno !=0 and
            modtime and modtime.date() == localsettings.currentDay()):
                rect = QtCore.QRectF(self.width()-timeWidth/2,
                startcell*slotHeight, timeWidth/2,rect.height()).adjusted(
                2,2,-2,-2)

                painter.save()
                painter.setPen(colours.BOOKED_TODAY)
                painter.setBrush(colours.BOOKED_TODAY)
                painter.drawEllipse(rect)
                painter.restore()

        for appt in self.doubleAppts:
            (startcell,endcell,start,fin,name,sno, trt1,trt2,
            trt3,memo,flag,cset, modtime)=appt

            rect=QtCore.QRectF(self.width()-timeWidth,startcell*slotHeight,
            self.width()-timeWidth,slotHeight)

            painter.setBrush(APPTCOLORS["DOUBLE"])
            painter.drawRect(rect)

        painter.restore()

        ##highlight current time
        if self.setTime:
            cellno = self.getCell_from_time(self.setTime)
            painter.setPen(blue_pen)
            painter.setBrush(QtCore.Qt.blue)
            corner1 = [timeWidth*1.4, cellno*slotHeight]
            corner2 = [timeWidth, (cellno-0.5)*slotHeight]
            corner3 = [timeWidth, (cellno+0.5)*slotHeight]
            triangle = corner1+corner2+corner3
            painter.drawPolygon(QtGui.QPolygon(triangle))
            corner1 = [self.width()-timeWidth*0.4, cellno*slotHeight]
            corner2 = [self.width(), (cellno-0.5)*slotHeight]
            corner3 = [self.width(), (cellno+0.5)*slotHeight]
            triangle = corner1+corner2+corner3
            painter.drawPolygon(QtGui.QPolygon(triangle))

        if self.dragging:
            painter.setPen(red_pen)
            y = self.drag_startrow *slotHeight
            y2 = self.drag_endrow * slotHeight
            painter.drawLine(0, y, self.width(), y)
            painter.setBrush(QtGui.QColor("yellow"))


            trect = QtCore.QRectF(timeWidth, y, self.width()-timeWidth, y2-y)
            painter.drawRect(trect)

            droptime = self.drop_time.strftime("%H:%M")
            trect = QtCore.QRectF(0, y, timeWidth, y2-y)
            painter.drawRect(trect)
            painter.drawText(trect, QtCore.Qt.AlignHCenter, droptime)

if __name__ == "__main__":
    import datetime
    class patient():
        '''
        a duck type for my real patient class
        '''
        def __init__(self):
            self.serialno = 4
            self.title = "mr"
            self.sname = "john"
            self.fname = "doe"

    def clicktest(*args):
        print "clicktest", args

    import sys
    localsettings.initiate()
    app = QtGui.QApplication(sys.argv)

    #--initiate a book starttime 08:00 endtime 10:00
    #--five minute slots, text every 3 slots

    #from openmolar.qt4gui import maingui
    #parent = maingui.OpenmolarGui()
    parent = QtGui.QFrame()
    parent.pt = patient()

    form = AppointmentWidget("0800","1500", parent)
    form.setStartTime("0830")
    form.setEndTime("1430")

    print'''
    created a calendar with start %d minutes past midnight
                1st appointment %d minutes past midnight
            appointments finish %d minutes past midnight
                        day end %d minutes past midnight
    - %d %d minutes slots'''%(
    form.canvas.dayStartTime,
    form.canvas.startTime,
    form.canvas.endTime,
    form.canvas.dayEndTime,
    form.canvas.slotNo,
    form.canvas.slotDuration)

    form.setCurrentTime("945")
    form.clearAppts()

    dt = datetime.datetime.now()
    for appoint in (
    (5, 915, 930, 'MCDONALD I', 6155, 'EXAM', '', '', '', 1, 73, 0, 0, dt )
    ,(5, 1100, 1130, 'EMERGENCY', 0, '', '', '', '', -128, 0, 0, 0, dt),
    (5, 1300, 1400, 'LUNCH', 0, '', '', '', '', -128, 0, 0, 0, dt),
    (5, 1400, 1410, 'STAFF MEETING', 0, '', '', '', '', -128, 0, 0, 0, dt),
    (5, 930, 1005, 'TAYLOR JANE', 19373, 'FILL', '', '', '', 1, 80, 0, 0, dt),
    ):
        form.setAppointment(appoint)

    form.connect(form, QtCore.SIGNAL("AppointmentClicked"), clicktest)
    form.connect(form, QtCore.SIGNAL("ClearEmergencySlot"), clicktest)
    form.connect(form, QtCore.SIGNAL("BlockEmptySlot"), clicktest)
    form.connect(form, QtCore.SIGNAL("print_me"), clicktest)
    form.connect(form,
        QtCore.SIGNAL("Appointment_into_EmptySlot"), clicktest)

    v = QtGui.QVBoxLayout()
    v.setSpacing(0)
    v.addWidget(form)
    parent.setLayout(v)
    parent.show()

    sys.exit(app.exec_())
