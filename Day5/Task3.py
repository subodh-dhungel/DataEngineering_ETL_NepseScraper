# 3. create a program that can merge multiple text files into one file and another program to split a large
# file into smaller files based on a specified file size or line count.

def mergeFiles(fileNames, outputFileName):
    """Merge multiple text files into a single file."""
    with open(outputFileName, 'w') as outputFile:
        for fileName in fileNames:
            try:
                with open(fileName, 'r') as inputFile:
                    content = inputFile.read()
                    outputFile.write(content)
                    outputFile.write("\n")
            except FileNotFoundError:
                print(f"File {fileName} not found. Skipping.")
                
    print(f"Files merged into {outputFileName}")


def splitFileByLineCount(inputFileName, linesPerFile):
    try:
        with open(inputFileName, 'r') as inputFile:
            fileCount = 1
            lines = []
            
            for line in inputFile:
                lines.append(line)
                if len(lines) >= linesPerFile:
                    with open(f"output_{fileCount}.txt", 'w') as outputFile:
                        outputFile.writelines(lines)
                    lines = [] 
                    fileCount += 1
            
            if lines:
                with open(f"output_{fileCount}.txt", 'w') as outputFile:
                    outputFile.writelines(lines)
            
        print(f"File split into {fileCount} smaller files.")
    except FileNotFoundError:
        print(f"File {inputFileName} not found.")


def splitFileBySize(inputFileName, maxFileSizeMB):
    try:
        with open(inputFileName, 'rb') as inputFile:
            fileCount = 1
            chunk = inputFile.read(1024 * 1024 * maxFileSizeMB) 
            while chunk:
                with open(f"output_{fileCount}.txt", 'wb') as outputFile:
                    outputFile.write(chunk)
                fileCount += 1
                chunk = inputFile.read(1024 * 1024 * maxFileSizeMB)
        
        print(f"File split into {fileCount - 1} smaller files.")
    except FileNotFoundError:
        print(f"File {inputFileName} not found.")


fileNames = ['file1.txt', 'file2.txt', 'file3.txt']
mergeFiles(fileNames, 'merged_output.txt')
splitFileByLineCount('largefile.txt', 10)
splitFileBySize('largefile.txt', 1)

#set
#dictionary
#tuple
#list