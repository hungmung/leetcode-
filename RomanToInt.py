class Solution:
    def romanToInt(self, s: str) -> int:
        import re
        
        hundreds = ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        tens =     ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        units =    ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        
        n=0
        ptr = 0
        while ptr != len(s) and s[ptr] == 'M':
            ptr += 1
        n += (ptr)*1000
        temp=""
        while ptr != len(s) and s[ptr] in ['C', 'D', 'M']:
            temp = temp+s[ptr]
            ptr += 1
        if len(temp) > 0:
            n += (hundreds.index(temp)+1)*100
        temp=""
        while ptr != len(s) and s[ptr] in ['X', 'L', 'C']:
            print (s[ptr])
            temp = temp + s[ptr]
            ptr += 1
        if len(temp) > 0:
            n+=(tens.index(temp)+1)*10
        if ptr != len(s):
            n+=units.index(s[ptr:])+1
                    
        return n
