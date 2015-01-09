def is_leap_year(year=None):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


month_array = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


def cal_day_offset(year=None, month=None, day=None):
    total_days = 0
    # cal days before "year"
    for y in range(1900, year):
        for i in range(1, 13):
            total_days += month_array[i]
        if is_leap_year(y):
            total_days += 1

    # cal days for this "year"
    for i in range(1, month):
        total_days += month_array[i]
    if is_leap_year(year) and month > 2:
        total_days += 1

    total_days += day - 1
    return total_days % 7


def cal_day_in_week():
    total_sunday = 0
    for y in range(1901, 2001):
        for m in range(1, 13):
            if cal_day_offset(y, m, 1) == 6:
                total_sunday += 1
                print y, m
    return total_sunday


print cal_day_in_week()
print cal_day_offset(2015, 1, 9)



