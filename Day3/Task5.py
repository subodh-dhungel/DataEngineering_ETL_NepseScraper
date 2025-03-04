numbers = [1,2,3,4,5,6,7,8,9,10]

def filterEven():
    for num in numbers:
        if num % 2 == 0:
            yield num

generator = filterEven()

for num in generator:
    print(num)