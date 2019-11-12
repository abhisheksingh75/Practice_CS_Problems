"""
We have a list A, of points(x,y) on the plane. Find the B closest points to the origin (0, 0). Here, the distance between two points on a plane is the Euclidean distance. You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in.) Note: Euclidean distance between two points P1(x1,y1) and P2(x2,y2) is sqrt( (x1-x2)^2 + (y1-y2)^2 ). 
Input Format
The argument given is list A and an integer B.
Output Format
Return the B closest points to the origin (0, 0) in any order.
Constraints
1 <= B <= length of the list A <= 100000
-100000 <= A[i][0] <= 100000
-100000 <= A[i][1] <= 100000
For Example
Input 1:
    A = [   [1, 3],
            [-2, 2]  ]
    B = 1
Output 1:
    [ [-2, 2] ]

Input 2:
    A =[    [3, 3],
            [5, -1],
            [-2, 4]  ]
    B = 2
Output 2:
    [ [3, 3], [-2, 4] ]
  """
  class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, A, B):
        
        #As x2 and y2 will always be zero, eq becomes sqrt( (x1)^2 + (y1)^2 )
        #as all elements square root need to be calculated so we just avoid it. and eq becomes (x1)^2 + (y1)^2
        A.sort(key = lambda X: (X[0]**2)+X[1]**2)
        return A[:B]
