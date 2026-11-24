class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        freq1 = {}

        for ch in s1:
            freq1[ch] = freq1.get(ch, 0) + 1

        l = 0
        r = 1

        freq2 = {s2[l]: 1}
        n = len(s2)

        if freq1 == freq2:
            return True

        while r < n:

            freq2[s2[r]] = freq2.get(s2[r], 0) + 1

            if freq1 == freq2:
                return True
            else:
                if len(s1) <= r-l+1:
                    freq2[s2[l]] -= 1

                    if freq2[s2[l]] == 0:
                        del freq2[s2[l]]

                    l += 1

                r += 1

        return False