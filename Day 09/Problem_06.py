with open("file.txt") as f:
    contnet1 = f.read()

with open("files.txt") as f:
    contnet2= f.read()

if (contnet1 == contnet2):
    print("Yes these files are identical")

else:
    print("No these files is not identicial")