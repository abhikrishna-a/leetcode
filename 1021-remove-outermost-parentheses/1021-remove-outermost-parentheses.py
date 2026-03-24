class Solution(object):
   def removeOuterParentheses(self,s):
    res = ""
    c = 0
    for i in s:
        if i == "(":
            if c: res += i
            c += 1
        else:
            c -= 1
            if c: res += i
    return res