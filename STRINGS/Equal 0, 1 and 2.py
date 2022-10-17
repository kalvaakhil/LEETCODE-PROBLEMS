#https://practice.geeksforgeeks.org/problems/equal-0-1-and-23208/1?page=1&status[]=unsolved&curated[]=3&sortBy=submissions
class Solution:

    def getSubstringWithEqual012(self,S):
        my_dic = {(0,0):1}
        z_c,o_c,t_c,count = 0,0,0,0
        for i in range(len(S)):
            if S[i]=='0':z_c+=1
            elif S[i]=="1":o_c+=1
            else:t_c+=1
            temp = (z_c - o_c , z_c - t_c)
            if temp not in my_dic:count+=0
            else:count+=my_dic[temp]
            if temp in my_dic:my_dic[temp]+=1
            else:my_dic[temp] = 1
        return count
