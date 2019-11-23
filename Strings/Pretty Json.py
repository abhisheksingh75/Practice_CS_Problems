"""
Given a string A representating json object. Return an array of string denoting json object with proper indentaion. Rules for proper indentaion:
Every inner brace should increase one indentation to the following lines.
Every close brace should decrease one indentation to the same line and the following lines.
The indents can be increased with an additional '\t'
Note:
[] and {} are only acceptable braces in this case.
Assume for this problem that space characters can be done away with.

Input Format
The only argument given is the integer array A.
Output Format
Return a list of strings, where each entry corresponds to a single line. The strings should not have "\n" character in them.
For Example
Input 1:
    A = "{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}"
Output 1:
    { 
        A:"B",
        C: 
        { 
            D:"E",
            F: 
            { 
                G:"H",
                I:"J"
            } 
        } 
    }

Input 2:
    A = ["foo", {"bar":["baz",null,1.0,2]}]
Output 2:
   [
        "foo", 
        {
            "bar":
            [
                "baz", 
                null, 
                1.0, 
                2
            ]
        }
    ]
    """
    class Solution:
    # @param A : string
    # @return a list of strings
    def prettyJSON(self, A):
        indent_count  = 0
        line = ''
        ans = []
        for ele in A:
            
            if ele in '[{':
                if line != '':
                    ans.append(line)
                ans.append('\t'*indent_count+ele)
                #line = '\t'*indent_count+ele
                line = ''
                indent_count += 1
            elif ele in '}]':
                if line != "":
                    ans.append(line)
                indent_count -= 1
                line = '\t'*indent_count + ele #consider case when next ele in ,
            else:
                if line == '':
                    line = '\t'*indent_count
                line += ele
                if ele == ',':
                    ans.append(line)
                    line = ''
        if line != '':
            ans.append(line)
            line = ''
        return ans
        
        
