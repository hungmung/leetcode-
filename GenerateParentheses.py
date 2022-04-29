
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

class Solution:
    def isValid(self, s: string) -> bool:
        pairs = {')':'(', '}':'{', ']':'['}
        stack = []

        try:
            for char in s: 
                if char in pairs.keys():
                    if stack.pop() != pairs[char]:
                        return False
                else:
                    stack.append(char)
            return len(stack)==0
        except:
            return False
    
    
    def generateParenthesis(self, n: int) -> List[str]:
        myList = ["("]*(n)
        myList.extend([")"]*(n))
        rtn = []
        from itertools import permutations
        for group in filter(lambda x: x[0]=='(' and x[-1]==')', permutations(myList, (n)*2)):
            test = "".join(group)
            if test in rtn: continue
            if self.isValid(test):
                rtn.append(test)
        return rtn
