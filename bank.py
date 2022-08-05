
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtWidgets import *
import json

class system(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.nameSend = ""
        self.cardSend = ""
        self.username = ""
        self.login()

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.btnExit.clicked.connect(self.close)
        self.btnMaximize.clicked.connect(self.showMaximized)
        self.btnMinimize.clicked.connect(self.showMinimized)

        self.show()

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.setGeometry(self.mapToGlobal(self.movement).x(),
                                self.mapToGlobal(self.movement).y(),
                                self.width(),
                                self.height())
            self.start = self.end
    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False
    
    def login(self):
        uic.loadUi("login.ui", self)
        self.btnLogin.clicked.connect(self.changeLog)

    def adminPage(self):
        uic.loadUi('system.ui', self)

        self.btnExit.clicked.connect(self.close)
        self.btnMaximize.clicked.connect(self.showMaximized)
        self.btnMinimize.clicked.connect(self.showMinimized)

        self.stack.addWidget(self.frmBlank)
        self.stack.addWidget(self.frmSystem)
        self.stack.addWidget(self.frmProfile)
        self.stack.addWidget(self.frmUser)
        self.stack.setCurrentIndex(0)

        self.btnSystem.clicked.connect(self.mainClick1)
        self.btnProfile.clicked.connect(self.mainClick2)
        self.btnEmployees.clicked.connect(self.mainClick3)
        self.btnUsers.clicked.connect(self.mainClick4)
        self.btnProAddcard.clicked.connect(self.Addcard)
        self.btnProReload.clicked.connect(self.proReload)
        self.btnEnterName.clicked.connect(self.search)
        self.btnEnterReload.clicked.connect(self.userReload)
        self.btnEnterAddcard.clicked.connect(self.Addcard)
        self.btnEnterRemcard.clicked.connect(self.removeCard)
        self.btnProRemcard.clicked.connect(self.removeCard)
        self.linProSendcard.textChanged.connect(self.anchanged)
        self.btnProSend.clicked.connect(self.send)
        self.btnLogout.clicked.connect(self.login)
        self.btnMore.clicked.connect(self.moreDialog)
        self.btnSysPower.clicked.connect(self.sysPower)
        self.btnSysSearch.clicked.connect(self.somSearch)

        self.linProName.setText(self.data()[self.username]["name"])
        self.linProConcode.setText(self.data()[self.username]["countryCode"])
        for i in self.data()[self.username]["cards"]:
            self.cmbProCards.addItem(i)
        for i in self.data()[self.username]["history"]:
            rows = self.tblProfile.rowCount()
            self.tblProfile.insertRow(rows)
            for d in i:
                columns = i.index(d)
                value = QTableWidgetItem(str(d))
                self.tblProfile.setItem(rows, columns, value)
    
    def employeePage(self):
        uic.loadUi("system.ui", self)

        self.btnExit.clicked.connect(self.close)
        self.btnMaximize.clicked.connect(self.showMaximized)
        self.btnMinimize.clicked.connect(self.showMinimized)

        self.stack.addWidget(self.frmBlank)
        self.stack.addWidget(self.frmSystem)
        self.stack.addWidget(self.frmProfile)
        self.stack.addWidget(self.frmUser)
        self.stack.setCurrentIndex(0)

        self.btnSystem.clicked.connect(self.mainClick1)
        self.btnProfile.clicked.connect(self.mainClick2)
        self.btnEmployees.clicked.connect(self.mainClick3)
        self.btnUsers.clicked.connect(self.mainClick4)
        self.btnProAddcard.clicked.connect(self.Addcard)
        self.btnProReload.clicked.connect(self.proReload)
        self.btnEnterName.clicked.connect(self.search)
        self.btnEnterReload.clicked.connect(self.userReload)
        self.btnEnterAddcard.clicked.connect(self.Addcard)
        self.btnEnterRemcard.clicked.connect(self.removeCard)
        self.btnProRemcard.clicked.connect(self.removeCard)
        self.linProSendcard.textChanged.connect(self.anchanged)
        self.btnProSend.clicked.connect(self.send)
        self.btnLogout.clicked.connect(self.login)
        self.btnMore.clicked.connect(self.moreDialog)

        self.linProName.setText(self.data()[self.username]["name"])
        self.linProConcode.setText(self.data()[self.username]["countryCode"])
        for i in self.data()[self.username]["cards"]:
            self.cmbProCards.addItem(i)
        for i in self.data()[self.username]["history"]:
            rows = self.tblProfile.rowCount()
            self.tblProfile.insertRow(rows)
            for d in i:
                columns = i.index(d)
                value = QTableWidgetItem(str(d))
                self.tblProfile.setItem(rows, columns, value)

    def userPage(self):
        
        uic.loadUi("system.ui", self)

        self.btnExit.clicked.connect(self.close)
        self.btnMaximize.clicked.connect(self.showMaximized)
        self.btnMinimize.clicked.connect(self.showMinimized)

        self.stack.addWidget(self.frmBlank)
        self.stack.addWidget(self.frmSystem)
        self.stack.addWidget(self.frmProfile)
        self.stack.addWidget(self.frmUser)
        self.stack.setCurrentIndex(0)

        self.btnSystem.clicked.connect(self.mainClick1)
        self.btnProfile.clicked.connect(self.mainClick2)
        self.btnEmployees.clicked.connect(self.mainClick3)
        self.btnUsers.clicked.connect(self.mainClick4)
        self.linProSendcard.textChanged.connect(self.anchanged)
        self.btnProSend.clicked.connect(self.send)
        self.btnLogout.clicked.connect(self.login)

        self.linProName.setText(self.data()[self.username]["name"])
        self.linProConcode.setText(self.data()[self.username]["countryCode"])
        for i in self.data()[self.username]["cards"]:
            self.cmbProCards.addItem(i)
        for i in self.data()[self.username]["history"]:
            rows = self.tblProfile.rowCount()
            self.tblProfile.insertRow(rows)
            for d in i:
                columns = i.index(d)
                value = QTableWidgetItem(str(d))
                self.tblProfile.setItem(rows, columns, value)
    def somSearch(self):

        print("Comingsoon... (75%)")
        data = self.data()
        for i in data:
            if "countryCode" in data[i]:
                if self.linSysConcode.text() == data[i]["countryCode"]:
                    
                    clsrowcount = self.tblSystem.rowCount()
                    while clsrowcount >= 0:
                        self.tblSystem.removeRow(clsrowcount)
                        clsrowcount -= 1
                    for x in data[i]["history"]:
                        rows = self.tblSystem.rowCount()
                        self.tblSystem.insertRow(rows)
                        for d in x:
                            columns = x.index(d)
                            value = QTableWidgetItem(str(d))
                            self.tblSystem.setItem(rows, columns, value)
        # self.linSysAtdate.text()
        # self.linSysTodate.text()

    def sysPower(self):
        
        if self.btnSysPower.isChecked() == False:
            self.btnSysPower.setChecked(False)
            self.btnProSend.setEnabled(False)
            self.btnProAddcard.setEnabled(False)
            self.btnProRemcard.setEnabled(False)
            self.btnEnterAddcard.setEnabled(False)
            self.btnEnterRemcard.setEnabled(False)
            self.btnMore.setEnabled(False)
        else:
            self.btnSysPower.setChecked(True)
            self.btnProSend.setEnabled(True)
            self.btnProAddcard.setEnabled(True)
            self.btnProRemcard.setEnabled(True)
            self.btnEnterAddcard.setEnabled(True)
            self.btnEnterRemcard.setEnabled(True)
            self.btnMore.setEnabled(True)

    def send(self):
        index = self.cmbProCards.currentIndex()
        if index != 0:
            data = self.data()
            price = self.linProSendprice.text()
            for i in data:
                if "cards" in data[i]:
                    if self.linProSendname.text() == data[i]["name"]:
                        p = data[i]["balanceCredit"]
                        n = int(p) + int(price)

                        data[i]["balanceCredit"] = str(n)
                        p = int(p) - int(price)
                        data[self.username]["balanceCredit"] = str(p)

                        rows = self.tblProfile.rowCount()
                        self.tblProfile.insertRow(rows)
                        tbl = ["date", "time", "move - " + price, self.cmbProCards.currentText(), self.cardSend]
                        for d in tbl:
                            columns = tbl.index(d)
                            value = QTableWidgetItem(str(d))
                            self.tblProfile.setItem(rows, columns, value)
                        data[self.username]["history"].append(tbl)
                        data[i]["history"].append(tbl)
                        json.dump(data, open("user.json", "w"), indent= 4)
        else:
            messageBox = QMessageBox.warning(
            self,
            "Error!",
            "Please Select your number of account!",
            QMessageBox.Ok
            )
        
            if messageBox == QMessageBox.Ok:
                pass



    def anchanged(self, text):
        data = self.data()
        for i in data:
            if "cards" in data[i]:
                if text in data[i]["cards"]:
                    self.linProSendname.setText(data[i]["name"])
                    self.nameSend = data[i]["name"]
                    self.cardSend = text

    def removeCard(self):
        data = self.data()
        if self.btnProfile.isChecked():
            if self.data()[self.username]["type"] == "admin":
                index = self.cmbProCards.currentIndex()
                self.cmbProCards.removeItem(index)
                index = data[self.username]["cards"][index - 1]
                data[self.username]["cards"].remove(index)
                data["cards"].remove(index)
                json.dump(data, open("user.json", "w"), indent= 4)
            else:
                messageBox = QMessageBox.warning(self, "Error!", "type of your account is not a admin", QMessageBox.Ok)
                if messageBox == QMessageBox.Ok:
                    pass
        else:
            for i in data:
                if "name" in data[i]:
                    if self.linEnterName.text() == data[i]["name"]:
                        if data[i]["type"] == "employee":
                            if self.data()[self.username]["type"] == "admin":
                                index = self.cmbEnterCards.currentIndex()
                                self.cmbEnterCards.removeItem(index)
                                index = data[i]["cards"][index - 1]
                                data[i]["cards"].remove(index)
                                data["cards"].remove(index)
                                json.dump(data, open("user.json", "w"), indent= 4)
                            else:
                                messageBox = QMessageBox.warning(self, "Error!", "type of your account is not a admin", QMessageBox.Ok)
                                if messageBox == QMessageBox.Ok:
                                    pass
                        if data[i]["type"] == "user":
                            index = self.cmbEnterCards.currentIndex()
                            self.cmbEnterCards.removeItem(index)
                            index = data[i]["cards"][index - 1]
                            data[i]["cards"].remove(index)
                            data["cards"].remove(index)
                            json.dump(data, open("user.json", "w"), indent= 4)
            
    def search(self):
        self.tblEnter.clear()
        clsrowcount = self.tblEnter.rowCount()
        while clsrowcount >= 0:
            self.tblEnter.removeRow(clsrowcount)
            clsrowcount -= 1
        data = self.data()
        if self.btnEmployees.isChecked():
            for i in data:
                if "name" in data[i]:
                    if self.linEnterName.text() == data[i]["name"]:
                        if data[i]["type"] == "employee":
                            self.linUserName.setText(data[i]["name"])
                            self.linUserConcode.setText(data[i]["countryCode"])
                            for x in self.data()[i]["cards"]:
                                self.cmbEnterCards.addItem(x)
                            for x in self.data()[i]["history"]:
                                rows = self.tblEnter.rowCount()
                                
                                self.tblEnter.insertRow(rows)
                                for d in x:
                                    columns = x.index(d)
                                    value = QTableWidgetItem(str(d))
                                    
                                    self.tblEnter.setItem(rows, columns, value)
        if self.btnUsers.isChecked():
            for i in data:
                if "name" in data[i]:
                    if self.linEnterName.text() == data[i]["name"]:
                        if data[i]["type"] == "user":
                            self.linUserName.setText(data[i]["name"])
                            self.linUserConcode.setText(data[i]["countryCode"])
                            for x in self.data()[i]["cards"]:
                                self.cmbEnterCards.addItem(x)
                            for x in self.data()[i]["history"]:
                                    rows = self.tblEnter.rowCount()
                                    self.tblEnter.insertRow(rows)
                                    for d in x:
                                        columns = x.index(d)
                                        value = QTableWidgetItem(str(d))
                                        self.tblEnter.setItem(rows, columns, value)
    
    def userReload(self):
        
        count = self.cmbEnterCards.count()
        for i in range(count):
            try:
                self.cmbEnterCards.removeItem(1)
            except IndexError:
                break
                
        for i in self.data():
            if "name" in self.data()[i]:
                if self.data()[i]["name"] == self.linUserName.text():
                    for x in self.data()[i]["cards"]:
                        self.cmbEnterCards.addItem(x)
    
    def proReload(self):
        
        count = self.cmbProCards.count()
        for i in range(count):
            try:
                self.cmbProCards.removeItem(1)
            except IndexError:
                break
                
        for i in self.data()[self.username]["cards"]:
            self.cmbProCards.addItem(i)
    
    def Addcard(self):
        data = self.data()
        
        up = "0"
        for i in self.data()["cards"]:
            if i > up:
                up = i
        up = int(up) + 1
        if self.btnProfile.isChecked():
            if self.data()[self.username]["type"] == "admin":
                data[self.username]["cards"].append(str(up))
                data["cards"].append(str(up))
            else:
                messageBox = QMessageBox.warning(
                self,
                "Error!",
                "type of your account is not a admin",
                QMessageBox.Ok
                )
            
                if messageBox == QMessageBox.Ok:
                    pass
        else:
            for i in data:
                if "name" in data[i]:
                    if data[i]["name"] == self.linUserName.text() and data[i]["type"] == "employee":
                        if self.data()[self.username]["type"] == "admin":
                            data[i]["cards"].append(str(up))
                            data["cards"].append(str(up))
                        else:
                            messageBox = QMessageBox.warning(self, "Error!", "type of your account is not a admin", QMessageBox.Ok)
                            if messageBox == QMessageBox.Ok:
                                pass
                    if data[i]["name"] == self.linUserName.text() and data[i]["type"] == "user":
                        data[i]["cards"].append(str(up))
                        data["cards"].append(str(up))
        
        json.dump(data, open("user.json", "r+"), indent= 4)
        
        

    def mainClick1(self):
        if self.data()[self.username]["type"] == "admin":
            if self.btnSystem.isChecked():
                self.btnProfile.setChecked(False)
                self.btnEmployees.setChecked(False)
                self.btnUsers.setChecked(False)
                self.stack.setCurrentIndex(1)
            else: self.stack.setCurrentIndex(0)
        else:
            self.btnSystem.setChecked(False)
            messageBox = QMessageBox.warning(
            self,
            "Error!",
            "type of your account is not a admin",
            QMessageBox.Ok
            )
        
            if messageBox == QMessageBox.Ok:
                pass

    def mainClick2(self):
        if self.btnProfile.isChecked():
            self.btnSystem.setChecked(False)
            self.btnEmployees.setChecked(False)
            self.btnUsers.setChecked(False)
            self.stack.setCurrentIndex(2)
        else: self.stack.setCurrentIndex(0)

    def mainClick3(self):
        if self.data()[self.username]["type"] == "admin" or self.data()[self.username]["type"] == "employee":
            if self.btnEmployees.isChecked():
                self.btnProfile.setChecked(False)
                self.btnSystem.setChecked(False)
                self.btnUsers.setChecked(False)
                self.stack.setCurrentIndex(3)
                self.linEnterName.clear()
                self.linUserName.clear()
                self.linUserConcode.clear()
                count = self.cmbEnterCards.count()
                for i in range(count):
                    try:
                        self.cmbEnterCards.removeItem(1)
                    except IndexError:
                        break
                row = self.tblEnter.rowCount()
                if row >= 1:
                    for i in range(row):
                        self.tblEnter.removeRow(0)
            else: self.stack.setCurrentIndex(0)
        else:
            self.btnEmployees.setChecked(False)
            messageBox = QMessageBox.warning(
            self,
            "Error!",
            "type of your account is not a admin or employee",
            QMessageBox.Ok
            )
        
            if messageBox == QMessageBox.Ok:
                pass

    def mainClick4(self):
        if self.data()[self.username]["type"] == "admin" or self.data()[self.username]["type"] == "employee":
            if self.btnUsers.isChecked():
                self.btnProfile.setChecked(False)
                self.btnEmployees.setChecked(False)
                self.btnSystem.setChecked(False)
                self.stack.setCurrentIndex(3)
                self.linEnterName.clear()
                self.linUserName.clear()
                self.linUserConcode.clear()
                count = self.cmbEnterCards.count()
                for i in range(count):
                    try:
                        self.cmbEnterCards.removeItem(1)
                    except IndexError:
                        break
                row = self.tblEnter.rowCount()
                if row >= 1:
                    for i in range(row):
                        self.tblEnter.removeRow(0)
            else: self.stack.setCurrentIndex(0)
        else:
            self.btnUsers.setChecked(False)
            messageBox = QMessageBox.warning(
            self,
            "Error!",
            "type of your account is not a admin or employee",
            QMessageBox.Ok
            )
        
            if messageBox == QMessageBox.Ok:
                pass

    def changeLog(self):
        data = self.data()
        if self.linUser.text() in data:
            if self.linPass.text() == data[self.linUser.text()]["password"]:
                self.username = self.linUser.text()
                if data[self.linUser.text()]["type"] == "admin":
                    self.adminPage()
                if data[self.linUser.text()]["type"] == "employee":
                    self.employeePage()
                if data[self.linUser.text()]["type"] == "user":
                    self.userPage()
    def moreDialog(self):
        if self.data()[self.username]["type"] == "admin":
            dialog = more(self)
            dialog.setValue(name= self.linUserName.text(), concode= self.linUserConcode.text())
            
            if dialog.exec() == QDialog.Accepted:
                pass
        elif self.data()[self.username]["type"] == "employee":
            if self.btnEmployees.isChecked() == True:
                messageBox = QMessageBox.warning(self, "Error!", "type of your account is not a admin", QMessageBox.Ok)
                if messageBox == QMessageBox.Ok:
                    pass
            else:    
                dialog = more(self)
                dialog.setValue(name= self.linUserName.text(), concode= self.linUserConcode.text())
                
                if dialog.exec() == QDialog.Accepted:
                    pass

    def data(self):
        return json.load(open("user.json", "r"))
class more(QDialog):
    def __init__(self, parent= None):
        super().__init__()
        
        self.tname = ""
        self.tconcode = ""
        self.new = False
        uic.loadUi("moreDialog.ui", self)
        self.setWindowTitle("More")
        self.syst = system()
        self.edit.clicked.connect(self.cedit)
        self.newAcc.clicked.connect(self.Fnew)
        self.confim.clicked.connect(self.conf)
        self.remove.clicked.connect(self.rem)
    def rem(self):
        print("comingsoon... (0%)")
        if self.new == False and self.edit.isChecked() == False:
            self.close()
        
    def conf(self):
        data = self.syst.data()
        if self.edit.isChecked() == True:
            
            for i in data:
                if 'countryCode' in data[i]:
                    if data[i]['countryCode'] == self.tconcode:
                        data[i]['name'] = self.name.text()
                        data[i]['countryCode'] = self.concode.text()
                        json.dump(data, open("user.json", "w"), indent= 4)
                        self.close()
        elif self.newAcc.isChecked() == True:
            print("Comingsoon... (0%)")
            self.close()
        else:
            self.close()

    def setValue(self, name, concode):
        self.tname = name
        self.tconcode = concode
        self.name.setText(name)
        self.concode.setText(concode)
        
        if self.name.text() == "":
            self.name.setEnabled(False)
            self.concode.setEnabled(False)
            self.edit.setChecked(False)
    def cedit(self):
        if self.edit.isChecked():
            self.name.setEnabled(True)
            self.concode.setEnabled(True)
        else:
            self.name.setEnabled(False)
            self.concode.setEnabled(False)
        
        if self.new == True:
            self.new == False
            self.newAcc.setChecked(False)
            self.name.setText(self.tname)
            self.concode.setText(self.tconcode)
    def Fnew(self):
        if self.newAcc.isChecked():
            self.new = True
        else:
            self.new = False

        if self.new == True:
            self.name.setText("")
            self.name.setEnabled(True)
            self.concode.setText("")
            self.concode.setEnabled(True)
            self.edit.setChecked(False)
        else:
            self.name.setText(self.tname)
            self.concode.setText(self.tconcode)
            self.edit.setChecked(True)

app = QApplication([])
win = system()
app.exec_()