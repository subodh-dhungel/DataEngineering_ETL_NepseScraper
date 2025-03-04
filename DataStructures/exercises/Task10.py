# 10. Write a Python program to split a list every Nth element.
# input:['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]

input = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]

def splitEveryNth(lst,n):
    return [lst[i::n]for i in range(n)]

print(splitEveryNth(input,3))
