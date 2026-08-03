class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        n = len(heights)
        right = n-1
        ans = 0

        while left < right :
            width = right - left
            height = min(heights[right], heights[left])
            curr = width * height
            
            ans = max(curr, ans)

            if heights[right] > heights[left] :
                left += 1
            else :
                right -= 1

        return ans