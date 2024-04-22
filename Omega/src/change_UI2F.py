from PyQt5 import QtCore, QtGui, QtWidgets
import datetime

jan = 31
fab = 28
mar = 31
apr = 30
may = 31
jun = 30
jul = 31
aug = 31
sep = 30
oct = 31
nov = 30
dec = 31

months = [jan, fab, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]

def change_ui2I(instance, MainWindow):
    if instance.type_of_window != 2:
        actual_date = datetime.datetime.now()
        actual_month = actual_date.month
        cur = 0
        while cur < actual_month - 1:
            cur += 1
        instance.centralwidget.deleteLater()
        instance.type_of_window = 2
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
        instance.pushButton_3.setGeometry(QtCore.QRect(30, 210, 75, 23))
        instance.pushButton_3.setObjectName("pushButton_3")

        instance.pushButton_3.clicked.connect(lambda: instance.change_ui3(MainWindow))

        instance.pushButton_4 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_4.setGeometry(QtCore.QRect(180, 80, 171, 51))
        instance.pushButton_4.setObjectName("pushButton_4")
        instance.pushButton_4.clicked.connect(lambda: instance.change_ui4(MainWindow, "01"))
        instance.pushButton_5 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_5.setGeometry(QtCore.QRect(370, 80, 171, 51))
        instance.pushButton_5.setObjectName("pushButton_5")
        instance.pushButton_5.clicked.connect(lambda: instance.change_ui4(MainWindow, "02"))
        instance.pushButton_6 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_6.setGeometry(QtCore.QRect(560, 80, 171, 51))
        instance.pushButton_6.setObjectName("pushButton_6")
        instance.pushButton_6.clicked.connect(lambda: instance.change_ui4(MainWindow, "03"))
        instance.pushButton_7 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_7.setGeometry(QtCore.QRect(750, 80, 171, 51))
        instance.pushButton_7.setObjectName("pushButton_7")
        instance.pushButton_7.clicked.connect(lambda: instance.change_ui4(MainWindow, "04"))
        instance.pushButton_8 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_8.setGeometry(QtCore.QRect(940, 80, 171, 51))
        instance.pushButton_8.setObjectName("pushButton_8")
        instance.pushButton_8.clicked.connect(lambda: instance.change_ui4(MainWindow, "05"))
        instance.pushButton_9 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_9.setGeometry(QtCore.QRect(180, 150, 171, 51))
        instance.pushButton_9.setObjectName("pushButton_9")
        instance.pushButton_9.clicked.connect(lambda: instance.change_ui4(MainWindow, "06"))
        instance.pushButton_10 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_10.setGeometry(QtCore.QRect(370, 150, 171, 51))
        instance.pushButton_10.setObjectName("pushButton_10")
        instance.pushButton_10.clicked.connect(lambda: instance.change_ui4(MainWindow, "07"))
        instance.pushButton_11 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_11.setGeometry(QtCore.QRect(560, 150, 171, 51))
        instance.pushButton_11.setObjectName("pushButton_11")
        instance.pushButton_11.clicked.connect(lambda: instance.change_ui4(MainWindow, "08"))
        instance.pushButton_12 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_12.setGeometry(QtCore.QRect(750, 150, 171, 51))
        instance.pushButton_12.setObjectName("pushButton_12")
        instance.pushButton_12.clicked.connect(lambda: instance.change_ui4(MainWindow, "09"))
        instance.pushButton_13 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_13.setGeometry(QtCore.QRect(940, 150, 171, 51))
        instance.pushButton_13.setObjectName("pushButton_13")
        instance.pushButton_13.clicked.connect(lambda: instance.change_ui4(MainWindow, 10))
        instance.pushButton_14 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_14.setGeometry(QtCore.QRect(180, 220, 171, 51))
        instance.pushButton_14.setObjectName("pushButton_14")
        instance.pushButton_14.clicked.connect(lambda: instance.change_ui4(MainWindow, 11))
        instance.pushButton_15 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_15.setGeometry(QtCore.QRect(370, 220, 171, 51))
        instance.pushButton_15.setObjectName("pushButton_15")
        instance.pushButton_15.clicked.connect(lambda: instance.change_ui4(MainWindow, 12))
        instance.pushButton_16 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_16.setGeometry(QtCore.QRect(560, 220, 171, 51))
        instance.pushButton_16.setObjectName("pushButton_16")
        instance.pushButton_16.clicked.connect(lambda: instance.change_ui4(MainWindow, 13))
        instance.pushButton_17 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_17.setGeometry(QtCore.QRect(750, 220, 171, 51))
        instance.pushButton_17.setObjectName("pushButton_17")
        instance.pushButton_17.clicked.connect(lambda: instance.change_ui4(MainWindow, 14))
        instance.pushButton_18 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_18.setGeometry(QtCore.QRect(940, 220, 171, 51))
        instance.pushButton_18.setObjectName("pushButton_18")
        instance.pushButton_18.clicked.connect(lambda: instance.change_ui4(MainWindow, 15))
        instance.pushButton_19 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_19.setGeometry(QtCore.QRect(180, 290, 171, 51))
        instance.pushButton_19.setObjectName("pushButton_19")
        instance.pushButton_19.clicked.connect(lambda: instance.change_ui4(MainWindow, 16))
        instance.pushButton_20 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_20.setGeometry(QtCore.QRect(370, 290, 171, 51))
        instance.pushButton_20.setObjectName("pushButton_20")
        instance.pushButton_20.clicked.connect(lambda: instance.change_ui4(MainWindow, 17))
        instance.pushButton_21 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_21.setGeometry(QtCore.QRect(560, 290, 171, 51))
        instance.pushButton_21.setObjectName("pushButton_21")
        instance.pushButton_21.clicked.connect(lambda: instance.change_ui4(MainWindow, 18))
        instance.pushButton_22 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_22.setGeometry(QtCore.QRect(750, 290, 171, 51))
        instance.pushButton_22.setObjectName("pushButton_22")
        instance.pushButton_22.clicked.connect(lambda: instance.change_ui4(MainWindow, 19))
        instance.pushButton_23 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_23.setGeometry(QtCore.QRect(940, 290, 171, 51))
        instance.pushButton_23.setObjectName("pushButton_23")
        instance.pushButton_23.clicked.connect(lambda: instance.change_ui4(MainWindow, 20))
        instance.pushButton_24 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_24.setGeometry(QtCore.QRect(180, 360, 171, 51))
        instance.pushButton_24.setObjectName("pushButton_24")
        instance.pushButton_24.clicked.connect(lambda: instance.change_ui4(MainWindow, 21))
        instance.pushButton_25 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_25.setGeometry(QtCore.QRect(370, 360, 171, 51))
        instance.pushButton_25.setObjectName("pushButton_25")
        instance.pushButton_25.clicked.connect(lambda: instance.change_ui4(MainWindow, 22))
        instance.pushButton_26 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_26.setGeometry(QtCore.QRect(560, 360, 171, 51))
        instance.pushButton_26.setObjectName("pushButton_26")
        instance.pushButton_26.clicked.connect(lambda: instance.change_ui4(MainWindow, 23))
        instance.pushButton_27 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_27.setGeometry(QtCore.QRect(750, 360, 171, 51))
        instance.pushButton_27.setObjectName("pushButton_27")
        instance.pushButton_27.clicked.connect(lambda: instance.change_ui4(MainWindow, 24))
        instance.pushButton_28 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_28.setGeometry(QtCore.QRect(940, 360, 171, 51))
        instance.pushButton_28.setObjectName("pushButton_28")
        instance.pushButton_28.clicked.connect(lambda: instance.change_ui4(MainWindow, 25))
        instance.pushButton_29 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_29.setGeometry(QtCore.QRect(180, 430, 171, 51))
        instance.pushButton_29.setObjectName("pushButton_29")
        instance.pushButton_29.clicked.connect(lambda: instance.change_ui4(MainWindow, 26))
        instance.pushButton_30 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_30.setGeometry(QtCore.QRect(370, 430, 171, 51))
        instance.pushButton_30.setObjectName("pushButton_30")
        instance.pushButton_30.clicked.connect(lambda: instance.change_ui4(MainWindow, 27))
        instance.pushButton_31 = QtWidgets.QPushButton(instance.centralwidget)
        instance.pushButton_31.setGeometry(QtCore.QRect(560, 430, 171, 51))
        instance.pushButton_31.setObjectName("pushButton_31")
        instance.pushButton_31.clicked.connect(lambda: instance.change_ui4(MainWindow, 28))
        if months[cur] >= 29:
            instance.pushButton_32 = QtWidgets.QPushButton(instance.centralwidget)
            instance.pushButton_32.setGeometry(QtCore.QRect(750, 430, 171, 51))
            instance.pushButton_32.setObjectName("pushButton_32")
            instance.pushButton_32.clicked.connect(lambda: instance.change_ui4(MainWindow, 29))
        if months[cur] >= 30:
            instance.pushButton_33 = QtWidgets.QPushButton(instance.centralwidget)
            instance.pushButton_33.setGeometry(QtCore.QRect(940, 430, 171, 51))
            instance.pushButton_33.setObjectName("pushButton_33")
            instance.pushButton_33.clicked.connect(lambda: instance.change_ui4(MainWindow, 30))
        if months[cur] == 31:
            instance.pushButton_34 = QtWidgets.QPushButton(instance.centralwidget)
            instance.pushButton_34.setGeometry(QtCore.QRect(180, 500, 171, 51))
            instance.pushButton_34.setObjectName("pushButton_34")
            instance.pushButton_34.clicked.connect(lambda: instance.change_ui4(MainWindow, 31))

        MainWindow.setCentralWidget(instance.centralwidget)
        instance.retranslateUi(MainWindow)