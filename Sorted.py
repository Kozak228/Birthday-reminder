from datetime import datetime

def sort_dict(dicts):
    sorted_tuple = sorted(dicts.items(), key=lambda x: datetime.strptime(x[0], "%d.%m"))
    return dict(sorted_tuple)