# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas=0
        total_cost=0
        acc=0
        start=0
        for i in range(len(gas)):
            total_gas+=gas[i]
            total_cost+=cost[i]
            acc+=gas[i]-cost[i]
            if acc<0:
                start=i+1 
                acc=0 
        if total_gas<total_cost:
            return -1
        return start
