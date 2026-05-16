class Solution(object):
    def maximumWealth(self, accounts):
        r = 0

        for c in accounts:
            w = sum(c)

            r = max(r, w)

        return r