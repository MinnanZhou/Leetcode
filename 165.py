class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')
        i = 0
        while i < len(version1) and i < len(version2):
            if int(version1[i]) < int(version2[i]):
                return -1
            if int(version1[i]) > int(version2[i]):
                return 1
            i += 1
        if len(version1) == len(version2):
            return 0
        if len(version1) > len(version2):
            if any(int(v) > 0 for v in version1[i:]):
                return 1
            return 0
        if len(version1) < len(version2):
            if any(int(v) > 0 for v in version2[i:]):
                return -1
            return 0
