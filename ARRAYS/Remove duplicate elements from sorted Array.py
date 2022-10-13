#https://practice.geeksforgeeks.org/problems/remove-duplicate-elements-from-sorted-array/1?page=2&category[]=Arrays&sortBy=submissions
class Solution:	
	def remove_duplicate(self, A, N):
	    A[:]=list(set(A))
	    A.sort()
	    return len(set(A))
