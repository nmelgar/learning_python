prompt = "\nTell me something, I will repeat it back to you: "
prompt += "\nEnter 'quit to end the program "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else: print(message)

#this was the first way to run it
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)
