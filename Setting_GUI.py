from GUI.ui_Setting import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtCore import Qt

from winreg import OpenKey, SetValueEx, DeleteValue, HKEY_CURRENT_USER, KEY_ALL_ACCESS, REG_SZ

from Proverka import path_for_autorun

class Setting(QMainWindow):
    def __init__(self, checked_checkbox, checked_checkbox_2):
        super(Setting, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.checkBox.setChecked(checked_checkbox)
        self.ui.checkBox_2.setChecked(checked_checkbox_2)

        self.setWindowFlags(Qt.WindowType.WindowSystemMenuHint)
        self.setFixedSize(416, 92)

        self.ui.pushButton_FAQ_check_1.clicked.connect(self.show_FAQ_check_1)
        self.ui.pushButton_FAQ_check_2.clicked.connect(self.show_FAQ_check_2)

        self.ui.checkBox.stateChanged.connect(self.autorun_checkbox)

    def autorun_checkbox(self, checked):
        full_path_file, name_app = path_for_autorun()

        if checked:
            key = OpenKey(HKEY_CURRENT_USER,"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", 0, KEY_ALL_ACCESS)
            SetValueEx(key, name_app, 0, REG_SZ, full_path_file)
            key.Close()

            self.msg("Information", "Автозапуск додатка активовано.")

        else:
            key = OpenKey(HKEY_CURRENT_USER,"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", 0, KEY_ALL_ACCESS)
            DeleteValue(key, name_app)
            key.Close()

            self.msg("Information", "Автозапуск додатка скасовано.")

    def show_FAQ_check_1(self):
        self.msg("Information", "Додаток додається в автозапуск Windows.")

    def show_FAQ_check_2(self):
        self.msg("Information", "Додаток запускається згорнутим і запускається таймер на закриття додатку, якщо в цей день немає збігу з Вашими даними.\
                 \nТаймер можливо зупинити, якщо протягом 5 хвилин натиснути на відповідну кнопку.")

    def msg(self, reson, message):
        msg = QMessageBox()

        msg.setWindowTitle(reson)
        msg.setText(message)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowFlags(Qt.WindowType.CoverWindow)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()