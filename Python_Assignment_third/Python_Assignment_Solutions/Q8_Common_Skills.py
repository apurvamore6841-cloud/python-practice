# Q8: Common Skills
# Purpose: Compare two candidates' skills using sets.

aman = ["python", "sql", "excel", "git"]
pooja = ["excel", "power bi", "sql", "tableau"]

a = set(aman)
p = set(pooja)

common = a & p
only_aman = a - p
all_skills = a | p

print("Common Skills:", common)
print("Only Aman:", only_aman)
print("All Skills:", all_skills)

if len(a) > len(p):
    print("Aman has more skills")
elif len(p) > len(a):
    print("Pooja has more skills")
else:
    print("Both have equal skills")

# Explanation:
# set() creates collections of unique items.
# & finds common skills (intersection).
# - finds skills only in Aman’s set (difference).
# | combines all unique skills (union).
# len() counts skills to compare the candidates.
