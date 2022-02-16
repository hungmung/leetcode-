class Solution {
public:
    int maxArea(vector<int>& height) {
      """
      You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

      Find two lines that together with the x-axis form a container, such that the container contains the most water.

      Return the maximum amount of water a container can store.
      """
        maxVol = 0
        # Get a list of the unique heights, sorted from highest to lowest.  we will then traverse this lest going down in height
        # We will also need to remove any zero heights
        sheight = reversed(list(set(height)))
        try:
            sheight.remove(0)
        except:
            pass
        
        
        for h in sheight:
            #  Find the 1st and last index of heights equal to or
            # greater than this value
            thisleft = height.index(next(filter(lambda x: x>=h, height)))
            thisright = len(height) - rheight.index(next(filter(lambda x: x>=h, rheight))) - 1
            if thisleft==thisright: continue
            v = h*(thisright-thisleft)
            if v>maxVol: maxVol = v
        return macVal
    }
};
