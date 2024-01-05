import calendar

day = int(input('Enter Date : '))
month = int(input('Month : '))
year = int(input('Year : '))

lastWeek = max(calendar.monthcalendar(year, month))
lastDay = max(lastWeek)

if 0<day<lastDay:
    print('Valid')
else:
    print('Invalid')
