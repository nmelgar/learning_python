#https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
#exercise #6

odd_counter = 0
even_counter = 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#for number in range(1, 100):
for number in numbers:
    if (number % 2 == 0):
        even_counter += 1
    elif(number % 2 != 0):
        odd_counter += 1
print("there are: " + str(odd_counter) + " odd numbers in the list")
print("there are: " + str(even_counter) + " even numbers in the list")
