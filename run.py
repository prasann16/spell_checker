import spell_checker

# To initialize class
checker = spell_checker.spell_checker("city_names.txt")

# Getting input city name
print("")
word = input("Type City Name: ")
print("")
result = checker.result(word)

# If there are more than one results
for item in result:
    print("Match:", item)
