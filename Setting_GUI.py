from GUI.ui_Setting import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtCore import Qt

from winreg import OpenKey, SetValueEx, DeleteValue, HKEY_CURRENT_USER, KEY_ALL_ACCESS, REG_SZ

from Proverka import path_for_autorun

class Setting(QMainWindow):
    def __init__(self, checked_checkbox_autorun, checked_checkbox_collapse_window,
                 checked_checkbox_list_birth_last, checked_checkbox_list_birth_future, spinbox_min, spinbox_sec):

        super(Setting, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.checkBox_autorun.setChecked(checked_checkbox_autorun)
        self.ui.checkBox_collapse_window.setChecked(checked_checkbox_collapse_window)
        self.ui.checkBox_list_birth_last.setChecked(checked_checkbox_list_birth_last)
        self.ui.checkBox_list_birth_future.setChecked(checked_checkbox_list_birth_future)
        self.ui.spinBox_minutes.setValue(spinbox_min)
        self.ui.spinBox_seconds.setValue(spinbox_sec)

        self.setWindowFlags(Qt.WindowType.WindowSystemMenuHint)
        self.setFixedSize(416, 269)

        self.ui.pushButton_FAQ_autorun.clicked.connect(self.show_FAQ_checkbox_autorun)
        self.ui.pushButton_FAQ_collapse_window.clicked.connect(self.show_FAQ_checkbox_collapse_window)
        self.ui.pushButton_FAQ_list_birth_last.clicked.connect(self.show_FAQ_checkbox_list_birth_last)
        self.ui.pushButton_FAQ_list_birth_future.clicked.connect(self.show_FAQ_checkbox_list_birth_future)
        self.ui.pushButton_FAQ_timer.clicked.connect(self.show_FAQ_checkbox_timer_time)

        self.ui.checkBox_autorun.stateChanged.connect(self.autorun_checkbox)

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

    def show_FAQ_checkbox_autorun(self):
        self.msg("Information", "Додаток додається в автозапуск Windows.")

    def show_FAQ_checkbox_collapse_window(self):
        self.msg("Information", f"Додаток запускається згорнутим і запускається таймер на закриття додатку, якщо людину, яка має День народження на поточну дату, не знайдено.\
                 \nТаймер можливо зупинити, якщо протягом {self.ui.spinBox_minutes.value()} хвилин {self.ui.spinBox_seconds.value()} секунд натиснути на відповідну кнопку.")

    def show_FAQ_checkbox_list_birth_last(self):
        self.msg("Information", "Додається табличка з ім'ям людини День народження, якого вже пройшов на поточну дату.")

    def show_FAQ_checkbox_list_birth_future(self):
        self.msg("Information", "Додається табличка з ім'ям людини День народження, якого настане.")

    def show_FAQ_checkbox_timer_time(self):
        self.msg("Information", "Змінити час на закриття додатку. \
                        \n\nЗакриття відбувається при увімкненій функції 'Після запуску згорнути додаток'.")

    def msg(self, reson, message):
        msg = QMessageBox()

        msg.setWindowTitle(reson)
        msg.setText(message)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowFlags(Qt.WindowType.CoverWindow)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()