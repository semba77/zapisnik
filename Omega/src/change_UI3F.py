from PyQt5 import QtCore, QtGui, QtWidgets

def change_ui3I(instance, MainWindow):
    if instance.type_of_window != 3:
        instance.centralwidget.deleteLater()
        instance.type_of_window = 3

        instance.centralwidget = QtWidgets.QWidget(MainWindow)
        instance.centralwidget.setObjectName("centralwidget")
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
        instance.pushButton_3.setGeometry(QtCore.QRect(30, 210, 75, 21))
        instance.pushButton_3.setObjectName("pushButton_3")

        instance.pushButton_3.clicked.connect(lambda: instance.change_ui3(MainWindow))
        try:
            task_dates = list(map(list, zip(*instance.tasks)))
        except Exception as e:
            print(e)
        print(task_dates[2][0].day)
        instance.pushButton_4 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_4.setGeometry(QtCore.QRect(180, 80, 931, 51))
        instance.pushButton_4.setObjectName("pushButton_4")
        instance.pushButton_4.clicked.connect(lambda: instance.change_ui4(MainWindow, task_dates[2][0].day))
        instance.pushButton_5 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_5.setGeometry(QtCore.QRect(180, 140, 931, 51))
        instance.pushButton_5.setObjectName("pushButton_5")
        instance.pushButton_5.clicked.connect(lambda: instance.change_ui4(MainWindow, task_dates[2][1].day))
        instance.pushButton_6 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_6.setGeometry(QtCore.QRect(180, 200, 931, 51))
        instance.pushButton_6.setObjectName("pushButton_6")
        instance.pushButton_6.clicked.connect(lambda: instance.change_ui4(MainWindow, task_dates[2][2].day))
        instance.pushButton_7 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_7.setGeometry(QtCore.QRect(180, 260, 931, 51))
        instance.pushButton_7.setObjectName("pushButton_7")
        instance.pushButton_7.clicked.connect(lambda: instance.change_ui4(MainWindow, task_dates[2][3].day))
        instance.pushButton_8 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_8.setGeometry(QtCore.QRect(180, 320, 931, 51))
        instance.pushButton_8.setObjectName("pushButton_8")
        instance.pushButton_8.clicked.connect(lambda: instance.change_ui4(MainWindow, task_dates[2][4].day))
        instance.pushButton_9 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_9.setGeometry(QtCore.QRect(180, 380, 931, 51))
        instance.pushButton_9.setObjectName("pushButton_9")
        instance.pushButton_9.clicked.connect(lambda: instance.change_ui4(MainWindow, task_dates[2][5].day))
        instance.pushButton_10 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_10.setGeometry(QtCore.QRect(180, 440, 931, 51))
        instance.pushButton_10.setObjectName("pushButton_10")

        MainWindow.setCentralWidget(instance.centralwidget)
        instance.retranslateUi(MainWindow)