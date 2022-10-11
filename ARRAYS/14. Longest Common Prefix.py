
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 2:
            return strs[0] 
        strs.sort()
        a = strs[0]
        b=strs[-1]
        ss = ''
        i = 0
        n = min(len(a), len(b)) 
        while i < n and a[i] == b[i]:
            ss += a[i]
            i +=1
        return ss
