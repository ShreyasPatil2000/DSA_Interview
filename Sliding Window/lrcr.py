class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res, l = 0, 0
        maxf = 0
        count = {}
        for r, char in enumerate(s):
            count[char] = count.get(char, 0) + 1
            maxf = max(maxf, count[char])
            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
    
ob = Solution()
print(ob.characterReplacement("ABAB", 2))

# We initialize variables result, maxf, l and dictionary count. We run an enumerate loop and we calculate frequency of each character. Next we compare max frequency using maxf = max(maxf, count[char]). If the length of substring(r - l + 1) - maxf is greater than number of replacements(k), then we shift left pointer to next character and reduce frequency of character at left pointer. The result is max(result, length of substring). We return the result in the end.
 
# Time Complexity: O(N) As we are running a for loop. The operations inside only take O(1) time complexity
# Space Complexity: O(1) It will be O(26) as we are updating count for uppercase characters only so round it off to O(1)