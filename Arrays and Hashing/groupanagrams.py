from typing import List
from collections import defaultdict

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for string in strs:
            key = tuple(sorted(string))
            group[key].append(string)
        return list(group.values())
    
ob = Solution()
print(ob.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

# We have a list of strings with a return type of a list with a list of strings. We initialize a defaultdict list and then we iterate through all the strings in the list. We want to use a key for unique strings so we sort the characters of the string into a list and convert it to tuple. A List is mutable in python and cannot be used as a key. We then append strings to the group using the key and then return the list of values. 

# Time Complexity: O(NKlogK) as we are iterating through the list of strings and multiplying it with time complexity of sorting algorithm 
# Space Complexity: O(NK) as we are storing a list of list of strings, basically a 2D list. 
        