class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = l = 0
        freqs = defaultdict(int)
        for r in range(len(s)):
            freqs[s[r]] += 1
            max_freq = max(freqs.values())
            cur_len = r - l + 1
            if cur_len - max_freq > k:
                freqs[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res