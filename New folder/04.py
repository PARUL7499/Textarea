with open("test.txt" , "r") as f:
    data = f.read()
    if "Python" in data:
        print("Word found")
    else:
        print("Word not Found")   