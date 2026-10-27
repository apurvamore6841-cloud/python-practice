# Q9: Rank List
# Purpose: Sort students by marks, print ranks, and show the top three.

marks = {"Riya": 78, "Omkar": 64, "Sneha": 91, "Aditya": 55, "Isha": 67}

rank_list = sorted(
    marks.items(),
    key=lambda item: item[1],
    reverse=True
)

for rank, (name, mark) in enumerate(rank_list, start=1):
    print(f"{rank}. {name} - {mark}")

print("Top 3:", rank_list[:3])

# Explanation:
# items() creates (name, marks) pairs.
# sorted() orders pairs by marks.
# lambda item: item[1] selects marks for sorting.
# reverse=True sorts from highest to lowest.
# enumerate() assigns ranks; [:3] selects the first three entries.
