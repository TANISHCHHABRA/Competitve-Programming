class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp_pre=[0]*3
        dp_cur=[0]*3
        #corner cases
        dp_pre[0]=0    #无票，自由期
        dp_pre[1]=-prices[0]   #有票
        dp_pre[2]=0  #无票，空窗期
      
        for i in range(1,len(prices)):
            dp_cur[0]=max(dp_pre[0],dp_pre[2])
            dp_cur[1]=max(dp_pre[1],dp_pre[0]-prices[i])
            dp_cur[2]=dp_pre[1]+prices[i]
            
            dp_pre=dp_cur[:]
            
        return max(dp_pre[0],dp_pre[2])
