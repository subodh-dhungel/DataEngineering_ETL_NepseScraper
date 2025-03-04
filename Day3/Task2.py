class SquareIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0 

    def __iter__(self):
        return self  

    def __next__(self):
        if self.index >= len(self.numbers):
            raise StopIteration  
        
        value = self.numbers[self.index] ** 2  
        self.index += 1  
        return value

numbers = [1, 2, 3, 4, 5]
squares = SquareIterator(numbers)

for square in squares:
    print(square)  
