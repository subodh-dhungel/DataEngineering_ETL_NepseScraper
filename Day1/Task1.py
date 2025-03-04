def bubble_sort(arr, key=None):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if key is None:
                if arr[j] > arr[j + 1]: 
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                if arr[j][key] > arr[j + 1][key]:  
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def find_smallest_largest(arr, n, key=None):
    sorted_arr = bubble_sort(arr, key)
    return sorted_arr[:n], sorted_arr[-n:]

# Portfolio of stocks
portfolio = [
    {'name': 'Stock A', 'value': 1200, 'price': 50},
    {'name': 'Stock B', 'value': 5000, 'price': 100},
    {'name': 'Stock C', 'value': 7000, 'price': 200},
    {'name': 'Stock D', 'value': 3000, 'price': 75},
    {'name': 'Stock E', 'value': 4000, 'price': 80},
]

# smallest and largest
n = 3
smallest_3, largest_3 = find_smallest_largest(portfolio, n, key='value')

print("Smallest 3 items based on 'value':", smallest_3)
print("Largest 3 items based on 'value':", largest_3)


a = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37]
smallest_3, largest_3 = find_smallest_largest(a, 3)

print("Smallest 3 numbers:", smallest_3)
print("Largest 3 numbers:", largest_3)