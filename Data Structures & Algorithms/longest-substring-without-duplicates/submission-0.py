class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        vis = {}
        ans = 0

        while right < len(s):
            ch = s[right]

            while ch in vis and vis[ch] == 1:
                vis[s[left]] = 0
                left += 1

            vis[ch] = 1
            ans = max(ans, right - left + 1)
            right += 1

        return ans