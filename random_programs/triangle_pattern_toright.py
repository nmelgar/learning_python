#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php

rows = 5

for i in range(rows + 1):
    for j in range (i):
        print("*", end = " ")
    print(" ")

for i in reversed(range(rows)):
    for j in range (i):
        print("*", end = " ")
    print(" ")
