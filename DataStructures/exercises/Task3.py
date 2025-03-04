sentence = 'The quick brown fox jumps over the lazy dog'

words = sentence.split()

print(words)
n = 4

longWords = [word for word in words if len(word) > n]

print("Words longer than", n, ":", longWords)