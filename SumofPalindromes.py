#check if Base 10 is palindrome
def palindrome_decimal(num):
    a = str(num) 
    return a == a[::-1]


#check if Base 2 is palindrome
def palindrome_binary(num):
    a = str(bin(num))[2:]
    return a == a[::-1]

# Returns true if both bases are plaindrome
def check_palindrome(num):
    return palindrome_decimal(num) and palindrome_binary(num)

#calculates the sum of palindrome
def sum_of_palindrome(lower_limit, upper_limit):
    return sum(x for x in range(lower_limit, upper_limit+1) if check_palindrome(x))
    
print('sum of numbers less than 1 million that are palindrome in both bases is:\n',sum_of_palindrome(1,1000000))
