class RansomNote:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        noteCounts = [0]*26
        magCounts = [0]*26

        for char in ransomNote:
            noteCounts[ord(char)-ord('a')]+=1
        for char in magazine:
            magCounts[ord(char)-ord('a')]+=1

        for i in range(len(noteCounts)):
            if noteCounts[i] > magCounts[i]:
                return False
        return True
