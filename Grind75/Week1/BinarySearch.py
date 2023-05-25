class BinarySearch:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)

        while(lo < hi):

            mid = (lo + hi)//2
            comp = nums[mid] - target

            if not comp: # If nums[mid] == target
                return mid
            elif comp > 0: # If nums[mid] > target
                hi = mid
            else:
                lo = mid + 1
                 
        return -1
