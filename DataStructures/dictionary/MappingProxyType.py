# MappingProxyType is a wrapper for Making readonly dictionaries
# used to create immutable proxy version of dictionaries

from types import MappingProxyType

writable = {"one": 1,"two": 2}
read_only = MappingProxyType(writable)

#The proxy is read only
print(read_only["one"])
read_only["one"] = 4
print(read_only["one"])
