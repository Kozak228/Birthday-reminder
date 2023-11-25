def add_zero(num_in_str):
    num = int(num_in_str)

    return f"0{num}" if num < 10 else num

def s_in_m_s(all_time):
    s = all_time % 60
    m = (all_time // 60) % 60

    return s, m

def date_optimization(date):
    day, month = date[:date.index(".")], date[date.rindex(".") + 1:]

    return f"{add_zero(day)}.{add_zero(month)}"