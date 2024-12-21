class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        # Initialize variables
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []
        
        # Loop until both strings are processed
        while i >= 0 or j >= 0 or carry:
            # Get the current digits (if the index is valid, else treat as 0)
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0
            
            # Add digits and carry
            total = digit1 + digit2 + carry
            
            # Calculate new carry and the digit to append
            carry = total // 10
            result.append(str(total % 10))
            
            # Move to the previous digit
            i -= 1
            j -= 1
        
        # Reverse the result and convert to string
        return ''.join(result[::-1])


        