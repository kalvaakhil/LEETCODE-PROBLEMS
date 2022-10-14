#https://practice.geeksforgeeks.org/problems/perfect-sum-problem5633/1?page=3&difficulty[]=1&status[]=unsolved&sortBy=submissions
class Solution:
	def perfectSum(self, A, N, S):
	    def _get(i, j): 
	    	return dp[i][j] if i>=0 else 0	    
		dp = [ [0] * (N+1) for _ in range(S+1) ]
		dp[0][0] = 1
		for i in range(S+1):
		    for j in range(1, N+1):
		        dp[i][j] = (dp[i][j-1] + _get(i-A[j-1], j-1)) %( 10**9+7)
		return dp[S][N]
