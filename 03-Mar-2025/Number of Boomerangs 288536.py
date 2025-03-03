# Problem: Number of Boomerangs - https://leetcode.com/problems/number-of-boomerangs/description/

class Solution:
    def numberOfBoomerangs(self, points):
        count = 0
        for a,b in points:
            counter = {}
            for x,y in points:
                z = (x-a)**2 + (y-b)**2
                if z in counter:
                    count += 2*counter[z]
                    counter[z] += 1
                else:
                    counter[z] = 1
        return count