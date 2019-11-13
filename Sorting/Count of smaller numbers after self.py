"""
Given an array of integers A, find and return new integer array B. B array has the property where B[i] is the number of smaller elements to the right of A[i]. 
Input Format
The only argument given is the integer array A.
Output Format
Return the new integer array B.
Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 10^9 
For Example
Input 1:
    A = [1, 5, 4, 2, 1]
Output 1:
    B = [0, 3, 2, 1, 0]

Input 2:
    A = [5, 17, 100, 11]
Output 2:
    B = [0, 1, 1, 0]
    """
class Items:
    def __init__(self, val, index):
        self.val = val
        self.idx = index
    def __str__(self):
        return "val:"+str(self.val)+"idx:"+str(self.idx)

def mergeSort(items, start, end,count):
    if start<end:
        mid = (start+end)//2
        mergeSort(items, start, mid,count)
        mergeSort(items, mid+1, end,count)
        merge(items, start, mid, end,count)
        return 

def merge(items, start, mid, end, count):
    right_cnt = 0
    left_array = items[start:mid+1]
    right_array = items[mid+1:end+1]
    i,j = 0, 0
    k = start
    while(i<len(left_array) and j < len(right_array)):
        if left_array[i].val > right_array[j].val:
            right_cnt += 1
            items[k] = right_array[j]
            j += 1
            k += 1
        else:
            count[left_array[i].idx] += right_cnt
            items[k] = left_array[i]
            i += 1
            k += 1
    #print("start:"+str(start)+"mid:"+str(mid)+"end:"+str(end)+"count:"+str(count)+"right_cnt:"+str(right_cnt))        
    while(i<len(left_array)):
        #print("left_array[i].idx"+str(left_array[i].idx))
        count[left_array[i].idx] += right_cnt
        items[k] = left_array[i]
        i += 1
        k += 1
    while(j < len(right_array)):
        items[k] = right_array[j]
        j += 1
        k += 1
    return 
            
    
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        items = [0]*len(A)
        count = [0]*len(A)
        for i in range(len(A)):
            items[i]  = Items(A[i], i)
        mergeSort(items, 0, len(A)-1, count)
        return count
        
        
        
