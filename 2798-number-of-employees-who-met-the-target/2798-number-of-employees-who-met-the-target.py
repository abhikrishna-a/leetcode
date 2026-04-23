class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        count=0

        for h in hours:
            if h >=target:
                count+=1
        return count
sol = Solution()
print(sol. numberOfEmployeesWhoMetTarget([0,1,2,3,4],2))