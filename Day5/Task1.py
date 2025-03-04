# 1. write a Python program that takes user input and appends it to a text file. Also write a program that
# overwrites the existing content of a file with new data.

def appendToFile(fileName):
    userInput = input("Enter the text you want to append to the file: ")
    with open(fileName, 'a') as file:
        file.write(userInput + '\n')
    print(f"Your input has been appended to {fileName}.")

def overwriteFile(fileName):
    userInput = input("Enter the text to overwrite the file: ")
    with open(fileName, 'w') as file:
        file.write(userInput + '\n')
    print(f"The file {fileName} has been overwritten with your new input.")

def main():
    fileName = 'example.txt'
    
    action = input("Do you want to append or overwrite the file? (append/overwrite): ").strip().lower()
    
    if action == 'append':
        appendToFile(fileName)
    elif action == 'overwrite':
        overwriteFile(fileName)
    else:
        print("Invalid choice! Please select 'append' or 'overwrite'.")

main()
