class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            if len(digits) == 1:
                digits.pop(0)
                digits.append(1)
                digits.append(0)
            else:
                count = 0
                while digits[-1] == 9:
                    digits = digits[:-1]
                    count += 1
                    if len(digits) == 0:
                        break
                if len(digits) != 0:
                    digits[-1] += 1
                else:
                    digits.append(1)
                for i in range(count):
                    digits.append(0)
        else:
            digits[-1] += 1
        return digits
