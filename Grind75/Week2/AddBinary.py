class AddBinary:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        pointerA = len(a)-1
        pointerB = len(b)-1
        res = ""

        while pointerA >= 0 or pointerB >= 0 or carry:
            if pointerA >= 0:
                carry += int(a[pointerA])
                pointerA -= 1
            if pointerB >= 0:
                carry += int(b[pointerB])
                pointerB -= 1
            res += str(carry % 2)
            carry //= 2
        
        return res[::-1]
      
