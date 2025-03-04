def mostfrequent(sequence, n=None):
    frequency = {}
    for item in sequence:
        frequency[item] = frequency.get(item, 0) + 1

    sorted_items = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    return sorted_items[:n] if n else sorted_items

sequence = [1, 2, 2, 3, 4, 3, 5, 1, 6, 3, 2, 4]
top_items = mostfrequent(sequence, n=2)
print("Most frequent items:", top_items)