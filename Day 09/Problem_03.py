def generateTable(n):
    print(f"Multiplication Table for {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
    print("\n")

    with open(f"table_{n}.txt", "w") as f:
        for i in range(1, 11):
            f.write(f"{n} x {i} = {n * i}\n")


for i in range(2, 21):
    generateTable(i)