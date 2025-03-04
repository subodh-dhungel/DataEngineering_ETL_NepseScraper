
data = {
    "Person1": 25,
    "Person2": 30,
    "Person3": 35,
    "Person4": 20,
    "Person5": 40
}

# Minimum and Maximum
min_value = min(data.values())
min_key = min(data, key=data.get)

max_value = max(data.values())
max_key = max(data, key=data.get)

print(f"Minimum value: {min_value} (Key: {min_key})")
print(f"Maximum value: {max_value} (Key: {max_key})")

# Keys and Values
sorted_by_keys = dict(sorted(data.items(), key=lambda x: x[0]))
sorted_by_values = dict(sorted(data.items(), key=lambda x: x[1]))

print("Sorted by keys:", sorted_by_keys)
print("Sorted by values:", sorted_by_values)

#Sum, Average, and Count
total_sum = sum(data.values())
average = total_sum / len(data)
count = len(data)

print(f"Sum: {total_sum}, Average: {average:.2f}, Count: {count}")


