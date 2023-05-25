class ValidPalindrome:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while(True):
            while(l < len(s)-1 and not s[l].isalnum()):
                l+=1
            while(r > 0 and not s[r].isalnum()):
                r-=1
            if(l > r):
                return True
            elif (s[l].upper() == s[r].upper()):
                l+=1
                r-=1
            else:
                return False
        return True
