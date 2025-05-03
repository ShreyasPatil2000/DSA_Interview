class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m:
            return False
        if s1 in s2:
            return True
        s1_count, window_count = [0] * 26, [0] * 26
        for c in s1:
            s1_count[ord(c) - ord('a')] += 1
        for i in range(m):
            window_count[ord(s2[i]) - ord('a')] += 1
            if i >= n:
                window_count[ord(s2[i - n]) - ord('a')] -= 1
            if window_count == s1_count:
                return True
        return False
 
 
ob = Solution()
print(ob.checkInclusion("ab", "eidboaoo"))
    
# We check length of both strings and if s1 is longer than s2 then return False. If s1 is in s2 then return True. Take 2 lists to store frequency of characters in s1 and window. It will be of length 26 assuming that everything is lowercase. We calculate frequency using count[ord(char) - ord('a)] += 1. For string s1 do it using for loop. For s2 run an iteration loop and count up the characters. If i >= n, then decrease count by 1. If window count is equal to count of string s1 then return True. return False at end if not true.
    
# Time Complexity: O(N)
# Space Complexity: O(1)