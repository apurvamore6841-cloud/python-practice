jan = {"Amit", "Sara", "John", "Riya"}
feb = {"Sara", "Riya", "Kunal", "Neha"}

print("Both:", sorted(jan & feb))
print("Either:", sorted(jan | feb))
print("Only Jan:", sorted(jan - feb))
print("Only Feb:", sorted(feb - jan))
print("Unique customers:", len(jan | feb))