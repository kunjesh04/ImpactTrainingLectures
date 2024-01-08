#  WAP to check if input date is valid or not
import calendar

date = (input('Enter Date  [DD MM YYYY]: '))

DD, MM, YYYY = date.split(' ')
DD = int(DD)
MM = int(MM)
YYYY = int(YYYY)

even_days_months = [2,4,6,9,11]
odd_days_months = [1,3,5,7,8,10,12]

def leapYear(Year):
    return True if Year%4==0 else False
    
if (len(str(YYYY))!=4):
    print('Year should be of 4 digits exactly')
elif (MM<1 or MM>12) :
    (print('Month should be between 1 and 12'))
elif (DD > 31 or DD < 1):
    print('Date should be between 1 and 31')
else :
    if leapYear(YYYY):
        print('Leap Year!')
        if MM == 2:
            if DD > 29:
                print('Invalid Date')
            else :
                print('Valid Date')
        else :
            if MM in even_days_months:
                print('Max Days 30')
                if DD > 30 :
                    print('Invalid Date')
                else :
                    print('Valid Date')    
            else :
                if DD > 31:
                    print('Invalid Date')
                else :
                    print('Valid Date')
    else :
        if MM in even_days_months:
            if MM == 2:
                if DD>28:
                    print('Invalid Date')
                else :
                    print('Valid Date')
            else :
                if DD > 30 :
                    print('Invalid Date')
                else :
                    print('Valid Date')
        else :
            if DD > 31:
                print('Invalid Date')
            else :
                print('Valid Date')
            