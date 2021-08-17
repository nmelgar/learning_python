favorite_language = {
    'sarah': ['c-sharp', 'ruby'],
    'peter': ['python', 'ruby'],
    'hannah': ['java', 'python'],
    'mark': ['javascript','ruby'],
    'phil': ['ruby', 'python'],
}

#use the singular version without lists inside the dictionary
#for name, language in favorite_language.items():
#    print(f"{name.title()}'s favorite language is {language.title()}.")
for name, languages in favorite_language.items():
    print(f"{name.title()}'s favorite language are:")
    for language in languages:
        print(f"\t{language.title()}")
#Loop just through the keys using the keys() method
print(f"\nTHe name of the users that love programming are:")
for name in favorite_language.keys():
    print(name.title())

if 'erin' not in favorite_language.keys():
    print("Erin, please take our poll")
#comment to try git