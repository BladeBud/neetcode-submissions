class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lenght = 0
        self.a = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.a[i]

    def set(self, i: int, n: int) -> None:
        self.a[i] = n

    def pushback(self, n: int) -> None:
        if self.lenght == self.capacity:
            self.resize()
        self.a[self.lenght] = n
        self.lenght +=1

    def popback(self) -> int:
        if self.lenght > 0:
            self.lenght -=1
        return self.a[self.lenght]

    def resize(self) -> None:
        self.capacity *= 2
        new_a = [0] * self.capacity

        for i in range(self.lenght):
            new_a[i] = self.a[i]
        self.a = new_a

    def getSize(self) -> int:
        return self.lenght
    
    def getCapacity(self) -> int:
        return self.capacity