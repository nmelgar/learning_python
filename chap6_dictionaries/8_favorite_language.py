favorite_language = {
    'sarah': 'c-sharp',
    'peter': 'python',
    'hannah': 'java',
    'mark': 'javascript',
    'phil': 'ruby',
}

language = favorite_language['sarah'].title()
print(f"Sarah's favorite laguage is {language}.")

for name, language in favorite_language.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

#Loop just through the keys using the keys() method
print(f"\nTHe name of the users that love programming are:")
for name in favorite_language.keys():
    print(name.title())