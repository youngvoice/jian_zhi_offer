'''
class Solution:
    def replaceSpace(self, s: str) -> str:
        res = ''
        for c in s:
            if c != ' ':
                res += c 
            else:
                res += '%20'
        return res 
'''
class Solution:
    def replaceSpace(self, s: str) -> str:
        ret = ''
        i = len(s) - 1
        while i >= 0:
            if s[i] != ' ':
                ret = s[i] + ret
            else:
                ret = '%20' + ret
            i -= 1
        return ret

            