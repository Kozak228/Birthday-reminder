from json import dump

from Sorted import sort_dict
from Loging_error import log_error

def write_file(dicts, file_name, file_path):
    sorted_dicts = sort_dict(dicts)

    try:
        with open(f'{file_path}{file_name}.json', 'w', encoding='utf8') as f:
            dump(sorted_dicts, f, indent=4, ensure_ascii=False)
    except Exception as ex:
        log_error(ex)

def write_config(info, file_name, file_path):
    try:
        with open(f'{file_path}{file_name}.ini', 'w', encoding='utf8') as f:
            f.writelines("%s\n" % i for i in info)
    except Exception as ex:
        log_error(ex)