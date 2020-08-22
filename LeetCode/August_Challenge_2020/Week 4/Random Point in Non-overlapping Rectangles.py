class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.areas = []
        sumarea = 0
        for i in range(len(rects)):
            a = (rects[i][2] - rects[i][0] + 1) * (rects[i][3] - rects[i][1] + 1)
            self.areas.append(a)
            sumarea += a
        #create prefix sum
        for i in range(0, len(self.areas)):
            self.areas[i] /= sumarea
        # print(self.areas)
        for i in range(1, len(self.areas)):
            self.areas[i] += self.areas[i - 1]
        print(self.areas)
    def pick(self) -> List[int]:
        #will pick with probability proportional to area
        p = random.random()
        idx = bisect.bisect_left(self.areas, p)
        r = self.rects[idx]
        x = randint(r[0], r[2])
        y = randint(r[1], r[3])
        return [x, y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
