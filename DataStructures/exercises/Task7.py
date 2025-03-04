# 7.Write a Python program to create a list by concatenating a given list with a range from 1 to n.
# eg: [q,p] -> [q1,q2,q3,p1,p2,p3]

def concatenateWithRange(lst:list, n:int):
    result = []
    for item in lst:
        for i in range(1, n+1):
            result.append(item+str(i))
        
    return result
    
list = ["q","p"]
n = 3
result = concatenateWithRange(list, n)
print(result)