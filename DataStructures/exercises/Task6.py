# 6. Write a Python program to find the second largest number in a list.

arr = [20,90,39,36,50]

def findSecondLargestItem(arr:list):
    arr.sort(reverse=True)
    if len(arr) < 2:
        raise ValueError("The list must contain 2 or more items")
    elif all(x == arr[0] for x in arr):
        raise ValueError("The list must contain differrent elements")
    else:
        return arr[1]
    

print("The second largest item in the list : ",findSecondLargestItem(arr))