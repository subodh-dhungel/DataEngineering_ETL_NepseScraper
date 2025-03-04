class IterateArray:
    def __init__(self, arr, step = 1):
        self.arr = arr
        self.index = 0
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.arr):
            value = self.arr[self.index]
            self.index += 2
            return value
        else:
            raise StopIteration

arr = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37]
iterable_array = IterateArray(arr,0)
iterable_array = IterateArray(arr,1)


for item in iterable_array:
    print(item, end=' ')
