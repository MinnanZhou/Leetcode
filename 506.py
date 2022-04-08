class Solution:
    def findRelativeRanks(self, score):
        score_s = sorted(score, reverse=True)
        medal = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        s_set = {}
        for i, s in enumerate(score_s):
            if i < 3:
                i = medal[i]
            else:
                i += 1
            s_set[s] = str(i)
        return [s_set[sc] for sc in score]
