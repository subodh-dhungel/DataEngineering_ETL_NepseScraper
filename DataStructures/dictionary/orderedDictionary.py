from collections import OrderedDict

#ordered dict is an collection subtype that remembers the insersion order
#ordered dict usage:
    # you need to maintain order while manupulating data
    # you are building an lru cache
    # you need to sort dictionaries while keeping order
    # you are working with json/yaml serialization
    # you need to compare dictionary with order sensitivity

d = OrderedDict(one = 1, two = 2 , three = 3)
print(d)

d["four"] = 4
print(d)

print(d.keys)

#another example:
userData = OrderedDict()
userData["name"] = "Alice"
userData["email"] = "alice13@gmail.com"
userData["age"] = 20

print(userData)