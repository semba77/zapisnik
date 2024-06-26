import sys
import re
import setupUIF
import datetime
import retranslateUIF
import changeUI1F
import change_UI2F
import change_UI3F
import change_UI4F
import extansions
import facade
from PyQt5 import QtCore, QtGui, QtWidgets



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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        setupUIF.setup(self, MainWindow)

    def retranslateUi(self, MainWindow):
        retranslateUIF.retranslate(self, MainWindow)

    def change_ui1(self, MainWindow):
        changeUI1F.change_ui1I(self, MainWindow)
    def change_ui2(self, MainWindow):
        change_UI2F.change_ui2I(self, MainWindow)
    def change_ui3(self, MainWindow):
        change_UI3F.change_ui3I(self, MainWindow)
    def change_ui4(self, MainWindow, date):
        change_UI4F.change_ui4I(self, MainWindow, date)

    def save_event(self, text):
        if text == "getname":
            extansions.true_name.get_random_name()
        if text == "funfact":
            extansions.facts.get_random_funfact()
        if text == "animal":
            extansions.animal.get_random_animal()
        if text == "city":
            extansions.city.cities()
        if text == "country":
            extansions.country.get_random_state()
        if text == "river":
            extansions.river.get_random_river()
        print(text)
        pattern = r'\{([^}]+)\}'
        matches = re.findall(pattern, text)
        for match in matches:
            extansions.facade.notebook(match)

    def del_event(self,event):
        extansions.facade.del_event(event)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())