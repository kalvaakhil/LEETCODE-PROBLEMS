#https://practice.geeksforgeeks.org/problems/valid-substring0624/1?page=3&difficulty[]=1&status[]=unsolved&sortBy=submissions

class Solution:
    def findMaxLen(ob, S):
        s=[-1]
        l=0
        for i in range(len(S)):
            if(S[i]=="("):
                s.append(i)
            else:
                if s:
                    s.pop()
                if not s:
                    s.append(i)
                else:
                    l=max(l,i-s[-1])
        return l
