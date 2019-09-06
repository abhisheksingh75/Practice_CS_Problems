"""
N/3 Repeat Number
You're given a read only array of n integers. Find out if any integer occurs more than n/3 times in the array in linear time and constant additional space. If so, return the integer. If not, return -1. If there are multiple solutions, return any one. Example :
Input : [1 2 3 1 1]
Output : 1 
1 occurs 3 times which is more than 5/3 times. 

""""
#moore's voting algoritm 
from math import ceil
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        number1,count1, number2, count2 = 1<<32,0,1<<32,0, 
        
        for i in range(len(A)):
            if number1 == A[i]:
                count1 +=1 
            elif number2 == A[i]:
                count2 += 1
            elif count1 == 0:
                number1 = A[i]
                count1 += 1
            elif count2 == 0:
                number2 = A[i]
                count2 += 1
            else:
                count1 -=1 
                count2 -=1
            
        count1, count2 = 0, 0
        for i in range(len(A)):
            if number1 == A[i]:
                count1 += 1
            elif number2 == A[i]:
                count2 += 1
        if count1 >len(A)/3:
            return number1
        elif count2 > len(A)/3:
            return number2
        else:
            return -1
