items = [
    {"name": "Apples", "price": 1.2},
    {"name": "Bananas", "price": 0.5},
    {"name": "Mangoes", "price": 2.5},
    {"name": "Guavas", "price": 3.0},
    {"name": "Papayas", "price": 1.8},
]

print(f"{'Item':<15}{'Price ($)':>10}")
print("-" * 25)

for item in items:
    print(f"{item['name']:<15}{item['price']:>10.2f}")