# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class FirstBadVersion:
    def firstBadVersion(self, n: int) -> int:
        min = 1
        max = n
        while min != max:
            guess = (max+min)//2
            if isBadVersion(guess):
                max = guess 
            else:
                min = guess + 1
        return max
        
