class Solution(object):
    def twoSum(self, nums, target):
       seen={}
       for i,nums in enumerate(nums):
            need=target-nums
            if need in seen:
                    return [seen[need],i]
            seen[nums]=i

        