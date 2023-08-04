from datetime import datetime
def async_time():
    c = str(datetime.now())
    print(c)
    b = c[0:10]
    c = c[11:-7]
    print(c)
    e = c.split(':')
    hours = int(input("Enter hours: \n"))
    if hours<10:
        hours = '0'+str(hours)
    minutes = int(input("Enter minutes: \n"))
    if minutes<10:
        minutes = '0'+str(minutes)
    seconds = int(input("Enter seconds: \n"))
    if seconds<10:
        seconds = '0'+str(seconds)
    e[0],e[1],e[2] = hours,minutes,seconds
    new_time = str(e[0])+':'+str(e[1])+':'+str(e[2])
    total = b+' '+new_time+'.'+'000000'
    while 1:
        x = str(datetime.now())
        print(f"{x[11:-7]} - {total[11:-7]}")
        if str(x)[11:-7]==str(total)[11:-7]:
            break
        else:
            continue
async_time()