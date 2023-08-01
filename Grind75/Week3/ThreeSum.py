class ThreeSum:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        n = len(nums)
        i = 0
        while i < n-2:
            l = i + 1
            r = n - 1
            comp = -nums[i]
            while l < r:
                if nums[l] + nums[r] > comp:
                    r -= 1
                elif nums[l] + nums[r] < comp:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    val = nums[l]
                    while l < n and nums[l] == val:
                        l += 1

            val = nums[i]

            while i < n-2 and nums[i] == val: # account for repeated values
                i += 1

        return res
