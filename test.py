# -*- coding: UTF-8 -*-
import random
import time

if __name__=="__main__":
    b = ["zhl", "gh", "gs", "xy", "sh", "xlz"]
    while 1:
        a = int(random.randint(0, 5))
        print (b[a])
        time.sleep(1)

