from sys import exit, argv

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QSystemSemaphore, QSharedMemory

from win10toast import ToastNotifier

from Main_GUI import MainWindow
from Proverka import proverka_path_in_icons_dir, proverka_path_in_config
from Read_file import read_config

def read_path_dir_icon():
    path_config_isexists = proverka_path_in_config("Birthday reminder", True)

    if path_config_isexists:
        path_dir_icon = read_config("Config", proverka_path_in_config("Birthday reminder"))[3]
    else:
        path_dir_icon = proverka_path_in_icons_dir()

    return path_dir_icon

def main():
    app = QApplication(argv)    

    semaphore = QSystemSemaphore("<uniq id>", 1) 
    semaphore.acquire() 

    nix_fix_shared_memory = QSharedMemory("<uniq id 2>")
    if nix_fix_shared_memory.attach():
        nix_fix_shared_memory.detach()

    sharedMemory = QSharedMemory("<uniq id 2>") 
    is_running = False 

    if sharedMemory.attach():
        is_running = True
    else:
        sharedMemory.create(1)
        is_running = False
        
    semaphore.release()

    if is_running:
        push_notification = ToastNotifier()
        push_notification.show_toast("Birthday reminder", "Додаток запущен, перевір панель завдань або трей.", duration = 10, 
                                     icon_path = f"{read_path_dir_icon()}birth.ico")
        exit()

    appl = MainWindow()
    appl.show()

    exit(app.exec())

if __name__ == '__main__':
    main()