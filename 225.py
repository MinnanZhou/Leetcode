from collections import deque


class MyStack:

    def __init__(self):
        self.q1 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        count = len(self.q1) - 1
        while count:
            self.q1.append(self.q1.popleft())
            count -= 1
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[-1]

    def empty(self) -> bool:
        return len(self.q1) == 0
