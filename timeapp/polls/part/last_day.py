from datetime import date, datetime, timedelta
data = datetime(2022,5,31, 20, 30, 00)
data_now = datetime.now()

#print(data_now.strftime("%H:%M:%S"))
#print(data.time())
def last_day_of_month(any_day):
    # this will never fail
    # get close to the end of the month for any day, and add 4 days 'over'
    next_month = any_day.replace(day=28) + timedelta(days=4)
    # subtract the number of remaining 'overage' days to get last day of current month, or said programattically said, the previous day of the first of next month
    return next_month - timedelta(days=next_month.day)

def add_total():
    for month in range(1, 13):
        if data.date() == last_day_of_month(date(2022, month, 1)):
            if data_now.strftime("%H:%M:%S") == data.time():
                return True
            
