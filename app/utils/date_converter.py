from jalali_calendar import JalaliDateTime

def Today():
    dt = JalaliDateTime.now()
    return dt.strftime('%Y/%m/%d')