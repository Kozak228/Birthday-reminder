from GUI.ui_Update_data import Ui_MainWindow
from PyQt6.QtWidgets import QMessageBox, QMainWindow, QTableWidgetItem
from PyQt6.QtCore import Qt

from time import strptime

from Time_date_format import date_optimization
from Proverka import proverka_dir
from Write_file import write_file
from Read_file import read_file

class Update_data(QMainWindow):
    def __init__(self, file_name, file_path):
        super(Update_data, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.file_name = file_name
        self.file_path = file_path

        self.setWindowFlags(Qt.WindowType.WindowSystemMenuHint)
        self.setFixedSize(591, 350)

        self.ui.pushButton_clear_name.setEnabled(False)
        self.ui.pushButton_clear_date.setEnabled(False)
        self.ui.pushButton_update_in_list.setEnabled(False)
        self.ui.pushButton_load_data.setEnabled(False)
        self.ui.pushButton_clear_date_in_data.setEnabled(False)
        self.ui.line_name.setEnabled(False)
        self.ui.line_name.setReadOnly(True)

        self.ui.tableWidget.clicked.connect(self.table_value)
        self.ui.pushButton_load_data.clicked.connect(self.load_info_in_date)
        self.ui.pushButton_update_in_list.clicked.connect(self.add_in_list)
        self.ui.pushButton_add_in_dict.clicked.connect(self.save_dict_in_file)
        self.ui.pushButton_clear_date_in_data.clicked.connect(self.clear_date_in_data)
        self.ui.pushButton_FAQ_name.clicked.connect(self.show_FAQ_name)
        self.ui.pushButton_FAQ_date.clicked.connect(self.show_FAQ_date)
        self.ui.pushButton_FAQ_replace_data.clicked.connect(self.show_FAQ_replace_data)
        self.ui.pushButton_FAQ_add_data.clicked.connect(self.show_FAQ_add_data)
        self.ui.pushButton_FAQ_remove_data.clicked.connect(self.show_FAQ_remove_data)
        self.ui.pushButton_clear_date.clicked.connect(self.btn_clear_date_in_line)

        self.ui.radioButton.toggled.connect(lambda: self.btn_state(self.ui.radioButton))
        self.ui.radioButton_2.toggled.connect(lambda: self.btn_state(self.ui.radioButton_2))
        self.ui.radioButton_3.toggled.connect(lambda: self.btn_state(self.ui.radioButton_3))

        self.ui.line_name.textChanged.connect(lambda text: self.ui.pushButton_clear_name.setEnabled(bool(text)))
        self.ui.line_name.textChanged.connect(lambda text: self.ui.pushButton_update_in_list.setEnabled(bool(text)))
        self.ui.line_date.textChanged.connect(lambda text: self.ui.pushButton_clear_date.setEnabled(bool(text)))
        self.ui.line_date.textChanged.connect(lambda text: self.ui.pushButton_load_data.setEnabled(bool(text)))
        
        self.read_data_with_file()
        self.load_info_date_in_file()

        self.ui.line_path.setText(self.file_path)

    def save_dict_in_file(self):
        path_dir = self.ui.line_path.text().strip()

        self.file_path = proverka_dir(path_dir)
        write_file(self.dict_birth, self.file_name, self.file_path)

        self.msg("Information", "Дані оновлені.")

    def read_data_with_file(self):
        self.dict_birth = read_file(self.file_name, self.file_path)

    def clear_date_in_data(self):
        self.dict_birth.pop(self.date)

        self.load_info_in_date()
        self.msg("Information", f"Дані на {self.date} видалені.\
                 \n\nНе забудьте зберегти дані!")
        
        self.load_info_date_in_file()
        self.ui.tableWidget.setRowCount(0)
        
    def add_in_list(self):
        flag_date = self.date_pulling()
        name = self.ui.line_name.text()

        if name == "":
            self.msg("Error", "Поле має бути заповнено.")
            flag_name = False
            self.ui.line_name.setStyleSheet("border: 2px solid red;")
        else:
            self.ui.line_name.setStyleSheet("border: 1px solid yellow;")
            flag_name = True

        if flag_date and flag_name:
            if self.ui.radioButton.isChecked():
                list_birth = self.dict_birth.get(self.date, [])
                list_birth[self.row] = name
                self.dict_birth[self.date] = list_birth
            
            if self.ui.radioButton_2.isChecked():
                list_birth = self.dict_birth.get(self.date, [])
                list_birth.append(name)
                self.dict_birth[self.date] = list_birth

                self.load_info_date_in_file()

            if self.ui.radioButton_3.isChecked():
                list_birth = self.dict_birth.get(self.date, [])
                list_birth.pop(self.row)
                self.dict_birth[self.date] = list_birth

            self.addItems_in_table(list_birth)
            self.ui.line_name.setText("")

    def addItems_in_table(self, items):
        self.ui.tableWidget.setRowCount(len(items))
                                        
        for row, val in enumerate(items):
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(val))

    def load_info_in_date(self):
        flag = self.date_pulling()

        if flag:
            list_birth = self.dict_birth.get(self.date, [])
            self.ui.label_info_names_in_date.setText(f"Кількість записів: {str(len(list_birth))}")
            self.addItems_in_table(list_birth)

    def load_info_date_in_file(self):
        keys = list(self.dict_birth.keys())
        values = list(self.dict_birth.values())

        kol_date = len(keys)
        kol_zapis = sum([len(i) for i in values])

        self.ui.label_info_date_in_file.setText(f"Кількість дат зчитаних з файлу: {kol_date};\
                                                \nКількість записів зчитаних з файлу: {kol_zapis}.")

    def btn_clear_date_in_line(self):
        self.ui.line_date.setText("")
        self.ui.pushButton_clear_date_in_data.setEnabled(False)
        self.ui.line_name.setText("")
        self.ui.line_name.setEnabled(False)

    def date_pulling(self):
        date = self.ui.line_date.text()

        if date == "":
            self.msg("Error", "Поле має бути заповнено.")
            self.ui.line_date.setStyleSheet("border: 2px solid red;")
        else:
            self.ui.line_date.setStyleSheet("border: 1px solid yellow;")

            try:
                date = date.strip().replace(",", ".")
                self.date = date_optimization(date)

                self.ui.line_date.setText(self.date)

                valid_date = strptime(self.date, '%d.%m')
                flag = True
                self.ui.line_name.setEnabled(True)
                self.ui.pushButton_clear_date_in_data.setEnabled(True)
                self.ui.line_name.setFocus()
                return flag

            except:
                self.msg("Error", "Невірний формат дати.")
                flag = False
                self.ui.line_name.setEnabled(False)
                self.ui.pushButton_clear_date_in_data.setEnabled(False)
                return flag

    def table_value(self):
        for i in self.ui.tableWidget.selectedItems():
            if i.column() == 0:
                self.row = i.row()
                self.ui.line_name.setText(i.text())
                self.ui.line_name.setReadOnly(False)

    def btn_state(self, b):
        if b.isChecked() and b.objectName() == "radioButton":
            self.ui.pushButton_update_in_list.setText("Оновити у списку") 

        if b.isChecked() and b.objectName() == "radioButton_2":
            self.ui.pushButton_update_in_list.setText("Додати до списку")
            self.ui.line_name.setFocus()
            self.ui.line_name.setReadOnly(False)
            
        if b.isChecked() and b.objectName() == "radioButton_3":
            self.ui.pushButton_update_in_list.setText("Видалити зі списку") 

    def show_FAQ_name(self):
        self.msg("Information", "Щоб розблокувати поле, введіть дату та натисніть 'Перевірити дату'.\
                 \nЩоб оновити дані на іншу дату, змініть її у відповідному полі та натисніть 'Перевірити дату'.\
                 \nДані, введені раніше, не пропадуть до закриття вікна.\
                 \n\nПісля роботи з оновленням даних не забудьте зберегти!")

    def show_FAQ_replace_data(self):
        self.msg("Information", "Заміняє існуючі дані у списку, натисніть відповідну комірку таблиці, щоб оновити дані.")
        
    def show_FAQ_add_data(self):
        self.msg("Information", "Додає нову запис до списку.")
        
    def show_FAQ_remove_data(self):
        self.msg("Information", "Видаляє існуючі дані у списку, натисніть відповідну комірку таблиці.")

    def show_FAQ_date(self):
        self.msg("Information", "Потрібно ввести день та місяць народження та натисніть 'Перевірити дату', щоб дії над даними здійснювалися на дату, зазначену в полі.\
                 \n\nЩоб очистити дані за датою, після перевірки дати натисніть 'Видалити дані'.")

    def msg(self, reson, message):
        msg = QMessageBox()
        if reson == "Error": 
            msg.setWindowTitle(reson)
            msg.setText(message)
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setWindowFlags(Qt.WindowType.CoverWindow)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()

        if reson == "Information":
            msg.setWindowTitle(reson)
            msg.setText(message)
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setWindowFlags(Qt.WindowType.CoverWindow)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()