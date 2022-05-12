from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        ret = defaultdict(list)
        for s in strs:
            s_key = ''.join(sorted(s))
            ret[s_key].append(s)
        return list(ret.values())
