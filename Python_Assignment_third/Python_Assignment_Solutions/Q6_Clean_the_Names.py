# Q6: Clean the Names
# Purpose: Remove extra spaces, standardize names, sort, and number them.

names = [" apurva ", "SONALI", "riddhi ", "nEHA"]
clean_names = [name.strip().title() for name in names]
clean_names.sort()

for number, name in enumerate(clean_names, start=1):
    print(f"{number}. {name}")

# Explanation:
# strip() removes spaces at the beginning and end.
# title() capitalizes the first letter of each word.
# List comprehension applies these operations to every name.
# sort() arranges names alphabetically.
# enumerate(start=1) adds numbering beginning at 1.
