import random

class RandomOperations:
    def __init__(self, seedValue=None):
        if seedValue is not None:
            random.seed(seedValue)

    def generateRandomNumber(self, start, end):
        """Generate a random integer between start and end (inclusive)."""
        return random.randint(start, end)

    def generateRandomFloat(self):
        """Generate a random float between 0 and 1."""
        return random.random()

    def pickRandomChoice(self, sequence):
        """Pick a random item from a given sequence."""
        return random.choice(sequence)

    def pickMultipleRandomChoices(self, sequence, count):
        """Pick multiple random items from a sequence (with replacement)."""
        return random.choices(sequence, k=count)

    def pickUniqueRandomChoices(self, sequence, count):
        """Pick multiple random items from a sequence (without replacement)."""
        return random.sample(sequence, count)

    def shuffleList(self, sequence):
        """Shuffle a given list in place."""
        random.shuffle(sequence)
        return sequence

randomOps = RandomOperations(seedValue=42) 

# Generate random numbers
print("Random Integer (1-100):", randomOps.generateRandomNumber(1, 100))
print("Random Float:", randomOps.generateRandomFloat())

# Random choice from a list
items = ["apple", "banana", "cherry", "date", "elderberry"]
print("Random Choice:", randomOps.pickRandomChoice(items))

# Pick multiple random choices (with replacement)
print("Multiple Random Choices:", randomOps.pickMultipleRandomChoices(items, 3))

# Pick unique random choices (without replacement)
print("Unique Random Choices:", randomOps.pickUniqueRandomChoices(items, 3))

# Shuffle a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original List:", numbers)
print("Shuffled List:", randomOps.shuffleList(numbers))
