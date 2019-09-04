"""https://www.interviewbit.com/problems/largest-number/
Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""
class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        A = list(A)
        sorted_array = self.quicksort(A)
        largest_number = ''
        for ele in A:
            largest_number += str(ele)        
        return int(largest_number)

    def quicksort(self, A):
        self.quicksrt(A, 0, len(A)-1)
        return A
  
    def quicksrt(self, array, start, end):
        if start < end and (len(array)-1 >= end):
            pivot_index = self.partition(array, start, end)
            self.quicksrt(array, start, pivot_index-1)
            self.quicksrt(array, pivot_index+1, end)

    
    def partition(self,array, start, end):   
       # array = list(array1)
        if end <= len(array)-1 and start >= 0:        
            pivot_ele =  array[end] 
            p_start = start
            p_end = end-1    
            while(p_start <= p_end):
    #            if(pivot_ele <array[p_start]):
                if(self.my_compare(pivot_ele,array[p_start])== 1):
                    self.swap(array, p_start, p_end)
                    p_end = p_end -1
                else:
                    p_start = p_start + 1
            self.swap(array, end, p_start)
            return p_start


    def swap(self, array, start, end):
        temp = array[start]
        array[start]= array[end]
        array[end] = temp

    def my_compare(self, number_1, number_2):
        if int(str(number_1)+ str(number_2)) > int(str(number_2)+ str(number_1)):
            return 1
        else:
            return -1
        
