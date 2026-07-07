class Twovector:
    def __init__(self,i,j):
        self.i=i
        self.j=j

        def show(self):
            print(f"i: {self.i}, j: {self.j}")


class Threevector(Twovector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k=k

        def show(self):
            print(f"i: {self.i}, j: {self.j}, k: {self.k}")

o = Twovector(1,2)
p = Threevector(1,2,3)

o.show()  # Output: i: 1, j: 2
p.show()  # Output: i: 1, j: 2, k: 3
