class Solution:
    def exclusiveTime(self, n: int, logs):
        ret = [0 for _ in range(n)]
        callstack = []
        time = 0
        for info in logs:
            ID, status, timestamp = int(info.split(':')[0]),info.split(':')[1],int(info.split(':')[2])
            if not callstack:
                callstack.append((ID, status, timestamp))
                time = timestamp
            else:
                if ID == callstack[-1][0] and status != callstack[-1][1]:
                    callstack.pop()
                    ret[ID] += (timestamp - time + 1)
                    time = timestamp + 1
                else:
                    ret[callstack[-1][0]] += timestamp - time
                    callstack.append((ID, status, timestamp))
                    time = timestamp
        return ret


a = Solution()
inp = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
print(a.exclusiveTime(2, inp))
