class Solution:
    def findPoisonedDuration(self, timeSeries, duration: int) -> int:
        total = duration
        for i in range(1, len(timeSeries)):
            if timeSeries[i] - timeSeries[i - 1] >= duration:
                total += duration
            else:
                total += timeSeries[i] - timeSeries[i - 1]
        return total
