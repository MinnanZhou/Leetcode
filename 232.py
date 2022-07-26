class MyQueue:

    def __init__(self):
        self.data = []
        self.dataRev = []

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        if not self.dataRev:
            self.dataRev = self.data[::-1]
            self.data.clear()
        return self.dataRev.pop()

    def peek(self) -> int:
        if self.dataRev:
            return self.dataRev[-1]
        return self.data[0]

    def empty(self) -> bool:
        return len(self.data) + len(self.dataRev) == 0
