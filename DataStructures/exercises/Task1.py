# 1. Count Strings with Same Start and End
# Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

strings = ["abc", "xyz", "aba", "1221"]
count = 0

for i in strings:
    firstChar = i[0] 
    lastChar = i[-1]  

    if len(i) >= 2 and firstChar == lastChar: 
        count += 1

print(count) 