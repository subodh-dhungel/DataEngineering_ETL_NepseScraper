# 4. write a program that compresses a file using a compression algorithm (e.g., zlib) and then another
# program to decompress it.

import zlib

def compressFile(inputFileName, compressedFileName):
    """Compress a file using zlib and save the compressed data."""
    try:
        with open(inputFileName, 'rb') as inputFile:
            fileData = inputFile.read() 
            compressedData = zlib.compress(fileData) 

        with open(compressedFileName, 'wb') as compressedFile:
            compressedFile.write(compressedData)  
            
        print(f"File {inputFileName} successfully compressed to {compressedFileName}.")
    
    except FileNotFoundError:
        print(f"File {inputFileName} not found.")


def decompressFile(compressedFileName, decompressedFileName):
    """Decompress a zlib compressed file and save the decompressed data."""
    try:
        with open(compressedFileName, 'rb') as compressedFile:
            compressedData = compressedFile.read()  
            decompressedData = zlib.decompress(compressedData)  

        with open(decompressedFileName, 'wb') as decompressedFile:
            decompressedFile.write(decompressedData)  
            
        print(f"File {compressedFileName} successfully decompressed to {decompressedFileName}.")
    
    except FileNotFoundError:
        print(f"File {compressedFileName} not found.")


# Compress a file
compressFile('example.txt', 'example_compressed.zlib')

# Decompress the file
decompressFile('example_compressed.zlib', 'example_decompressed.txt')
