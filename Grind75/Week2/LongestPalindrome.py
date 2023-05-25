class LongestPalindrome:
    def longestPalindrome(self, s: str) -> int:
        freq = {i: s.count(i) for i in set(s)}
        count = 0
        oddUsed = False
        for val in freq.values():
            if val % 2 == 1:
                count += val-1
                oddUsed = True
            else:
                count += val
        
        return count + 1 if oddUsed else count
