class Solution {
public:
    int maxArea(vector<int>& height) {
      """
      You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

      Find two lines that together with the x-axis form a container, such that the container contains the most water.

      Return the maximum amount of water a container can store.
      """
      from itertools import combinations as combinations
      maxVol = 0
      for v in combinations(range(len(height)), 2):
        v = min([height[v[0]], height[v[1]]]) * (v[1]-v[0])
        if v > maxVol: maxVol=v
      return maxVol
        
    }
};
