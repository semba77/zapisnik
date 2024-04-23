from PyQt5 import QtCore, QtGui, QtWidgets

def change_ui1I(instance,MainWindow):
    if instance.type_of_window != 1:
        instance.centralwidget.deleteLater()
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
        instance.retranslateUi(MainWindow)