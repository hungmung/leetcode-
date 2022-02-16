class Solution:
    def romanToInt(self, s: str) -> int:
        import re
        
        hundreds = ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        tens =     ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        units =    ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        
        rx = '^(M*)([CM|C|D]*)([XC|L|X]*)(.*)$'
        m = re.fullmatch(rx, s )
        n=0
        if m[1]:
            n += len(m[1])*1000
        if m[2]:
            n += (hundreds.index(m[2])+1)*100
        if m[3]:
            n += (tens.index(m[3]) + 1) * 10
        if m[4]:
            n += units.index(m[4]) + 1
        
        return n
