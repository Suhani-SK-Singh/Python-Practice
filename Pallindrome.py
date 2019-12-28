
#Student name : Suhani
#Student number: 119220491

    ##This python function checks, if given string is pallindrome or not.
    #All(non-letters (spaces, punctuation etc.) are ignored and no distinction is made betweenupper and lowercase letters)

    #Arguments:
    #s : Any string
    
    #Return:
    #True-if string is pallindrome
    #False-if string is not Pallindrome
    

def is_Palindrome(s):
    ralpha = ''.join(i for i in s if i.isalpha())
    lcase = ralpha.lower()
    reverse = lcase[::-1]  

    if (lcase == reverse):
        return True
    return False

