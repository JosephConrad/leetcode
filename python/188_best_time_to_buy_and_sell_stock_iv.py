from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        length = len(prices)
        if length < 2:
            return 0
        max_profit = 0
        
        if k>=length/2:
            for i in range(1,length):
                max_profit += max(prices[i]-prices[i-1],0)
            return max_profit

        MAX = 1000000000
        b = [MAX] * k
        s = [0] * k

        for price in prices:
            for i in range(k):
                b[i] = min(b[i], price - (s[i-1] if i>0 else 0))
                s[i] = max(s[i], price - b[i])   
        return s[-1] if k > 0 else 0



if __name__ == "__main__": 
    print(Solution().maxProfit(prices=[2,4,1], k=2))
    print(Solution().maxProfit(prices=[3,2,6,5,0,3], k = 2))