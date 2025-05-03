# here we will check if given number is palindrome or not

# palindrome number  -  n= 7887 - rev(n)=7887 both are same hence this is panlindrome number 

def isPalindrome(num):
    # we will extract each digit and from a new digit and then we will compare them 
    temp =num
    revNumber =0

    while temp!=0:
        #extract digit 
        unitDigit=temp%10

        # add this unit digit to number 
        revNumber= revNumber*10+unitDigit

        #remove unitDigit 
        temp=temp//10

    if num!=revNumber:
         return False

    return True         


print(isPalindrome(121))
