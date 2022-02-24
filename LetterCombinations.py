class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
        Return the answer in any order.
        '''
        mappings = {
            1: [],
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }
        from itertools import product
        
        iterables = []
        if len(digits)==0: return iterables
        for i in digits:
            chars = mappings[int(i)]
            iterables.append(chars)
        prods =  list(product(*iterables))
        rtn = ["".join(x) for x in prods]
        return rtn
