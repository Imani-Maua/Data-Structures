
def lengthOfLongestSubstring(s):
        max_len = float('-inf')
        freq = {}
        left = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            while freq[s[right]] > 1:
                 max_len = max(max_len, right - left)
                 freq[s[left]] -= 1
                 left+= 1
        return max_len

s = "pwwkew"
print(lengthOfLongestSubstring(s))