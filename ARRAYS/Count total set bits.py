#https://practice.geeksforgeeks.org/problems/count-total-set-bits-1587115620/1?page=2&difficulty[]=1&status[]=unsolved&sortBy=submissions
class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):
        # code here
        # return the count
        c=0
        b=1
        i=1
        while(b>0):
            a=2**i
            d=2**(i-1)
            x=(n+1)//a
            y=(n+1)%a
            if y>d:
                b=x*d+y-d
                c=c+b
            else:
                b=x*d
                c=c+b
            i=i+1
        return c
