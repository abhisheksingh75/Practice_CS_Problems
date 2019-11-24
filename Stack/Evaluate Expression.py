"""
valuate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression. 
Input Format
The only argument given is character array A.
Output Format
Return the value of arithmetic expression formed using reverse Polish Notation.
For Example
Input 1:
    A =   ["2", "1", "+", "3", "*"]
Output 1:
    9
Explaination 1:
    starting from backside:
    *: ( )*( )
    3: ()*(3)
    +: ( () + () )*(3)
    1: ( () + (1) )*(3)
    2: ( (2) + (1) )*(3)
    ((2)+(1))*(3) = 9

Input 2:
    A = ["4", "13", "5", "/", "+"]
Output 2:
    6
Explaination 2:
    +: ()+()
    /: ()+(() / ())
    5: ()+(() / (5))
    1: ()+((13) / (5))
    4: (4)+((13) / (5))
    (4)+((13) / (5)) = 6
    """
    class Solution:
	# @param A : list of strings
	# @return an integer
	def evalRPN(self, A):
        stack = []
        for i in range(len(A)):
	        
            if A[i] in ['+','-','/','*']:
                op2 = stack.pop()
                op2 =  int(op2)
                op1 = stack.pop()
                op1 = int(op1)
                if A[i] == '+':
                    stack.append(op1+op2)
                elif A[i] == '-':
                    stack.append(op1-op2)
                elif A[i] == '/':
                    stack.append(op1//op2)
                else:
                    stack.append(op1*op2)
            else:
                stack.append(A[i])
                
        return stack.pop()
                
        
            
