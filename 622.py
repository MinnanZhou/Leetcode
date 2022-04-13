class MyCircularQueue:

    def __init__(self, k: int):
        self.data = [-1 for _ in range(k)]
        self.in_pointer = 0
        self.out_pointer = 0
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.data[self.in_pointer] == -1:
            self.data[self.in_pointer] = value
            self.in_pointer = (1 + self.in_pointer) % self.size
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.data[self.out_pointer] == -1:
            return False
        else:
            self.data[self.out_pointer] = -1
            self.out_pointer = (self.out_pointer + 1) % self.size
            return True

    def Front(self) -> int:
        return self.data[self.out_pointer]

    def Rear(self) -> int:
        return self.data[self.in_pointer - 1]

    def isEmpty(self) -> bool:
        return all(self.data[i] == -1 for i in range(self.size))

    def isFull(self) -> bool:
        return all(self.data[i] != -1 for i in range(self.size))


a = MyCircularQueue(3)
a.enQueue(1)
a.enQueue(2)
a.enQueue(3)
a.enQueue(4)
a.Rear()
a.Front()
a.isFull()
a.deQueue()
a.enQueue(4)
a.Rear()
