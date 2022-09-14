# The task is to Create a program that
# - takes an  int as input
# - uses this int as a countdown
# - visibly counts down
# - prints begin time, end time and countdown int

import time
import os

x = int(input("Enter integer: "))
a = time.ctime()
print("Begin time is: ", a)
time.sleep(1)
print("Integer number is: ", x)
time.sleep(1)
while x > 0:
    print(x-1)
    time.sleep(3)
    os.system("clear")
    x = x-1
b= time.ctime()
print("Begin time is: ", a)
time.sleep(1)
print("End time is: ", b)