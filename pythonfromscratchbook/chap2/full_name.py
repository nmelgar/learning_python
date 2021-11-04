first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"hello, {full_name.title()}!")
message =f"hello,{full_name.upper()}!\n"
print(message)

#try for the new line(\n) and tab (\t)
print("languages: \nPython \nJava \nJavascript")
print("languages: \n\tPython \n\tJava \n\tJavascript\n\n")

third_name = "nefi"
fourth_name = "melgar"
full_second_name = f"{third_name} {fourth_name}"
print(full_second_name.title())

final_message = f"\nhello, {full_name.title()} and {full_second_name.title()}, are the names i practiced with"
print(final_message)

favorite_language = "\npython "
favorite_language = favorite_language.rstrip()
print(favorite_language)



