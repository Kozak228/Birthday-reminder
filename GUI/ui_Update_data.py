# Form implementation generated from reading ui file 'd:\Проги python\Напоминание о ДР\GUI\Update_data.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(591, 350)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\Проги python\\Напоминание о ДР\\GUI\\../Icons for app Birthday reminder/update.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget{\n"
"    background-color: #1E1E1E;\n"
"}\n"
"QPushButton{\n"
"    background-color: black;\n"
"    color: yellow;\n"
"    border: 1px solid #483D8B;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px dashed #00FA9A;\n"
"    color: #00FA9A;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #2F4F4F;\n"
"    color: #FF0000;\n"
"    border: 1px dashed #000080;\n"
"}\n"
"QPushButton:disabled{\n"
"    background-color: black;\n"
"    color: #800000;\n"
"    border: none;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    background-color: #DCDCDC;\n"
"    color:     #000080;\n"
"    border: 1px solid yellow; \n"
"}\n"
"QLineEdit:focus{\n"
"    border: 3px dashed #800000;\n"
"}\n"
"QLabel{\n"
"    color: #FF4500;\n"
"}\n"
"QGroupBox{\n"
"    backgrond-color: #696969;\n"
"    color: #7FFF00;\n"
"    border: 1px solid #0000CD;\n"
"}\n"
"QRadioButton{\n"
"    color: #FF4500;\n"
"}\n"
"QRadioButton:hover{\n"
"    color: #00FF00;\n"
"}\n"
"QTableWidget {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 black, stop:1 blue);\n"
"    border: 2px solid #FF4500;\n"
"    color: yellow;\n"
"}\n"
"QTableWidget::item {\n"
"    border: 5px solid rgba(68, 119, 170, 150);\n"
"    background-color:rgba(68, 119, 170, 125);\n"
"}\n"
"\n"
"QHeaderView, QHeaderView::section {\n"
"    background-color: rgba(128, 128, 128, 128);\n"
"    color: #00CED1;\n"
"}\n"
"QTableWidget::item:hover {\n"
"    border: 2px dashed #00FA9A;\n"
"    color: #00FA9A;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(7, 10, 201, 192))
        self.tableWidget.setMidLineWidth(1)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(213, 10, 206, 58))
        self.groupBox.setObjectName("groupBox")
        self.line_path = QtWidgets.QLineEdit(self.groupBox)
        self.line_path.setGeometry(QtCore.QRect(10, 20, 191, 31))
        self.line_path.setReadOnly(True)
        self.line_path.setObjectName("line_path")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(215, 80, 226, 136))
        self.groupBox_2.setObjectName("groupBox_2")
        self.line_date = QtWidgets.QLineEdit(self.groupBox_2)
        self.line_date.setGeometry(QtCore.QRect(10, 20, 61, 31))
        self.line_date.setInputMask("")
        self.line_date.setMaxLength(5)
        self.line_date.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.line_date.setClearButtonEnabled(False)
        self.line_date.setObjectName("line_date")
        self.pushButton_FAQ_date = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_FAQ_date.setGeometry(QtCore.QRect(80, 20, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_FAQ_date.setFont(font)
        self.pushButton_FAQ_date.setObjectName("pushButton_FAQ_date")
        self.pushButton_load_data = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_load_data.setGeometry(QtCore.QRect(120, 20, 101, 31))
        self.pushButton_load_data.setObjectName("pushButton_load_data")
        self.label_info_names_in_date = QtWidgets.QLabel(self.groupBox_2)
        self.label_info_names_in_date.setGeometry(QtCore.QRect(10, 60, 101, 71))
        self.label_info_names_in_date.setStyleSheet("color: #00FA9A;")
        self.label_info_names_in_date.setText("")
        self.label_info_names_in_date.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_info_names_in_date.setWordWrap(True)
        self.label_info_names_in_date.setObjectName("label_info_names_in_date")
        self.pushButton_clear_date = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_clear_date.setGeometry(QtCore.QRect(120, 60, 101, 31))
        self.pushButton_clear_date.setObjectName("pushButton_clear_date")
        self.pushButton_clear_date_in_data = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_clear_date_in_data.setGeometry(QtCore.QRect(120, 100, 101, 31))
        self.pushButton_clear_date_in_data.setObjectName("pushButton_clear_date_in_data")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(7, 220, 417, 127))
        self.groupBox_3.setObjectName("groupBox_3")
        self.line_name = QtWidgets.QLineEdit(self.groupBox_3)
        self.line_name.setGeometry(QtCore.QRect(10, 20, 181, 31))
        self.line_name.setObjectName("line_name")
        self.pushButton_FAQ_name = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_FAQ_name.setGeometry(QtCore.QRect(195, 20, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_FAQ_name.setFont(font)
        self.pushButton_FAQ_name.setObjectName("pushButton_FAQ_name")
        self.pushButton_clear_name = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_clear_name.setGeometry(QtCore.QRect(10, 90, 81, 31))
        self.pushButton_clear_name.setObjectName("pushButton_clear_name")
        self.pushButton_update_in_list = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_update_in_list.setGeometry(QtCore.QRect(114, 90, 111, 31))
        self.pushButton_update_in_list.setObjectName("pushButton_update_in_list")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_2.setGeometry(QtCore.QRect(241, 54, 131, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton.setGeometry(QtCore.QRect(241, 10, 121, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_3.setGeometry(QtCore.QRect(241, 98, 131, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.pushButton_FAQ_replace_data = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_FAQ_replace_data.setGeometry(QtCore.QRect(382, 5, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_FAQ_replace_data.setFont(font)
        self.pushButton_FAQ_replace_data.setObjectName("pushButton_FAQ_replace_data")
        self.pushButton_FAQ_add_data = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_FAQ_add_data.setGeometry(QtCore.QRect(382, 50, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_FAQ_add_data.setFont(font)
        self.pushButton_FAQ_add_data.setObjectName("pushButton_FAQ_add_data")
        self.pushButton_FAQ_remove_data = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_FAQ_remove_data.setGeometry(QtCore.QRect(382, 93, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_FAQ_remove_data.setFont(font)
        self.pushButton_FAQ_remove_data.setObjectName("pushButton_FAQ_remove_data")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(533, 315, 55, 31))
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.pushButton_add_in_dict = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add_in_dict.setGeometry(QtCore.QRect(434, 314, 79, 31))
        self.pushButton_add_in_dict.setObjectName("pushButton_add_in_dict")
        self.label_info_date_in_file = QtWidgets.QLabel(self.centralwidget)
        self.label_info_date_in_file.setGeometry(QtCore.QRect(430, 233, 152, 59))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_info_date_in_file.setFont(font)
        self.label_info_date_in_file.setStyleSheet("color: #00FA9A;")
        self.label_info_date_in_file.setText("")
        self.label_info_date_in_file.setWordWrap(True)
        self.label_info_date_in_file.setObjectName("label_info_date_in_file")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_clear_name.clicked.connect(self.line_name.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Update data"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ім\'я"))
        self.groupBox.setTitle(_translate("MainWindow", "Шлях до файлу"))
        self.line_path.setPlaceholderText(_translate("MainWindow", "Шлях..."))
        self.groupBox_2.setTitle(_translate("MainWindow", "Введення дати народження"))
        self.line_date.setPlaceholderText(_translate("MainWindow", "02.12"))
        self.pushButton_FAQ_date.setText(_translate("MainWindow", "?"))
        self.pushButton_load_data.setText(_translate("MainWindow", "Перевірити дату"))
        self.pushButton_clear_date.setText(_translate("MainWindow", "Очистити поле"))
        self.pushButton_clear_date_in_data.setText(_translate("MainWindow", "Видалити дані"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Дії над даними"))
        self.line_name.setPlaceholderText(_translate("MainWindow", "Ім\'я...."))
        self.pushButton_FAQ_name.setText(_translate("MainWindow", "?"))
        self.pushButton_clear_name.setText(_translate("MainWindow", "Очистити"))
        self.pushButton_update_in_list.setText(_translate("MainWindow", "Оновити у списку"))
        self.radioButton_2.setText(_translate("MainWindow", "Додавання даних"))
        self.radioButton.setText(_translate("MainWindow", "Заміна даних"))
        self.radioButton_3.setText(_translate("MainWindow", "Видалення даних"))
        self.pushButton_FAQ_replace_data.setText(_translate("MainWindow", "?"))
        self.pushButton_FAQ_add_data.setText(_translate("MainWindow", "?"))
        self.pushButton_FAQ_remove_data.setText(_translate("MainWindow", "?"))
        self.pushButton_exit.setText(_translate("MainWindow", "Закрити"))
        self.pushButton_add_in_dict.setText(_translate("MainWindow", "Зберегти дані"))
