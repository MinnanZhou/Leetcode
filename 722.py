import re


class Solution:
    def removeComments(self, source):
        return filter(None, re.sub('//.*|/\*(.|\n)*?\*/', '', '\n'.join(source)).split('\n'))
