# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# Write the code that will take a string and make this conversion given a number of rows:
# 
# string convert(string s, int numRows);

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        import numpy as np
        posn = 0
        arr = []
        if numRows==1: return s
        while posn < len(s):
            if posn%(numRows-1) == 0:
                arr.append(list(s[posn:posn+numRows]))
                posn += numRows
            else:
                tmp = [""]*numRows
                tmp[-1*posn%(numRows-1)] = s[posn]
                arr.append(tmp)
                posn += 1
        #while len(arr[-1]) < numRows:
        #    arr[-1].append("")
        arr[-1].extend([""]*(numRows-len(arr[-1])))
        a = np.array(arr)
        a = a.transpose()
        a = list(a.flatten())
        a = [i for i in a if a != ""]
        return "".join(a)
