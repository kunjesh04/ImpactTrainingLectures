import time

n = int(input('Enter Number of Seconds : '))
iSECONDS = n
iMINUTES = n//60
while iSECONDS >= 0 and iMINUTES >= 0 :
    MINUTES, SECONDS = divmod(iSECONDS, 60)
    time.sleep(1)
    if 0<=SECONDS<=9:
        SECONDS=str(0) + str(SECONDS)
    print(f'{MINUTES}:{SECONDS}')
    SECONDS = int(SECONDS)
    iSECONDS -= 1
print('Countdown Finished!')
    