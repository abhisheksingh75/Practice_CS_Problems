def isArrangementPossible(mini_page,A,B):
    tmp_page = 0
    i = 0
    student_Req = 1
    for i in range(len(A)):
        
        if A[i] > mini_page:
            return False
        
        if tmp_page + A[i] > mini_page:
            student_Req += 1
            tmp_page = A[i]
            if student_Req > B:
                return False
    
        else:
            tmp_page += A[i]
            

    return True


import sys
class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def books(self, A, B):
        
        ans = -1
        start, end = 0, 1000
        if len(A) < B:
            return -1
        while(start<=end):
            mid = (start+end)//2
            print("start:"+str(start)+"end:"+str(end)+"mid:"+str(mid)+"isArrangementPossible2(mid,A,B)"+str(isArrangementPossible2(mid,A,B)))
            if isArrangementPossible2(mid,A,B):
                #print("start:"+str(start)+"end:"+str(end)+"mid:"+str(mid))
                ans = mid
                end = mid-1
            else:
                start = mid+1
        return ans
        
