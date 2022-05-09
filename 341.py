class NestedIterator:
    def __init__(self, nestedList):
        self.data = nestedList
        self.pointer = 0
        self.res = self.flatten()

    def flatten(self):
        ret = []
        for i in range(len(self.data)):
            if self.data[i].isInteger():
                ret.append(self.data[i].getInteger())
            else:
                temp = self.data[i].getList()
                if not temp: continue
                ret += NestedIterator(temp).res
        return ret

    def hasNext(self):
        return self.pointer < len(self.res)

    def next(self):
        self.pointer += 1
        return self.res[self.pointer - 1]
