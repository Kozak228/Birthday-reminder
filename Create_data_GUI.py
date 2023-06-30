from GUI.ui_Create_data import Ui_MainWindow
from PyQt6.QtWidgets import QMessageBox, QMainWindow, QFileDialog, QTableWidgetItem
from PyQt6.QtCore import Qt

from time import strptime

from Time_date_format import date_optimization
from Proverka import proverka_dir
from Write_file import write_file

class Create_data(QMainWindow):
    def __init__(self, file_name):
        super(Create_data, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.dict_birth = {}
        self.file_name = file_name

        self.setWindowFlags(Qt.WindowType.WindowSystemMenuHint)
        self.setFixedSize(465, 320)

        self.ui.pushButton_clear_path.setEnabled(False)
        self.ui.pushButton_clear_name.setEnabled(False)
        self.ui.pushButton_clear_date.setEnabled(False)
        self.ui.pushButton_add_in_list.setEnabled(False)
        self.ui.pushButton_proverk_date.setEnabled(False)
        self.ui.line_name.setEnabled(False)

        self.ui.pushButton_proverk_date.clicked.connect(self.proverk_date)
        self.ui.pushButton_add_in_list.clicked.connect(self.add_in_list)
        self.ui.pushButton_add_in_dict.clicked.connect(self.save_dict_in_file)
        self.ui.pushButton_path_dir.clicked.connect(self.path_folder)
        self.ui.pushButton_clear_date.clicked.connect(self.btn_clear_date_in_line)
        self.ui.pushButton_FAQ_path.clicked.connect(self.show_FAQ_path)
        self.ui.pushButton_FAQ_name.clicked.connect(self.show_FAQ_name)
        self.ui.pushButton_FAQ_date.clicked.connect(self.show_FAQ_date)

        self.ui.line_path.textChanged.connect(lambda text: self.ui.pushButton_clear_path.setEnabled(bool(text)))
        self.ui.line_name.textChanged.connect(lambda text: self.ui.pushButton_clear_name.setEnabled(bool(text)))
        self.ui.line_name.textChanged.connect(lambda text: self.ui.pushButton_add_in_list.setEnabled(bool(text)))
        self.ui.line_date.textChanged.connect(lambda text: self.ui.pushButton_clear_date.setEnabled(bool(text)))
        self.ui.line_date.textChanged.connect(lambda text: self.ui.pushButton_proverk_date.setEnabled(bool(text)))

        self.file_path = proverka_dir(self.ui.line_path.text())

    def save_dict_in_file(self):
        path_dir = self.ui.line_path.text().strip()

        self.file_path = proverka_dir(path_dir)
        write_file(self.dict_birth, self.file_name, self.file_path)

        self.msg("Information", f"Файл збережено! Запам'ятайте розташування\n{self.file_path}{self.file_name}.json.")

    def info_add_in_file(self):
        keys = list(self.dict_birth.keys())
        values = list(self.dict_birth.values())

        kol_date = len(keys)
        kol_zapis = sum([len(i) for i in values])

        self.ui.label_info_add_in_file.setText(f"Кількість дат додано: {kol_date};\
                                               \nКількість записів: {kol_zapis}.")

    def add_in_list(self):
        flag_date = self.proverk_date()
        name = self.ui.line_name.text()

        if name == "":
            self.msg("Error", "Поле має бути заповнено.")
            self.ui.line_name.setStyleSheet("border: 2px solid red;")
            flag_name = False
        else:
            flag_name = True
            self.ui.line_name.setStyleSheet("border: 1px solid yellow;")

        if flag_date and flag_name:
            list_birth = self.dict_birth.get(self.date, [])
            list_birth.append(name)
            self.dict_birth[self.date] = list_birth
            self.addItems_in_table(list_birth)
            self.ui.line_name.setText("")

            self.info_add_in_file()

    def addItems_in_table(self, items):
        self.ui.tableWidget.setRowCount(len(items))
                                        
        for row, val in enumerate(items):
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(val))

    def btn_clear_date_in_line(self):
        self.ui.line_date.setText("")
        self.ui.line_name.setText("")
        self.ui.line_name.setEnabled(False) 

    def proverk_date(self):
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
                self.ui.line_name.setFocus()
                self.ui.tableWidget.setRowCount(0)
                return flag

            except:
                self.msg("Error", "Невірний формат дати.")
                flag = False
                self.ui.line_date.setText("")
                self.ui.line_name.setEnabled(False)
                return flag
                
    def path_folder(self):
        path = QFileDialog.getExistingDirectory(self, "Select a folder")
        path = path.replace("/", "\\")
        self.ui.line_path.setText(path)

    def show_FAQ_name(self):
        self.msg("Information", "Щоб розблокувати поле, введіть дату та натисніть 'Перевірити дату'.\
                 \n\nПісля введення імені ви можете:\
                 \n\n'Додати до списку' - додавання імені до списку на вибрану дату.\
                 \nЩоб ввести дані на іншу дату, змініть її у відповідному полі та натисніть 'Перевірити дату'.\
                 \nДані, введені раніше, не пропадуть до закриття вікна.\
                 \n\n'Зберегти дані' - список даних записується у файл.")

    def show_FAQ_date(self):
        self.msg("Information", "Потрібно ввести день та місяць народження та натисніть 'Перевірити дату', щоб дані записувалися на дату, зазначену в полі.")

    def show_FAQ_path(self):
        self.msg("Information", "Щоб зберегти файл, натисніть '...', щоб вказати папку, де зберегти файл (при виборі папки файли в ній не відображаються).\
                 \n\nЯкщо поле залишити порожнім, файл з'явиться біля додатку.")

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