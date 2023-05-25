class LongestSubstringWithoutRepeatingCharacters:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charToIndex = {}
        maxLen = 0
        currStart = 0

        for i in range(len(s)):
            if s[i] in charToIndex:
                if(charToIndex[s[i]] >= currStart):
                    length = i - currStart
                    currStart = charToIndex[s[i]] + 1
                    if length > maxLen:
                        maxLen = length
            charToIndex[s[i]] = i

        if maxLen < len(s) - currStart:
            return len(s) - currStart
        return maxLen
