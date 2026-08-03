class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        for i in range(len(nums)) :
            left = i+1
            right = len(nums)-1
            while left < right :
                curr = nums[i] + nums[left] + nums[right]
                if curr == 0 :
                    x = [nums[i],nums[left],nums[right]]
                    if x not in ans :
                        ans.append(x)
                    left += 1
                    right -= 1
                elif curr < 0:
                    left += 1
                else :
                    right -= 1
        return ans