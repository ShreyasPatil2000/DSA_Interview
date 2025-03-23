# Input: s = "anagram", t = "nagaram"

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        counter = {}
        for i in s:
            counter[i] = counter.get(i, 0) + 1
        for i in t:
            if i not in counter or counter[i]==0:
                return False
            counter[i] -= 1
        return True 

ob = Solution()
print(ob.isAnagram("anagram", "nagaram"))

# Here we have 2 strings where we want to check that they are anagrams. Basically, we see if the freqency of characters in s and t is the same. First we check if the length of strings is the same. If it's not then it is not an anagram. We take s and iterate over the characters. Then we store the frequency of each character in the counter. We then iterate over t and check whether the character is in t. We then subtract from the counter if its there. If its not there we return False. If its not False, we return True. 

# Time Complexity: O(N)
# Space Complexity: O(N)