# Checks if a word is a palindrome

def palindrome(s = None):
    if s == None:
        return False
    # Removes any spaces
    s = str(s)
    newStr = s.split(' ')
    newStr = ''.join(newStr).lower()
    
    if len(newStr) < 2:
        return True
    # Checks if both ends are equal and works its way in
    total = int(len(newStr)/2)
    isPalindrome = True
    for i in range(total):
        if (newStr[i] != newStr[-1*(i+1)]):
            return False
    return True

# word = input('Enter Word: ')
# palindrome(word)
