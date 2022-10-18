#https://practice.geeksforgeeks.org/problems/maximum-occuring-character-1587115620/1?page=2&category[]=Strings&sortBy=submissions
class Solution:
    def getMaxOccurringChar(self,s):
        mapD = {}
        for i in s:
            mapD[i] = 1 + mapD.get(i, 0)
        maxS = 0
        for v in mapD.values():
            if v > maxS:
                maxS = v
        li = []    
        for key in mapD:
            if mapD[key] == maxS:
                li.append(key)
        li.sort()
        return li[0]
