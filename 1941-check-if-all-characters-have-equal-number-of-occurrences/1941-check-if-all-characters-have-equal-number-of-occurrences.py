class Solution(object):
    def areOccurrencesEqual(self, s):
        for ch in s:
            if s.count(ch) != s.count(s[0]):
                return False
        return True
        