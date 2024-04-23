from PyQt5 import QtCore, QtGui, QtWidgets
import sys

def setup(instance,MainWindow):
    MainWindow.setObjectName("MainWindow")
    MainWindow.resize(1125, 603)
    instance.type_of_window = 1
    instance.centralwidget = QtWidgets.QWidget(MainWindow)
    instance.centralwidget.setObjectName("centralwidget")
    instance.textEdit = QtWidgets.QTextEdit(instance.centralwidget)
    instance.textEdit.setGeometry(QtCore.QRect(150, 80, 971, 491))
    instance.textEdit.setObjectName("textEdit")
    instance.pushButton = QtWidgets.QPushButton(instance.centralwidget)
    instance.pushButton.setGeometry(QtCore.QRect(30, 80, 75, 23))
    instance.pushButton.setCheckable(False)
    instance.pushButton.setObjectName("pushButton")

    instance.pushButton.clicked.connect(lambda: instance.change_ui1(MainWindow))

    instance.pushButton_2 = QtWidgets.QPushButton(instance.centralwidget)
    instance.pushButton_2.setGeometry(QtCore.QRect(30, 150, 75, 23))
    instance.pushButton_2.setObjectName("pushButton_2")

    instance.pushButton_2.clicked.connect(lambda: instance.change_ui2(MainWindow))

    instance.pushButton_3 = QtWidgets.QPushButton(instance.centralwidget)
    instance.pushButton_3.setGeometry(QtCore.QRect(30, 210, 75, 23))
    instance.pushButton_3.setObjectName("pushButton_3")

    instance.pushButton_3.clicked.connect(lambda: instance.change_ui3(MainWindow))

    instance.save_Button = QtWidgets.QPushButton(instance.centralwidget)
    instance.save_Button.setGeometry(QtCore.QRect(30, 270, 75, 23))
    instance.save_Button.setObjectName("save_Button")
    instance.save_Button.clicked.connect(lambda: instance.save_event(instance.textEdit.toPlainText()))

    MainWindow.setCentralWidget(instance.centralwidget)
    instance.menubar = QtWidgets.QMenuBar(MainWindow)
    instance.menubar.setGeometry(QtCore.QRect(0, 0, 1125, 21))
    instance.menubar.setObjectName("menubar")
    instance.menunastaven = QtWidgets.QMenu(instance.menubar)
    instance.menunastaven.setObjectName("menunastaven")
    MainWindow.setMenuBar(instance.menubar)
    instance.statusbar = QtWidgets.QStatusBar(MainWindow)
    instance.statusbar.setObjectName("statusbar")
    MainWindow.setStatusBar(instance.statusbar)
    instance.actionsv_tl = QtWidgets.QAction(MainWindow)
    instance.actionsv_tl.setObjectName("actionsv_tl")
    instance.actiontmav = QtWidgets.QAction(MainWindow)
    instance.actiontmav.setObjectName("actiontmav")
    instance.actionenglish = QtWidgets.QAction(MainWindow)
    instance.actionenglish.setObjectName("actionenglish")
    instance.action_estina = QtWidgets.QAction(MainWindow)
    instance.action_estina.setObjectName("action_estina")
    instance.menunastaven.addAction(instance.actionsv_tl)
    instance.menunastaven.addAction(instance.actiontmav)
    instance.menunastaven.addAction(instance.actionenglish)
    instance.menunastaven.addAction(instance.action_estina)
    instance.menubar.addAction(instance.menunastaven.menuAction())

    instance.retranslateUi(MainWindow)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)