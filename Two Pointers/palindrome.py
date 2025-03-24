# Input: s = "A man, a plan, a canal: Panama"
# Output: true

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char.lower() for char in s if char.isalnum()]
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left]!=s[right]:
                return False
            left += 1
            right -= 1
        return True
    
# First we convert characters of string into lower case and remove all punctuation and spaces. Take 2 pointers left and right. We need to compare left and right. Take left = 0 and right = len(s) - 1. While left is lesser than right check if s[left]!=s[right]. If they aren't equal then return False. Increment left and decrement right every iteration. Here we are checking if both the halves of the string are equal.

# Time Complexity: O(N) as we convert characters to usable format and iteration through the while loop. 
# Space Complexity: O(N) to change the characters and store it in s.