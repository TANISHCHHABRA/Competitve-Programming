class Solution:
    def reverseBits(self, n: int) -> int:
        l = bin(n)[2:]
        l = (32 - len(l))*'0' + l
        l = l[::-1]
        return int(l,2)
