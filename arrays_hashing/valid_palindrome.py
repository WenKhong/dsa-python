def isPalindrome(s):  
    # Convert to lowercase and remove non-alphanumeric characters in the string
    s = ''.join(c.lower() for c in s if c.isalnum())
    
    # Check if the converted string is equal to its reverse
    return s == s[::-1] 

# Example usage:
print(isPalindrome("A man, a plan, a canal: Panama"))  # True
print(isPalindrome("race a car"))  #False