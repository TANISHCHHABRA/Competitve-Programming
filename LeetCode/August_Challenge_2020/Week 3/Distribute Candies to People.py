class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0 for _ in range(num_people)]
        i = 0
        a = 0
        while True:
            temp = a+i+1
            if candies < temp:
                temp = candies
            ans[i] += temp 
            candies -= temp
            if candies <= 0:
                break
            i += 1
            if i >= num_people:
                i = 0
                a += num_people
                #print(ans,candies,a)
        return ans
