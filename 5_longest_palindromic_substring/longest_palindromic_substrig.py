class Solution:
    
    def get_palindrome(self, idx, s, centered=False):
        palindrome = ''
        
        # Set the seed indices
        x = idx-1
        y = idx
        if centered:
            y = idx+1
            palindrome = s[idx]
           
        for i in range(500):  # 500: as the max length is 1000
            if (x-i >= 0) and (y+i < len(s)) and s[x-i] == s[y+i]:
                palindrome = s[x-i] + palindrome + s[y+i]
            else:
                break
                
        return palindrome 
    
    def longestPalindrome(self, s: str) -> str:
        
        palindrome = s[0] if s else ''
        buffers = []
        for idx in range(1, len(s)-1):
            # Detect the two type of centers of palindrome
            if s[idx-1] == s[idx]:
                buffers.append(self.get_palindrome(idx, s))
            if s[idx-1] == s[idx+1]:
                buffers.append(self.get_palindrome(idx, s, centered=True))
                
        # Handle the border case
        if len(s)>=2 and s[-1] == s[-2]:
            buffers.append(s[-2] + s[-1])
            
        # Find the longest
        for buffer in buffers:
            if len(buffer) > len(palindrome):
                palindrome = buffer
                
        return palindrome