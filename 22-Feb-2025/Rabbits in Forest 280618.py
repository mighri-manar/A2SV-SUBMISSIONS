# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count=Counter(answers) 
        total=0
        
        for k, freq in count.items():
            groups=math.ceil(freq / (k + 1)) 
            total+=groups * (k + 1)  

        return total