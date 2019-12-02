"""
Stairs
You are climbing a stair case and it takes A steps to reach to the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? 
 Input Format:
The first and the only argument contains an integer A, the number of steps.
Output Format:
Return an integer, representing the number of ways to reach the top.
Constrains:
1 <= A <= 36
Example : Input 1:
A = 2
Output 1:
2
Explanation 1:
[1, 1], [2]
Input 2:
A = 3
Output 2:
3
Explanation 2:
[1 1 1], [1 2], [2 1]
"""
class Solution:
	# @param A : integer
	# @return an integer
	def climbStairs(self, A):
        
        climb = [0]*(A+2)
        climb[1] = 1
        climb[2] = 2
        
        if A <=2:
            return climb[A]
        for i in range(3, A+1):
            climb[i] = climb[i-1] + climb[i-2]
        return climb[A]
