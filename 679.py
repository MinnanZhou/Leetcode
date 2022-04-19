class Solution:
    def judgePoint24(self, cards) -> bool:
        if len(cards) == 1 and abs(cards[0] - 24) < 0.00001:
            return True
        for i in range(len(cards)):
            for j in range(len(cards)):
                if i != j:
                    remains = [cards[k] for k in range(len(cards)) if k != i and k != j]
                    if \
                        self.judgePoint24(remains + [cards[i] + cards[j]]) or \
                        self.judgePoint24(remains + [cards[i] - cards[j]]) or \
                        self.judgePoint24(remains + [cards[j] - cards[i]]) or \
                        self.judgePoint24(remains + [cards[i] * cards[j]]) or \
                        (cards[j] and self.judgePoint24(remains + [cards[i] / cards[j]])) or \
                        (cards[i] and self.judgePoint24(remains + [cards[j] / cards[i]])):
                        return True
        return False
