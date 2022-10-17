#https://practice.geeksforgeeks.org/problems/check-if-two-strings-are-k-anagrams-or-not/1?page=1&status[]=unsolved&curated[]=3&sortBy=submissions
class Solution:
    def areKAnagrams(self, str1, str2, k):
        cnt=0
        if len(str1)==len(str2):
            for i in str1:
                if i not in str2:
                    cnt+=1
                else:
                    str2=str2.replace(i,"",1)
            if cnt<=k:
                return True
            return False
        else:
            return False
