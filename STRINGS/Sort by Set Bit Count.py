#https://practice.geeksforgeeks.org/problems/sort-by-set-bit-count1153/1?page=1&status[]=unsolved&curated[]=7&sortBy=submissions
class Solution:
    def sortBySetBitCount(self, arr, n):
        # Your code goes here
        dic={}
        for i in range(n):
            num=bin(arr[i]).count('1')
            dic[i]=num
        dic=sorted(dic.items(),key=lambda item:item[1],reverse=True)
        # print(dic)
        li=[]
        for i in dic:
            li.append(arr[i[0]])
        arr[::]=li[::]
