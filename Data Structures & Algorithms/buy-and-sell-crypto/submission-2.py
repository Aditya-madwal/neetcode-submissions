class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        n = len(prices)
        # for i in range(n) :
        #     for j in range(i+1, n) :
        #         if prices[j] > prices[i] :
        #             profit = prices[j] - prices[i]
        #             ans = max(ans, profit)
        # return ans

        left = 0
        right = 1

        while right < n :
            present = prices[left]
            future = prices[right]
            profit = future - present

            if profit > 0 :
                ans = max(profit, ans)
            else :
                left=right  # left sirf tab badhana h jab loss hora ho , cuz then we have a new negative peak. so this previous low would not matter anyway 
            right += 1 # right toh badhana hi hai har baar.
        
        return ans
        
