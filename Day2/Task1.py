#Extension finder

def getExtension(data):
    if "://" in data:
        scheme = data.split("://")[0]
        print("The given data is of type: URL")
        print("URL Scheme:", scheme)
    else:
        for char in data:
            if char == ".":
                extension = data.split(".")
                print("The given data is of type: File")
                print("File Extension:", extension[-1])
                break   
            elif "/" in data:
                print("The given data is of type: Directory")
                break
        else:
            print("The given data is of unknown type")

getExtension("https://example.com")
getExtension("subodh.txt")
getExtension("/home/user/documents/")
getExtension("no_extension_file")