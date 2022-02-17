class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      """
      find the longest common prefix string amongst an array of strings.
      If there is no common prefix, return an empty string 
      "".
      """
        if len(strs)==0: return ""
        if len(strs) == 1: return strs[0]
        strs = sorted(strs, key=len)
        shortest_word = min(strs, key=len)
        if len(shortest_word)==0: return ""
        i=0
        while all(map(lambda x: x[i]==shortest_word[i], strs)):
            i += 1
            if i == len(shortest_word): break
        return shortest_word[0:i]
