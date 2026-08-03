class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n-1

        ans = []

        while left < right :
            currsum = numbers[left] + numbers[right]

            if currsum == target :
                ans = [left+1, right+1]
                return ans
            elif currsum < target :
                left+= 1
            else :
                right -= 1
        
        return ans