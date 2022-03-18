"""
Given a string s consists of upper/lower-case alphabets and empty space
characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space
characters only.

For example, Given s = "Hello World",
return 5.
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        p = n - 1
        right = -1
        while p >= 0:
            if right == -1 and s[p] != ' ':
                right = p
            elif right >= 0 and s[p] == ' ':
                return right - p
            p -= 1
        if right >= 0:
            return right + 1
        else:
            return 0
