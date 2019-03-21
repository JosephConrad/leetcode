import numpy as np
from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int: 
        maxDays = days[-1] + 1
        dp = [0 for _ in range(maxDays)]

        def calcCost(dp, i): 
            return min(dp[max(0,i-1)]+costs[0], 
                       dp[max(0,i-7)]+costs[1], 
                       dp[max(0,i-30)]+costs[2])
 
        for day in range(1, maxDays): 
            dp[day] = calcCost(dp, day) if day in days else dp[day-1] 
 
        return dp[-1] 

if __name__ == "__main__":
    print(Solution().mincostTickets(days=[1,4,6,7,8,20], costs=[2,7,15]))