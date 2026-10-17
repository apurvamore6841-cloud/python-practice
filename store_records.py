stores = {
    "Pune": {"sales": 50000, "staff": 8},
    "Mumbai": {"sales": 82000, "staff": 12},
    "Nashik": {"sales": 31000, "staff": 5}
}

print(stores["Mumbai"]["sales"])

stores["Nashik"]["staff"] = 6
stores["Nagpur"] = {"sales": 27000, "staff": 4}

for city, details in stores.items():
    print(f"{city}: sales={details['sales']}, staff={details['staff']}")