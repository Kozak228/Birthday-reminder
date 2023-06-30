from logging import basicConfig, exception

from Proverka import proverka_path_in_config

def log_error(msg_error):
    basicConfig(filename='log_errors.log', path=proverka_path_in_config("Birthday reminder", True), format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%d.%m.%Y %I:%M:%S',
                encoding='utf8')

    exception(msg_error)