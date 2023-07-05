input=input("Enter a word: ")

def print_not_palindrome():
    print(f"{input} is not a palindrome.")

def print_palindrome():
    print(f"{input} is a palindrome.")

#with list
list = [*input]
reverse= [*input]
reverse.reverse()
if list == reverse:
    print(f"{input} is a palindrome.")
else:
    print(f"{input} is not a palindrome.")

#with string
str = input
str_reverse = input[::-1] #[::-1] reverses a string
if str == str_reverse:
    print(f"{input} is a palindrome.")
else:
    print(f"{input} is not a palindrome.")

#smart way
str = input
str_length = len(str)
isPalindrome = True
for i,j in zip(range(str_length), range(str_length-1,-1,-1)):
    if str[i] != str[j]:
        isPalindrome = False
        break
if isPalindrome == True:
    print_palindrome()
elif isPalindrome == False:
    print_not_palindrome()