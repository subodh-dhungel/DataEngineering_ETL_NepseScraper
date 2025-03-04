def remove_duplicates(sequence):
    seen = set()  
    result = []  
    
    for item in sequence:
        if item not in seen: 
            result.append(item) 
            seen.add(item)  
    
    return result


sequence = [1, 2, 2, 3, 4, 3, 5, 1, 6]
unique_sequence = remove_duplicates(sequence)
print("Original sequence:", sequence)
print("Sequence without duplicates:", unique_sequence)
