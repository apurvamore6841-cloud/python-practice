'''A shop owner wants a quick summary of product sales. Each record contains a product name, price, and units sold.'''


names = [' riya shah', 'AMAN KUMAR ', ' neha patil ', 'ROHAN DAS']

cleaned_names = []

for name in names:
    cleaned_name = name.strip().title()
    cleaned_names.append(cleaned_name)

print("Cleaned names:", cleaned_names)
print("Number of names:", len(cleaned_names))
