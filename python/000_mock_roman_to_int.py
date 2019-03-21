from collections import OrderedDict

class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = OrderedDict([
            ('I', 1),
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000), 
        ])
        lastVal = mapping[s[-1]]
        result = 0
        for char in reversed(s): 
            currVal = mapping[char]
            result = result + (-currVal if currVal < lastVal else currVal) 
            lastVal = currVal
        return result 
        
if __name__ == "__main__":
    print(Solution().romanToInt("MCMXCIV"))
