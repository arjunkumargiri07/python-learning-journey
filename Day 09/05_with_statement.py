f = open("file.txt", "r")
data = f.read()
f.close()

#The same can be written using with statement
with open("file.txt") as f:
    print(f.read())