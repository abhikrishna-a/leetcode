class Solution(object):
    def differenceOfSum(self, nums):
        e_sum = sum(nums)
        d_sum = sum(int(digit) for num in nums for digit in str(num))
        return abs(e_sum - d_sum)