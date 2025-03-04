from collections import ChainMap

#chainmap combines multiple dictionaries into a single one
# usage of chainmaps:
    #combine multiple dictionary into one without merging
    #
    
dict1 = {"one": 1, "two": 2}
dict2 = {"three": 3, "four":4}
chain = ChainMap(dict1, dict2)

print(chain)
print(chain["three"])
print(chain["one"])

print(chain["missing"])

