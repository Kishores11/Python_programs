from datetime import datetime
from dateutil import relativedelta


def difference(x,y):
    delta = relativedelta.relativedelta(x,y)
    years = delta.years
    
    if years > 18:
        return 1
    else:
        return 0


def start():
    d1 = '14/1/2000'
    d2 = '16/1/2015'

    # convert string to date object
    start_date = datetime.strptime(d1, "%d/%m/%Y")
    end_date = datetime.strptime(d2, "%d/%m/%Y")
    message = difference(end_date,start_date)
    print(message)


start()