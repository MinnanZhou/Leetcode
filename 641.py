class MyCircularDeque:

    def __init__(self, k: int):
        self._data = [-1 for _ in range(k)]
        self._F = 0
        self._R = k - 1
        self._K = k

    def insertFront(self, value: int) -> bool:
        if self._data[self._F] != -1:
            return False
        else:
            self._data[self._F] = value
            self._F = (self._F + 1) % self._K
        return True

    def insertLast(self, value: int) -> bool:
        if self._data[self._R] != -1:
            return False
        else:
            self._data[self._R] = value
            self._R = (self._R - 1) % self._K
        return True

    def deleteFront(self) -> bool:
        if self._data[self._F - 1] == -1:
            return False
        else:
            self._data[self._F - 1] = -1
            self._F = (self._F - 1) % self._K
        return True

    def deleteLast(self) -> bool:
        if self._data[(self._R + 1) % self._K] == -1:
            return False
        else:
            self._data[(self._R + 1) % self._K] = -1
            self._R = (self._R + 1) % self._K
        return True

    def getFront(self) -> int:
        return self._data[self._F - 1]

    def getRear(self) -> int:
        return self._data[(self._R + 1) % self._K]

    def isEmpty(self) -> bool:
        return (self._F - self._R) % self._K == 1 and self._data[0] == -1

    def isFull(self) -> bool:
        return (self._F - self._R) % self._K == 1 and self._data[0] != -1


a = MyCircularDeque(77)
ops = ["insertFront", "getRear", "deleteLast", "getRear", "insertFront", "insertFront", "insertFront", "insertFront",
       "isFull", "insertFront", "isFull", "getRear", "deleteLast", "getFront", "getFront", "insertLast", "deleteFront",
       "getFront", "insertLast", "getRear", "insertLast", "getRear", "getFront", "getFront", "getFront", "getRear",
       "getRear", "insertFront", "getFront", "getFront", "getFront", "getFront", "deleteFront", "insertFront",
       "getFront", "deleteLast", "insertLast", "insertLast", "getRear", "getRear", "getRear", "isEmpty", "insertFront",
       "deleteLast", "getFront", "deleteLast", "getRear", "getFront", "isFull", "isFull", "deleteFront", "getFront",
       "deleteLast", "getRear", "insertFront", "getFront", "insertFront", "insertFront", "getRear", "isFull",
       "getFront", "getFront", "insertFront", "insertLast", "getRear", "getRear", "deleteLast", "insertFront",
       "getRear", "insertLast", "getFront", "getFront", "getFront", "getRear", "insertFront", "isEmpty", "getFront",
       "getFront", "insertFront", "deleteFront", "insertFront", "deleteLast", "getFront", "getRear", "getFront",
       "insertFront", "getFront", "deleteFront", "insertFront", "isEmpty", "getRear", "getRear", "getRear", "getRear",
       "deleteFront", "getRear", "isEmpty", "deleteFront", "insertFront", "insertLast", "deleteLast"]
v = [[89], [], [], [], [19], [23], [23], [82], [], [45], [], [], [], [], [], [74], [], [], [98], [], [99], [], [], [],
     [], [], [], [8], [], [], [], [], [], [75], [], [], [35], [59], [], [], [], [], [22], [], [], [], [], [], [], [],
     [], [], [], [], [21], [], [26], [63], [], [], [], [], [87], [76], [], [], [], [26], [], [67], [], [], [], [], [36],
     [], [], [], [72], [], [87], [], [], [], [], [85], [], [], [91], [], [], [], [], [], [], [], [], [], [34], [44], []]
for index, op in enumerate(ops):
    if index == len(ops) - 7:
        i = 0
    if not v[index]:
        print(eval('a.' + op + '()'))
    else:
        print(eval('a.' + op + '(' + str(v[index][0]) + ')'))
