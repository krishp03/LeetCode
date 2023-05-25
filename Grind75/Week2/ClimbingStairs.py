class ClimbingStairs:
    def climbStairs(self, n: int) -> int:
        last = 1
        curr = 1
        for i in range(1, n):
            tmp = curr
            curr = last+curr
            last = tmp   
        return curr
