# Q8: Common Skills
# Compare two candidates' skills using sets.

apurva= ["python", "sql", "excel", "git"]
sonali = ["excel", "power bi", "sql", "tableau"]

a = set(apurva)
s = set(sonali)

common = a & s
only_aman = a - s
all_skills = a | s

print("Common Skills:", common)
print("Only apurva:", only_aman)
print("All Skills:", all_skills)

if len(a) > len(s):
    print("Apurva has more skills")
elif len(s) > len(a):
    print("sonali has more skills")
else:
    print("Both have equal skills")

