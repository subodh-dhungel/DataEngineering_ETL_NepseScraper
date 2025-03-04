#9.Write a Python program to sort a list of nested dictionaries.
#eg:
#[{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]

dict1 = {"JFL": {"price": 512}, "ICFC":{"price":655}, "NFS":{"price": 712}}
array = ["a","z","A","C","c","b"]
sortedDict = dict(sorted(dict1.items()))
sortedArray = sorted(array)
print(sortedDict)
print(sortedArray)