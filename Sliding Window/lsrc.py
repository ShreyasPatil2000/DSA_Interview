class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxl, l = 0, 0
        charset = set()
        for r, char in enumerate(s):
            while char in charset:
                charset.remove(s[l])
                l += 1
            charset.add(char)
            maxl = max(maxl, r - l + 1)
        return maxl
        
    
ob = Solution()
print(ob.lengthOfLongestSubstring("abcabcbb"))

# We take a set in which we store the characters of the substring that has the longest length without repeating characters. We initialize 2 variables, left(l) and maxlength(maxl). We use enumerate in for loop and right(r) as index. We add char to the set and calculate maxl = max(maxl, r - l + 1) at every iteration. When the character is repeated, we take a while loop and remove s[l] from charset and increment l pointer.

# Time Complexity: O(N) as there is only 1 for loop. The other loop inside it runs in constant time. The other operations don't take much time
# Space Complexity: O(N) as we have to store characters in a set, worst case is n. 