class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freqs = {}
        maxfreq = 0
        ans = 0

        for right in range(len(s)):
            char = s[right]
            freqs[char] = freqs.get(char, 0) + 1

            maxfreq = max(maxfreq, freqs[char])

            while right - left + 1 - maxfreq > k:
                freqs[s[left]] -= 1
                left += 1

                maxfreq = max(freqs.values(), default=0)

            ans = max(ans, right - left + 1)

        return ans