class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t1_cost = math.inf
        t2_cost = math.inf
        t1_profit, t2_profit = 0, 0
        
        for price in prices:
            t1_cost = min(t1_cost, price)
            t1_profit = max(t1_profit, price - t1_cost)
            
            t2_cost = min(t2_cost, price - t1_profit)
            t2_profit = max(t2_profit, price-t2_cost)
            # print(price, "|" ,t1_cost, t1_profit, t2_cost, t2_profit)
        return t2_profit
