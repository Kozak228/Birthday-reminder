from json import dump
from logging import getLogger

def write_file(dicts, file_name, file_path):
    logger = getLogger('app.write_file')

    try:
        with open(f'{file_path}{file_name}.json', 'w') as f:
            dump(dicts, f, indent=4, ensure_ascii=False)
    except Exception as ex:
        logger.error(ex)