class Solution(object):
    def canAliceWin(self, nums):
        single_digit = 0
        double_digit = 0
        
        for num in nums:
            if num < 10:
                single_digit += num
            else:
                double_digit += num
        
        total = single_digit + double_digit
        
        return single_digit != total - single_digit