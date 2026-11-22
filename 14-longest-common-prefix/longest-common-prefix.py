class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        pre = strs[0]
        for i in range(1,len(strs)):
            if strs[i].startswith(pre):
                continue
            else:
                while not strs[i].startswith(pre):
                    pre = pre[:-1]
        return pre