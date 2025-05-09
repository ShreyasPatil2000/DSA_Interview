from typing import List

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        Tcount, window = {}, {}
        for c in t:
            Tcount[c] = 1 + Tcount.get(c, 0)
        have, need, l = 0, len(t), 0 
        result, reslen = [-1, -1], float('inf')
        for r, char in enumerate(s):
            if char in Tcount:
                window[char] = 1 + window.get(char, 0)
                if window[char] <= Tcount[char]:
                    have += 1
            while have == need:
                if (r - l + 1) < reslen:
                    result = [l, r]
                    reslen = r - l + 1
                if s[l] in window: 
                    window[s[l]] -= 1
                    if window[s[l]] < Tcount[s[l]]:
                        have -= 1
                l += 1
        l, r = result
        if reslen != float('inf'):
            return s[l: r + 1]
        else:
            return ""
                
    
ob = Solution()
print(ob.minWindow("ADOBECODEBANC", "ABC"))

# If the length of t is greater than the length of s then we have to return "". Then we initialize have and need(is length of string t) variables along with left pointer. We initialize result and reslen as well. We use a for loop to store all frequencies of t in a dictionary Tcount. In another for loop, check if the characters in the string are in the window. If they are in the window then put it into the array and check if frequency of that character is less than or equal to Tcount frequency, then increment have. Use a while loop for have == need, check if length of window r - l + 1 < reslen, if it is then update result and reslen. If s[l] is in window then decrement the frequency. Check if the frequency there is less than the Tcount frequency and decrement have. Increment left pointer as we are moving one point forward. Store result in l, r and return s[l: r + 1] if the reslen != float('inf), else return "". 

# Time Complexity: O(N) for loops and dictionaries take up that much time complexity
# Space Complexity: O(N) storing the the dictionaries takes that much space