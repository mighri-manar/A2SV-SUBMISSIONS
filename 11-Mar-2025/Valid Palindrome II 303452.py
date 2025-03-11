# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        count = 0
        i = 0
        n = len(s)
        while i < n // 2:
            if s[i] != s[n - 1 - i]:
                s1 = s[:i] + s[i+1:]  
                s2 = s[:n-1-i] + s[n-i:] 
                return s1 == s1[::-1] or s2 == s2[::-1]  
            i += 1
        return True  

