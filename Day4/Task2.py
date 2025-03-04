# You have a byte string and you need to unpack it into an integer value. Alternatively, you need to convert a large integer back into a byte string.

def unpackBytesToInt(byteData, byteOrder='big'):
    """Convert a byte string into an integer."""
    return int.from_bytes(byteData, byteorder=byteOrder)

def packIntToBytes(integerValue, byteOrder='big'):
    """Convert an integer into a byte string."""
    byteLength = (integerValue.bit_length() + 7) // 8 or 1 
    return integerValue.to_bytes(byteLength, byteorder=byteOrder)

# Bytes lai integer ma change garna
byteData = b'\x00\x10'
integerValue = unpackBytesToInt(byteData, byteOrder='big')
print(f"Byte data {byteData} converted to integer: {integerValue}")

# Integer lai bytes ma change garna
integerValue = 256
byteData = packIntToBytes(integerValue, byteOrder='big')
print(f"Integer {integerValue} converted to byte data: {byteData}")

# Larger integer handle garna
largeInteger = 9876543210
largeByteData = packIntToBytes(largeInteger, byteOrder='big')
restoredInteger = unpackBytesToInt(largeByteData, byteOrder='big')

print(f"Larger integer {largeInteger} converted to byte data: {largeByteData}")
print(f"Restored integer from byte data: {restoredInteger}")
