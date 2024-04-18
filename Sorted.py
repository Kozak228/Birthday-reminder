from datetime import datetime

def sort_data(data, type_data='list'):
    if type_data == 'dict':
        sorted_tuple = sorted(data.items(), key=lambda x: datetime.strptime(x[0], "%d.%m"))
        return dict(sorted_tuple)

    else:
        sorted_list = sorted(data, key=lambda x: datetime.strptime(x, "%d.%m"))
        return sorted_list