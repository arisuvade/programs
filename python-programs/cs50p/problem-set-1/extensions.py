file_name = input("File name: ")

if "." in file_name:
    file, type = file_name.split(".")
    if type == "gif":
        print("images/gif")
    elif type == "jpg":
        print("images/jpeg")
    elif type == "peg":
        print("images/jpeg")
    elif type == "png":
        print("images/png")
    elif type == "pdf":
        print("pdf file")
    elif type == "txt":
        print("text file")
    elif type == "zip":
        print("zip file")
else:
    print("application/octet-stream")
