import time
from datetime import datetime as dt
while True:
    time.sleep(1)
    now=dt.now()
    m=now.second
    print(m)
    