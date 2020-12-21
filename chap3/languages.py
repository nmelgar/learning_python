languages = ['spanish', 'french', 'italian', 'english', 'russian']
print("\nThese are the languages I lked the most:")
print("\nOriginal List")
print(languages)

print("\nAlphabetical order")
print(sorted(languages))

print("\nAlphabetical order reverse")
print(sorted(languages, reverse=True))

print("\nSort list")
languages.sort()
print(languages)

print("\nSort list reversed")
languages.sort(reverse=True)
print(languages)
print(f"There are {len(languages)} languages I like the most")

#prints the last item in the list
print(languages[-1])