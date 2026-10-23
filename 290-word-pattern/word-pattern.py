class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.strip().split()
        if len(pattern) != len(words):
            return False
        d = {}
        for i in range(len(pattern)):
            ch = pattern[i]
            word = words[i]
            if ch in d:
                if d[ch] != word:
                    return False
            else:
                if word in d.values():
                    return False
                d[ch] = word
        return True