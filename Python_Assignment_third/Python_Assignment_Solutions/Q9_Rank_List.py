# Q9: Rank List
# Sort students by marks, print ranks, and show the top three.

marks = {"Apurva": 78, "sanika": 64, "Sonali": 91, "riddhi": 55, "megha": 67}

rank_list = sorted(
    marks.items(),
    key=lambda item: item[1],
    reverse=True
)

for rank, (name, mark) in enumerate(rank_list, start=1):
    print(f"{rank}. {name} - {mark}")

print("Top 3:", rank_list[:3])

