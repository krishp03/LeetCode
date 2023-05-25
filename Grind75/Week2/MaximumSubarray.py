class MaximumSubarray:
    def maxSubArray(self, nums: List[int]) -> int:
        overallMax = nums[0]
        lastMax = nums[0]
        for i in range(1, len(nums)):
            if lastMax < 0:
                lastMax = nums[i]
            else:
                lastMax += nums[i]

            if overallMax < lastMax:
                overallMax = lastMax
        
        return overallMax
        
