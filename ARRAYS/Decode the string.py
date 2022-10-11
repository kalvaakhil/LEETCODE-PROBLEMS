#https://practice.geeksforgeeks.org/problems/decode-the-string2444/1
class Solution:
    def decodedString(self, s):
        p = ""
        n = 0
        stack = []
        for i in s:
            if i.isdigit():
                n = n * 10 + int(i)
            elif i == '[':
                stack.append((p,n))
                p = ''
                n = 0
            elif i == ']':
                prevp , prevn = stack.pop()
                p = prevp + prevn*p
            else:
                p += i
        return p
