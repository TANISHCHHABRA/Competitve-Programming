class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h = 30*hour + 0.5*minutes
        m = 6*minutes
        d = abs(h-m)
        if d <= 180:
            return d
        return 360-d
