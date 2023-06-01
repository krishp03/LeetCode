class HouseRobber:
    def rob(self, nums: List[int]) -> int:
        lastMax = 0
        nonAdjMax = 0
        
        for num in nums:
            temp = nonAdjMax + num
            nonAdjMax = lastMax if(nonAdjMax < lastMax) else nonAdjMax
            lastMax = temp
        
        return max(lastMax, nonAdjMax)
