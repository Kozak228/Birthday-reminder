from GUI.ui_Remind_main import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMessageBox, QMainWindow, QFileDialog, QSystemTrayIcon, QMenu
from PyQt6.QtCore import QDate, Qt, QTimer
from PyQt6.QtGui import QAction, QIcon
from sys import exit

from win10toast import ToastNotifier

from Create_data_GUI import Create_data
from Update_data_GUI import Update_data
from Setting_GUI import Setting

from Time_date_format import add_zero, s_in_m_s
from Proverka import proverka_file, proverka_dir, proverka_path_in_config, proverka_path_in_icons_dir
from Read_file import read_file
from Write_file import write_file
from Loging_error import logger_init
from Sorted import sort_data

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.file_name = "List of happy birthdays"
        self.name_file_config = "Config"
        self.dir_name_config = "Birthday reminder"
        self.dict_birth = {}
        self.all_sec = 120

        logger_init('app')

        self.setWindowFlags(Qt.WindowType.BypassWindowManagerHint)
        self.setFixedSize(579, 340)

        self.path_dir_icons = proverka_path_in_icons_dir()

        self.checked_checkbox_autorun, self.checked_checkbox_collapse_window = False, False
        self.checked_checkbox_list_birth_last, self.checked_checkbox_list_birth_future = False, False
        self.spinbox_min, self.spinbox_sec = 2, 0

        self.ui.pushButton_clear.setEnabled(False)
        self.ui.pushButton_update_file.setEnabled(False)

        self.ui.groupBox_3.hide()

        self.welcome_app()

        self.ui.pushButton_exit.clicked.connect(self.btn_app_exit)
        self.ui.pushButton_setting.clicked.connect(self.setting_win)
        self.ui.pushButton_FAQ_path.clicked.connect(self.show_FAQ_path)
        self.ui.pushButton_path_file.clicked.connect(self.path_folder)
        self.ui.pushButton_create_file.clicked.connect(self.create_file)
        self.ui.pushButton_update_file.clicked.connect(self.update_file)
        self.ui.pushButton_stop_timer.clicked.connect(self.stop_timer)
        self.ui.pushButton_clear.clicked.connect(self.btn_clear_path)
        self.ui.calendarWidget.clicked[QDate].connect(self.show_date_select_wdg)
        self.ui.line_path.textChanged.connect(lambda text: self.ui.pushButton_clear.setEnabled(bool(text)))

        self.reload_exist()
        self.read_config()

        self.setting_window = Setting(self.checked_checkbox_autorun, self.checked_checkbox_collapse_window,
                                      self.checked_checkbox_list_birth_last, self.checked_checkbox_list_birth_future,
                                      self.spinbox_min, self.spinbox_sec)

        self.setWindowIcon(QIcon(f"{self.path_dir_icons}birth.ico"))
        self.tray_icon = QSystemTrayIcon(QIcon(f"{self.path_dir_icons}birth.ico"))        

        self.tray_gui()

        self.push_notification = ToastNotifier()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_timer)

        self.change_size_window()
        self.show_last_and_future_data()

        self.run_app_in_collapse()

        self.create_data_window = Create_data(self.file_name)

        date = self.ui.calendarWidget.selectedDate().toString('dd.MM')
        self.ui.label_info_birth_now.setText(f"{date}\nвідзначає День Народження.")

    def welcome_app(self):
        if not proverka_path_in_config(self.dir_name_config, True):
            self.msg(f"Welcome to '{self.dir_name_config}'", "Додаток нагадує про дні народження друзів. У ньому є підказки, раджу тобі з ними ознайомитись перед використанням додатку, кнопка із знаком питання.\
                     \n\nРаджу спочатку створити файл, записавши в нього дані про дні народження друзів, для цього натисніть 'Створити дані'.")

    def show_timer(self):
        if self.all_sec <= 0:
            self.timer.stop()
            self.exit_app()
        else:
            self.all_sec -= 1
            s, m = s_in_m_s(self.all_sec)

            self.ui.label_timer.setText(f"{add_zero(m)} м. {add_zero(s)} с.")

    def stop_timer(self):
        self.timer.stop()
        self.msg("Information", "Закриття додатку скасовано.")
        self.ui.groupBox_3.hide()
        self.change_size_window()

    def change_size_window(self):
        if not self.timer.isActive() and not self.setting_window.ui.checkBox_list_birth_last.isChecked() and not \
                self.setting_window.ui.checkBox_list_birth_future.isChecked():

            self.ui.label_info_birth_last.hide()
            self.ui.listWidget_birth_last.hide()
            self.ui.label_info_birth_future.hide()
            self.ui.listWidget_birth_future.hide()

            self.setFixedHeight(340)
            self.ui.label_info_birth_now.move(333, 160)
            self.ui.listWidget_birth_now.move(332, 204)
            self.ui.pushButton_exit.move(514, 304)
            self.ui.pushButton_setting.move(418, 304)

        elif self.timer.isActive() and not self.setting_window.ui.checkBox_list_birth_last.isChecked() and not \
                self.setting_window.ui.checkBox_list_birth_future.isChecked():

            self.ui.label_info_birth_last.hide()
            self.ui.listWidget_birth_last.hide()
            self.ui.label_info_birth_future.hide()
            self.ui.listWidget_birth_future.hide()

            self.setFixedHeight(358)
            self.ui.label_info_birth_now.move(333, 160)
            self.ui.listWidget_birth_now.move(332, 204)
            self.ui.pushButton_exit.move(514, 321)
            self.ui.pushButton_setting.move(418, 321)

        elif self.setting_window.ui.checkBox_list_birth_last.isChecked() and not \
                self.setting_window.ui.checkBox_list_birth_future.isChecked():

            self.ui.label_info_birth_last.show()
            self.ui.listWidget_birth_last.show()
            self.ui.label_info_birth_future.hide()
            self.ui.listWidget_birth_future.hide()

            self.setFixedHeight(420)
            self.ui.label_info_birth_last.move(333, 160)
            self.ui.listWidget_birth_last.move(332, 204)
            self.ui.label_info_birth_now.move(333, 276)
            self.ui.listWidget_birth_now.move(332, 316)
            self.ui.pushButton_exit.move(514, 387)
            self.ui.pushButton_setting.move(418, 387)

        elif not self.setting_window.ui.checkBox_list_birth_last.isChecked() and \
                self.setting_window.ui.checkBox_list_birth_future.isChecked():

            self.ui.label_info_birth_last.hide()
            self.ui.listWidget_birth_last.hide()
            self.ui.label_info_birth_future.show()
            self.ui.listWidget_birth_future.show()

            self.setFixedHeight(420)
            self.ui.label_info_birth_now.move(333, 160)
            self.ui.listWidget_birth_now.move(332, 204)
            self.ui.label_info_birth_future.move(333, 276)
            self.ui.listWidget_birth_future.move(332, 316)
            self.ui.pushButton_exit.move(514, 387)
            self.ui.pushButton_setting.move(418, 387)

        elif self.setting_window.ui.checkBox_list_birth_last.isChecked() and \
                self.setting_window.ui.checkBox_list_birth_future.isChecked():

            self.ui.label_info_birth_last.show()
            self.ui.listWidget_birth_last.show()
            self.ui.label_info_birth_future.show()
            self.ui.listWidget_birth_future.show()

            self.setFixedHeight(540)
            self.ui.label_info_birth_last.move(333, 160)
            self.ui.listWidget_birth_last.move(332, 204)
            self.ui.label_info_birth_now.move(333, 276)
            self.ui.listWidget_birth_now.move(332, 316)
            self.ui.label_info_birth_future.move(333, 390)
            self.ui.listWidget_birth_future.move(332, 430)
            self.ui.pushButton_exit.move(514, 501)
            self.ui.pushButton_setting.move(418, 501)

    def create_file(self):
        self.hide()

        self.create_data_window.setWindowIcon(QIcon(f"{self.path_dir_icons}create.ico"))
        self.create_data_window.show()

        self.create_data_window.ui.pushButton_exit.clicked.connect(self.return_main_with_create_data_window)

    def return_main_with_create_data_window(self):
        self.ui.line_path.setText(self.create_data_window.file_path)
        self.create_data_window.close()
        self.reload_exist()
        self.show_last_and_future_data()
        self.show()

    def update_file(self):
        self.hide()

        self.update_data_window = Update_data(self.file_name, self.path_file)
        self.update_data_window.setWindowIcon(QIcon(f"{self.path_dir_icons}update.ico"))
        self.update_data_window.show()

        self.update_data_window.ui.pushButton_exit.clicked.connect(self.return_main_with_update_data_window)

    def return_main_with_update_data_window(self):
        self.update_data_window.close()
        self.reload_exist()
        self.show_last_and_future_data()
        self.show()

    def setting_win(self):
        self.hide()

        self.setting_window.setWindowIcon(QIcon(f"{self.path_dir_icons}settings.ico"))
        self.setting_window.show()

        self.setting_window.ui.pushButton_exit.clicked.connect(self.return_main_with_setting_window)

    def return_main_with_setting_window(self):
        self.setting_window.close()
        self.change_size_window()
        self.reload_exist()
        self.show_last_and_future_data()
        self.show()

    def reload_exist(self):
        self.path_pulling()
        self.exists_file(self.file_name, self.path_file)
        self.read_with_file(self.file_name, self.path_file)

        self.show_date(self.ui.calendarWidget.selectedDate())

    def path_folder(self):
        path = QFileDialog().getExistingDirectory(self, "Select a folder")
        path = path.replace("/", "\\")
        self.ui.line_path.setText(path)

        self.reload_exist()

    def exists_file(self, file_name, file_path):
        if proverka_file(file_name, file_path):
            self.ui.label_exists_file.setText("Файл знайдено.")
            self.ui.line_path.setText(self.path_file)
            self.ui.pushButton_update_file.setEnabled(True)
            self.ui.pushButton_create_file.setEnabled(False)
            self.ui.label_exists_file.setStyleSheet("color: #00FF00;")
        else:
            self.ui.label_exists_file.setText("Файл не знайдено.")
            self.ui.pushButton_update_file.setEnabled(False)
            self.ui.pushButton_create_file.setEnabled(True)
            self.ui.label_exists_file.setStyleSheet("color: #FF0000;")

    def read_with_file(self, file_name, file_path):
        self.dict_birth = read_file(file_name, file_path)

    def path_pulling(self):
        path_file = self.ui.line_path.text().strip()
        self.path_file = proverka_dir(path_file)
        self.path_cofig = proverka_path_in_config(self.dir_name_config)

    def show_last_and_future_data(self, date_wdg=''):
        if date_wdg != '':
            date = date_wdg
        else:
            date = self.ui.calendarWidget.selectedDate().toString('dd.MM')

        if self.dict_birth:
            all_dates_birth = list(self.dict_birth.keys())

            all_dates_birth.append(date)

            all_dates_birth = list(set(all_dates_birth))

            sorted_all_dates = sort_data(all_dates_birth)

            index_date_now = sorted_all_dates.index(date)

            if self.setting_window.ui.checkBox_list_birth_last.isChecked():
                if index_date_now - 1 >= 0:
                    past_date = sorted_all_dates[index_date_now - 1]
                else:
                    past_date = sorted_all_dates[sorted_all_dates.index(sorted_all_dates[-1])]

                birth_list_last = self.dict_birth.get(past_date, [])

                if birth_list_last:
                    self.ui.listWidget_birth_last.clear()
                    self.ui.label_info_birth_last.setText(f"{past_date}\nсвяткував День Народження.")
                    self.ui.listWidget_birth_last.addItems(birth_list_last)
                else:
                    self.ui.listWidget_birth_last.clear()
                    self.ui.label_info_birth_last.setText('Даних немає')

            if self.setting_window.ui.checkBox_list_birth_future.isChecked():
                if index_date_now + 1 <= len(sorted_all_dates) - 1:
                    future_date = sorted_all_dates[index_date_now + 1]
                else:
                    future_date = sorted_all_dates[0]

                birth_list_future = self.dict_birth.get(future_date, [])

                if birth_list_future:
                    self.ui.listWidget_birth_future.clear()
                    self.ui.label_info_birth_future.setText(f"{future_date}\nсвяткуватиме День Народження.")
                    self.ui.listWidget_birth_future.addItems(birth_list_future)
                else:
                    self.ui.listWidget_birth_future.clear()
                    self.ui.label_info_birth_future.setText('Даних немає')

    def push_notifications(self):
        date = self.ui.calendarWidget.selectedDate().toString('dd.MM')
        birth_list = self.dict_birth.get(date, [])

        self.show_last_and_future_data()

        if birth_list:
            self.show_date(date)

            self.showNormal()
            
            if len(birth_list) == 1:
                self.push_notification.show_toast(self.dir_name_config, f"У {birth_list[0]} сьогодні День Народження! Не забудь привітати, тобі займе кілька хвилин, а йому (їй) буде приємно :)",
                                                   duration = 120, icon_path = f"{self.path_dir_icons}birth.ico", threaded=True)
            else:
                self.push_notification.show_toast(self.dir_name_config, "У твоїх друзів сьогодні День Народження! Не забудь привітати, тобі займе кілька хвилин, а їм буде приємно :)",
                                                   duration = 120, icon_path = f"{self.path_dir_icons}birth.ico", threaded=True)
        else:
            self.ui.groupBox_3.show()
            self.timer.start(1000)
            self.change_size_window()

    def btn_clear_path(self):
        self.ui.line_path.setText('')
        self.reload_exist()
        self.show_last_and_future_data()

    def show_date_select_wdg(self, date_wdg):
        self.ui.listWidget_birth_now.clear()
        date = date_wdg.toString('dd.MM')

        self.ui.label_info_birth_now.setText(f"{date}\nвідзначає День Народження.")
        self.ui.listWidget_birth_now.addItems(self.dict_birth.get(date, []))

        self.show_last_and_future_data(date)

    def show_date(self, date_get):
        self.ui.listWidget_birth_now.clear()

        if isinstance(date_get, str):
            date = date_get
        else:
            date = date_get.toString('dd.MM')

        self.ui.label_info_birth_now.setText(f"{date}\nвідзначає День Народження.")
        self.ui.listWidget_birth_now.addItems(self.dict_birth.get(date, []))

    def read_config(self):
        data_config = read_file(self.name_file_config, self.path_cofig)

        if data_config:
            self.checked_checkbox_autorun = data_config.get('checkbox_autorun')
            self.checked_checkbox_collapse_window = data_config.get('checkbox_collapse_window')
            self.checked_checkbox_list_birth_last = data_config.get('checkbox_list_birth_last')
            self.checked_checkbox_list_birth_future = data_config.get('checkbox_list_birth_future')
            file_path = data_config.get('path_file')
            self.path_dir_icons = data_config.get('path_dir_icons')
            self.spinbox_min, self.spinbox_sec = data_config.get('timer_time')

            self.all_sec = self.spinbox_min * 60 + self.spinbox_sec

            self.ui.line_path.setText(file_path)
            self.reload_exist()

    def data_capture_for_config(self):
        data_config = {}

        data_config['checkbox_autorun'] = self.setting_window.ui.checkBox_autorun.isChecked()
        data_config['checkbox_collapse_window'] = self.setting_window.ui.checkBox_collapse_window.isChecked()
        data_config['path_file'] = self.path_file[:self.path_file.rindex("\\")]
        data_config['path_dir_icons'] = self.path_dir_icons
        data_config['checkbox_list_birth_last'] = self.setting_window.ui.checkBox_list_birth_last.isChecked()
        data_config['checkbox_list_birth_future'] = self.setting_window.ui.checkBox_list_birth_future.isChecked()
        data_config['timer_time'] = [self.setting_window.ui.spinBox_minutes.value(), self.setting_window.ui.spinBox_seconds.value()]
        
        return data_config

    def run_app_in_collapse(self):
        if self.setting_window.ui.checkBox_collapse_window.isChecked():
            self.showMinimized()

            self.push_notifications()

    def tray_gui(self):
        show_action = QAction("Показати", self)
        show_action.triggered.connect(self.show)
        
        hide_action = QAction("Сховати", self)
        hide_action.triggered.connect(self.hide)

        exit_action = QAction("Вийти", self)
        exit_action.triggered.connect(self.exit_app)

        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(exit_action)

        self.tray_icon.setToolTip(self.dir_name_config)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.activated.connect(self.restore_window)
        
    def restore_window(self, reason):
        if reason != self.isHidden():   
            self.tray_icon.hide()
            self.show()
        else:
            self.tray_icon.show()        
            self.hide()

    def closeEvent(self, event): 
        answ = self.show_question()
        event.ignore()

        if answ == "yes":
            self.tray_icon.show()
            self.hide()

            self.tray_icon.showMessage(
                self.dir_name_config, "Додаток згорнутий в трей.",
                QSystemTrayIcon.MessageIcon.Information, 
                1000)
            
        elif answ == "close":
            self.exit_app()

    def btn_app_exit(self):
        answ = self.show_question()
        
        if answ == "yes":
            self.tray_icon.show()
            self.hide()

            self.tray_icon.showMessage(self.dir_name_config, "Додаток згорнутий в трей.",
                QSystemTrayIcon.MessageIcon.Information, 
                1000)
        elif answ == "close":
            self.exit_app()

    def exit_app(self):
        write_file(self.data_capture_for_config(), self.name_file_config, self.path_cofig)
        QApplication.instance().quit
        exit()

    def show_question(self):
        question = QMessageBox()
        question.setWindowTitle("Question")
        question.setText("Додаток згорнути в трей?")
        question.setIcon(QMessageBox.Icon.Question)
        question.setWindowFlags(Qt.WindowType.CoverWindow)
        question.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.Close)
        btn = question.exec()

        if btn == QMessageBox.StandardButton.Yes:
            return "yes"
        elif btn == QMessageBox.StandardButton.Close:
            return "close"
            
    def show_FAQ_path(self):
        self.msg("Information", "Якщо файл створено, але не знаходиться поруч із додатком.\nНатисніть \"...\", щоб вказати папку, де лежить файл (при виборі папки файли в ній не відображаються).")

    def msg(self, reson, message):
        msg = QMessageBox()
        if reson == "Error": 
            msg.setWindowTitle(reson)
            msg.setText(message)
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setWindowFlags(Qt.WindowType.CoverWindow)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()

        elif reson == "Information":
            msg.setWindowTitle(reson)
            msg.setText(message)
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setWindowFlags(Qt.WindowType.CoverWindow)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()

        else:
            msg.setWindowTitle(reson)
            msg.setText(message)
            msg.setIcon(QMessageBox.Icon.NoIcon)
            msg.setWindowFlags(Qt.WindowType.CoverWindow)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()