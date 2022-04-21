import sys
import sqlite3
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog


apply_user = list()

class Mainwindow(QDialog):
    def __init__(self):
        super(Mainwindow, self).__init__()
        loadUi("window_welcome.ui", self)
        self.pushButton_login.clicked.connect(self.gotologin)
        self.pushButton_create.clicked.connect(self.gotosign)

    def gotologin(self):
        login = Otherwindow()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotosign(self):
        sign = Createwindow()
        widget.addWidget(sign)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Otherwindow(QDialog):
    def __init__(self):
        super(Otherwindow, self).__init__()
        loadUi("login.ui", self)
        self.flag = True

        self.names = False
        self.passwords = False

        self.pushButton_cancel.clicked.connect(self.gotocancel)
        self.pushButton_loginin.clicked.connect(self.loginfunc)
        self.pushButton_show.clicked.connect(self.showfunction)
        self.pushButton_forgot.clicked.connect(self.gotoforgot)


    def loginfunc(self):
        user = self.lineEdit_username.text()
        password = self.lineEdit_password.text()

        if len(user) == 0 or len(password) == 0:
            self.label_error.setText("Please input all fields!")
        else:
            conn = sqlite3.connect('date.db')

            cur = conn.cursor()
            c = conn.cursor()

            cur.execute(f'SELECT password FROM inf WHERE username="{user}";')
            c.execute(f'SELECT username FROM inf WHERE password="{password}";')

            value = cur.fetchone()
            val = c.fetchone()

            name = ''
            pas = ''

            if val == None:
                self.label_error.setText("invalid")
            elif val != None:
                name += val[0]

            if value == None:
                self.label_error.setText("invalid")
            elif value != None:
                pas += value[0]

            if user == name:
                self.names = True
            if password == pas:
                self.passwords = True
            if  self.names and self.passwords == True:
                welcome = Mainwindow()
                widget.addWidget(welcome)
                widget.setCurrentIndex(widget.currentIndex() + 1)

    def showfunction(self):
        if self.flag == True:
            self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
            self.flag = False
        elif self.flag == False:
            self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.flag = True

    def gotocancel(self):
        welcome = Mainwindow()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoforgot(self):
        forgot = Forgotwindow()
        widget.addWidget(forgot)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Createwindow(QDialog):
    def __init__(self):
        super(Createwindow, self).__init__()
        loadUi("sign.ui", self)
        self.flag_1 = True
        self.flag_2 = True

        self.pushButton_cancel.clicked.connect(self.gotocancel)
        self.pushButton_sign.clicked.connect(self.signfunction)

        self.pushButton_show.clicked.connect(self.showfunction)
        self.pushButton_show_2.clicked.connect(self.show_2function)

    def signfunction(self):
        user = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        confirm = self.lineEdit_password_confirm.text()

        if len(user) == 0 or len(password) == 0:
            self.label_error_2.setText("Please input all fields!")
        elif password != confirm:
            self.label_error_2.setText("Password don't match")
        else:
            conn = sqlite3.connect("date.db")
            cur = conn.cursor()

            user_info = [user, password]
            cur.execute('INSERT INTO inf (username, password) VALUES(?,?)', user_info)

            conn.commit()
            conn.close()

            welcome = Mainwindow()
            widget.addWidget(welcome)
            widget.setCurrentIndex(widget.currentIndex() + 1)


    def showfunction(self):
        if self.flag_1 == True:
            self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
            self.flag_1 = False
        elif self.flag_1 == False:
            self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.flag_1 = True
    def show_2function(self):
        if self.flag_2 == True:
            self.lineEdit_password_confirm.setEchoMode(QtWidgets.QLineEdit.Password)
            self.flag_2 = False
        elif self.flag_2 == False:
            self.lineEdit_password_confirm.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.flag_2 = True
    def gotocancel(self):
        welcome = Mainwindow()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Forgotwindow(QDialog):
    def __init__(self):
        super(Forgotwindow, self).__init__()
        loadUi("forgot.ui", self)
        self.names = False
        self.pushButton_cancel.clicked.connect(self.gotocancel)
        self.pushButton_search.clicked.connect(self.searchfunc)

    def searchfunc(self):
        user = self.lineEdit_username.text()
        if len(user) == 0:
            self.label_error.setText("Please input all fields!")
        else:
            conn = sqlite3.connect('date.db')
            cur = conn.cursor()
            value  = cur.execute('SELECT username FROM inf WHERE username == ?', (user,)).fetchone()

            if value == None:
                self.label_error.setText("invalid")
            elif value != None:
                global apply_user
                apply_user += value
                self.names = True

            if  self.names == True:
                 password = Passwordwindow()
                 widget.addWidget(password)
                 widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotocancel(self):
        login = Otherwindow()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Passwordwindow(QDialog):
    def __init__(self):
        super(Passwordwindow, self).__init__()
        loadUi("password.ui", self)
        self.new_flag = True
        self.confilm_flag = True

        self.pushButton_apply.clicked.connect(self.appyfunction)

        self.pushButton_show_new_111.clicked.connect(self.news_show)
        self.pushButton_show_confilm_111.clicked.connect(self.confilms_show)

        self.pushButton_cancel.clicked.connect(self.gotocancel)

    def appyfunction(self):
        password = self.lineEdit_password_new_1111.text()
        confilm =  self.lineEdit_password_confilm_1111.text()
        name = apply_user[0]

        if len(confilm) == 0 and len(password) == 0:
            self.label_error.setText("Please input all fields!")
        elif confilm != password:
            self.label_error.setText("Invalid password")
        else:
            conn = sqlite3.connect('date.db')

            cur = conn.cursor()
            c = conn.cursor()

            cur.execute('UPDATE inf SET password == ? WHERE username == ?', (password, name))
            conn.commit()

            welcome = Mainwindow()
            widget.addWidget(welcome)
            widget.setCurrentIndex(widget.currentIndex() + 1)

    def news_show(self):
        if self.new_flag == True:
            self.lineEdit_password_new_1111.setEchoMode(QtWidgets.QLineEdit.Password)
            self.new_flag = False
        elif self.new_flag == False:
            self.lineEdit_password_new_1111.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.new_flag = True

    def confilms_show(self):
        if self.confilm_flag == True:
            self.lineEdit_password_confilm_1111.setEchoMode(QtWidgets.QLineEdit.Password)
            self.confilm_flag = False
        elif self.confilm_flag == False:
            self.lineEdit_password_confilm_1111.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.confilm_flag = True

    def gotocancel(self):
        login = Otherwindow()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)





app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
mainwindow = Mainwindow()
#otherwindow = OtherMain()
widget.addWidget(mainwindow)
#widget.addWidget(otherwindow)
widget.setFixedWidth(600)
widget.setFixedHeight(500)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting!")
