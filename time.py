import time
import auto_send
time_exact = "09:31:00"
while True:
    timedeltal = time.time()
    now = time.localtime(timedeltal)
    x = time.strftime('%H:%M:%S', now)
    print x
    if cmp(time_exact,x) == 0:
        auto_send.exe()
    time.sleep(1)