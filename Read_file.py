from json import loads

from logging import getLogger

def read_file(file_name, file_path):
    logger = getLogger('app.read_file')

    try:
        with open(f'{file_path}{file_name}.json') as f:
            slovar = loads(f.read())

        return slovar
    except FileNotFoundError:
        return {}
    except Exception as ex:
        logger.error(ex)