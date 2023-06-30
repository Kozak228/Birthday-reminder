from json import loads

from Loging_error import log_error

def read_file(file_name, file_path):
    try:
        with open(f'{file_path}{file_name}.json') as f:
            slovar = loads(f.read())

        return slovar

    except FileNotFoundError:
        return {}
    except Exception as ex:
        log_error(ex)

def read_config(file_name, file_path):
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
        log_error(ex)