class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maximum = max(candies)
        a = []

        for candy in candies:
            a.append(candy + extraCandies >= maximum)

        return a