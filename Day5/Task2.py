# 2. You want to feed a text or binary string to code that’s been written to operate on file-
# like objects instead. ( files in memory)

import io

def processTextFile(textData):
    """Simulate processing of text file-like object."""
    textFile = io.StringIO(textData)
    
    for line in textFile:
        print(f"Processing line: {line.strip()}")

def processBinaryFile(binaryData):
    """Simulate processing of binary file-like object."""
    binaryFile = io.BytesIO(binaryData)
    
    while chunk := binaryFile.read(16):
        print(f"Processing chunk: {chunk.hex()}")

def main():
    textData = "This is line 1.\nThis is line 2.\nThis is line 3."
    
    binaryData = b"Hello world!\x00\x01\x02"
    
    print("Processing text data as a file-like object:")
    processTextFile(textData)
    
    print("\nProcessing binary data as a file-like object:")
    processBinaryFile(binaryData)

main()
