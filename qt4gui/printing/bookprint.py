# -*- coding: utf-8 -*-
# Copyright (c) 2009 Neil Wallace. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or 
# (at your option) any later version. See the GNU General Public License for more details.

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
#import qrc_resources

DATE_FORMAT="dd mm yyyy"

class printBook():
    '''initiates with an image (chart) as the argument'''
    def __init__(self,html):
        self.html=html
        self.printer = QPrinter()
        self.printer.setPageSize(QPrinter.A4)
    def printpage(self,askfirst=True):
        dialog = QPrintDialog(self.printer)
        if askfirst and not dialog.exec_():
            return
        #print dir(self.printer)
        document = QTextDocument()
        document.setHtml(self.html)
        document.print_(self.printer)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = printBook("<html><body><h1>This is a Test</h1><p>I trust it worked?</p></body></html>")
    form.printpage(True)  #show a dialog for testing purposes
    app.exec_()

