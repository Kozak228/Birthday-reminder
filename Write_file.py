from json import dump
from logging import getLogger

from Sorted import sort_dict

def write_file(dicts, file_name, file_path):
    logger = getLogger('app.write_file')
    sorted_dicts = sort_dict(dicts)

    try:
        with open(f'{file_path}{file_name}.json', 'w') as f:
            dump(sorted_dicts, f, indent=4, ensure_ascii=False)
    except Exception as ex:
        logger.error(ex)

def write_config(info, file_name, file_path):
    logger = getLogger('app.write_file')

    try:
        with open(f'{file_path}{file_name}.ini', 'w', encoding='utf8') as f:
            f.writelines("%s\n" % i for i in info)
    except Exception as ex:
        logger.error(ex)