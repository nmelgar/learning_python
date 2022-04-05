def hello_function():
    print("hello world")

hello_function()

#ONE WAY
# def your_name():
#     name = str(input("whats your name? "))
#     age = int(input("whats your age? "))
#     print("hello " + name + " " + str(age))

# your_name()

#ANOTHER WAY
# def your_name(name, age):
#     print("hello " + name + " " + str(age))

# your_name(name = "joan", age = 27)

#ANOTHER WAY
def greeting_function(name, age):
    print("welcome " + name + ". You are " + str(age)+ " years old.")

name = input("Whats your name?  ")
age = input("Whats your age?  ")
greeting_function(name, age)