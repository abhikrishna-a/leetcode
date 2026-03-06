class Solution(object):
    def countDigits(self, num):
        count=0
        for d in str(num):
            if num% int(d)==0:
                count+=1
        return count
