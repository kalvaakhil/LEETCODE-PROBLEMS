#https://practice.geeksforgeeks.org/problems/first-repeating-element4018/1?page=1&status[]=unsolved&category[]=Arrays&sortBy=submissions
class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr, n):
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in arr:
            if(d[i]>1):
                return arr.index(i)+1
        return -1
