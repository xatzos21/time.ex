# Task is to Create a program that
# - saves current time and prints it
# - saves another time moment and prints it
# - prints the time that has passed in between

import time

input("Start stopwatch")
x = time.time()
print("Tme now is: ", x)
time.sleep(3)
y = time.time()
print("TIme now is: ", y)
z = y-x

print("Start time:" + str(time.ctime(x)))
print("Stop time:" + str(time.ctime(y)))
print("Time elapsed is: " + str(z))
