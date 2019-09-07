"""
Given three integers A, B and C, find and return the day of the week for the given date A/B/C where A represents the date, B represents the month and C represents the year. Assume that Jan 1st 1 AD is a Monday in Gregorian calendar. February has 28 days(excluding leap years when it has 29 days). Leap year is a year that is either (divisible by 400) or (divisible by 4 and not divisible by 100). 
Input Format
The 3 arguments given are the integers A, B and C.
Output Format
Return the day of the year as a string of lower case english alphabets.
Answer will be one of the following {sunday, monday, tuesday, wednesday, thursday, friday, saturday}.
Constraints
1 <= A <= 31
1 <= B <= 12
1990 <= C <= 2100
For Example
Input 1:
    A = 19
    B = 4
    C = 2019
Output 1:
    friday

Input 2:
    A = 7
    B = 10
    C = 1996
Output 2:
    monday
"""
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return a strings
    def solve(self, A, B, C):
        no_of_days = 0
        year,month,day = C,B,A
        days_in_week = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
        days_in_month = [31,28,31,30,31,30,31,31,30,31,30,30]
        #add previous year
        no_of_days = (year-1)*365
        leap_days = ((year-1)//4 - (year-1)//100 + (year-1)//400)
        no_of_days  = no_of_days + leap_days
        
        if((year%400 == 0) or (year%100 != 0 and year%4 == 0)):
            days_in_month[1] = 29
        
        
        for i in range(month-1):
            no_of_days += days_in_month[i]
        
        no_of_days += day
        
        
        return days_in_week[(no_of_days)%7]
        
            
