from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import extansions

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
def retranslate(instance,MainWindow):
    instance.tasks = extansions.facade.find_all_tasks()
    actual_date = datetime.datetime.now()
    actual_month = actual_date.month
    cur = 0
    while cur < actual_month - 1:
        cur += 1
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    if instance.type_of_window < 4:
        instance.pushButton.setText(_translate("MainWindow", "zapisník"))
        instance.pushButton_2.setText(_translate("MainWindow", "kalendář"))
        instance.pushButton_3.setText(_translate("MainWindow", "to do"))
    else:
        date_tasks = extansions.facade.find_everything_for_date(f'{datetime.datetime.now().year}-0{datetime.datetime.now().month}-{instance.chosen_date}')
        date_tasks = list(map(list, zip(*date_tasks)))
        print(date_tasks)
        instance.pushButton.setText(_translate("MainWindow", "zpět"))
        instance.pushButton_2.setText(_translate("MainWindow", "další"))
        instance.pushButton_3.setText(_translate("MainWindow", "nový úkol"))
        #instance.pushButton_4.setText(_translate("MainWindow", "x"))
        #instance.pushButton_5.setText(_translate("MainWindow", "x"))
        #instance.pushButton_6.setText(_translate("MainWindow", "x"))
        #instance.pushButton_7.setText(_translate("MainWindow", "x"))
        if len(date_tasks[0]) >= 1:
            instance.label.setText(_translate("MainWindow", f"{date_tasks[1][0]}"))
            instance.label_2.setText(_translate("MainWindow", f"{date_tasks[2][0]}"))
        if len(date_tasks[0]) >= 2:
            instance.label_3.setText(_translate("MainWindow", f"{date_tasks[1][1]}"))
            instance.label_4.setText(_translate("MainWindow", f"{date_tasks[2][1]}"))
        if len(date_tasks[0]) >= 3:
            instance.label_5.setText(_translate("MainWindow", f"{date_tasks[1][2]}"))
            instance.label_6.setText(_translate("MainWindow", f"{date_tasks[2][2]}"))
        if len(date_tasks[0]) >= 4:
            instance.label_7.setText(_translate("MainWindow", f"{date_tasks[1][3]}"))
            instance.label_8.setText(_translate("MainWindow", f"{date_tasks[2][3]}"))

    if instance.type_of_window == 1:
        instance.save_Button.setText(_translate("MainWindow", "save event"))
    if instance.type_of_window == 2:
        instance.pushButton_4.setText(_translate("MainWindow", "1"))
    if instance.type_of_window == 2:
        instance.pushButton_5.setText(_translate("MainWindow", "2"))
    if instance.type_of_window == 2:
        instance.pushButton_6.setText(_translate("MainWindow", "3"))
    if instance.type_of_window == 2:
        instance.pushButton_7.setText(_translate("MainWindow", "4"))
    if instance.type_of_window == 2:
        instance.pushButton_8.setText(_translate("MainWindow", "5"))
    if instance.type_of_window == 2:
        instance.pushButton_9.setText(_translate("MainWindow", "6"))
    if instance.type_of_window == 2:
        instance.pushButton_10.setText(_translate("MainWindow", "7"))
    if instance.type_of_window == 2:
        instance.pushButton_11.setText(_translate("MainWindow", "8"))
    if instance.type_of_window == 2:
        instance.pushButton_12.setText(_translate("MainWindow", "9"))
    if instance.type_of_window == 2:
        instance.pushButton_13.setText(_translate("MainWindow", "10"))
    if instance.type_of_window == 2:
        instance.pushButton_14.setText(_translate("MainWindow", "11"))
    if instance.type_of_window == 2:
        instance.pushButton_15.setText(_translate("MainWindow", "12"))
    if instance.type_of_window == 2:
        instance.pushButton_16.setText(_translate("MainWindow", "13"))
    if instance.type_of_window == 2:
        instance.pushButton_17.setText(_translate("MainWindow", "14"))
    if instance.type_of_window == 2:
        instance.pushButton_18.setText(_translate("MainWindow", "15"))
    if instance.type_of_window == 2:
        instance.pushButton_19.setText(_translate("MainWindow", "16"))
    if instance.type_of_window == 2:
        instance.pushButton_20.setText(_translate("MainWindow", "17"))
    if instance.type_of_window == 2:
        instance.pushButton_21.setText(_translate("MainWindow", "18"))
    if instance.type_of_window == 2:
        instance.pushButton_22.setText(_translate("MainWindow", "19"))
    if instance.type_of_window == 2:
        instance.pushButton_23.setText(_translate("MainWindow", "20"))
    if instance.type_of_window == 2:
        instance.pushButton_24.setText(_translate("MainWindow", "21"))
    if instance.type_of_window == 2:
        instance.pushButton_25.setText(_translate("MainWindow", "22"))
    if instance.type_of_window == 2:
        instance.pushButton_26.setText(_translate("MainWindow", "23"))
    if instance.type_of_window == 2:
        instance.pushButton_27.setText(_translate("MainWindow", "24"))
    if instance.type_of_window == 2:
        instance.pushButton_28.setText(_translate("MainWindow", "25"))
    if instance.type_of_window == 2:
        instance.pushButton_29.setText(_translate("MainWindow", "26"))
    if instance.type_of_window == 2:
        instance.pushButton_30.setText(_translate("MainWindow", "27"))
    if instance.type_of_window == 2:
        instance.pushButton_31.setText(_translate("MainWindow", "28"))
    if instance.type_of_window == 2 and months[cur] >= 29:
        instance.pushButton_32.setText(_translate("MainWindow", "29"))
    if instance.type_of_window == 2 and months[cur] >= 30:
        instance.pushButton_33.setText(_translate("MainWindow", "30"))
    if instance.type_of_window == 2 and months[cur] == 31:
        instance.pushButton_34.setText(_translate("MainWindow", "31"))
    if instance.type_of_window == 3:

        print(instance.tasks)
        if len(instance.tasks) >= 1:
            instance.pushButton_4.setText(_translate("MainWindow", f"{instance.tasks[0]}"))
        if len(instance.tasks) >= 2:
            instance.pushButton_5.setText(_translate("MainWindow", f"{instance.tasks[1]}"))
        if len(instance.tasks) >= 3:
            instance.pushButton_6.setText(_translate("MainWindow", f"{instance.tasks[2]}"))
        if len(instance.tasks) >= 4:
            instance.pushButton_7.setText(_translate("MainWindow", f"{instance.tasks[3]}"))
        if len(instance.tasks) >= 5:
            instance.pushButton_8.setText(_translate("MainWindow", f"{instance.tasks[4]}"))
        if len(instance.tasks) >= 6:
            instance.pushButton_9.setText(_translate("MainWindow", f"{instance.tasks[5]}"))
    instance.menunastaven.setTitle(_translate("MainWindow", "nastavení"))
    instance.actionsv_tl.setText(_translate("MainWindow", "světlý"))
    instance.actiontmav.setText(_translate("MainWindow", "tmavý"))
    instance.actionenglish.setText(_translate("MainWindow", "english"))
    instance.action_estina.setText(_translate("MainWindow", "čestina"))