class Solution:
    def findComplement(self, num: int) -> int:
        s = bin(num).replace("0b", "")
        s = str(s)
        a = ""
        for i in s:
            if i =='1':
                a = a + '0'
            else:
                a = a + '1'
        return(int(a,2))
