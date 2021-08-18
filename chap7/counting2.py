#imprimir los numeros que al dividirse entre 2 si dejan
#residuo, osea número impares

number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue
    print(number)