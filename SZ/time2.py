import time
import SZ
time_exact = "09:31:00"
# time_exact = "11:31:10"
while True:
    timedeltal = time.time()
    now = time.localtime(timedeltal)
    x = time.strftime('%H:%M:%S', now)
    print x
    if cmp(time_exact,x) == 0:
        SZ.exe()
    time.sleep(1)