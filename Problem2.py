# Time Complexity: O(n)
# Space Complexity: O(n)
# Accepted on leet code

from collections import Counter
class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        hashmap = Counter()
        n = len(tops)
        candidate = 0
        for i in range(n):
            hashmap[tops[i]] += 1
            if hashmap[tops[i]] >= n:
                candidate = tops[i]
                break
            hashmap[bottoms[i]] += 1
            if hashmap[bottoms[i]] >= n:
                candidate = bottoms[i]
                break
        toprot = bottomrot = 0
        for i in range(n):
            if tops[i] != candidate and bottoms[i] != candidate:
                return -1
            if tops[i] != candidate:
                toprot += 1
            if bottoms[i] != candidate:
                bottomrot +=1
        return min(toprot, bottomrot)
