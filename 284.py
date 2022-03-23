class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.len = len(nums)
        self.pos = 0
        self.array = nums

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        if self.pos >= self.len - 1:
            return False
        return True

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        value = self.array[self.pos] if self.pos < self.len else None
        self.pos += 1
        return value


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.instance = iterator
        self.value = self.instance.next() if self.instance.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.value

    def next(self):
        """
        :rtype: int
        """
        value = self.value
        self.value = self.instance.next() if self.instance.hasNext() else None
        return value

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.value else False


inp = [1, 2, 3, 4, 5]
a = Iterator(inp)
b = PeekingIterator(a)
print(b.peek())
print(b.next())
print(b.next())
print(b.peek())
print(b.next())
print(b.next())
print(b.next())
print(b.next())
print(b.hasNext())
