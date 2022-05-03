from collections import Counter


class Solution:
    def subdomainVisits(self, cpdomains):
        c = Counter()
        for cp in cpdomains:
            [count, domain] = cp.split(' ')
            domain = domain.split('.')
            for i in range(len(domain)):
                c['.'.join(domain[i:])] += int(count)
        ret = []
        for key, value in c.items():
            ret.append(str(value) + ' ' + key)
        return ret


a = Solution()
inp = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print(a.subdomainVisits(inp))
