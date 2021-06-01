class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        A = int(a,2)
        B = int(b,2)
        
        result = A + B
        
        result_ = format(result, 'b')
        
        return result_
        
        
        
        
        