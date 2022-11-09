class Solution(object):
    def isValid(self, s):
        a = {")":"(", "}":"{","]":"["}
        stack = []
        for ob in s:
            if ob in a.values():
                stack.append(ob)
            elif len(stack)!=0 and a[ob] == stack[-1]:
                stack.pop()
            else:
                return False
            
        return len(stack)==0
                
        