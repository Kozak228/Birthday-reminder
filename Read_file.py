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

def read_config(file_name, file_path):
    logger = getLogger('app.read_file')
    data = []

    try:
        with open(f'{file_path}{file_name}.ini') as f:
            info = f.readlines()

            for line in info:
                current_data = line[:-1]

                data.append(current_data)

        return data

    except FileNotFoundError:
        return []
    except Exception as ex:
        logger.error(ex)