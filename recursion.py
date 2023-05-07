# functions that using a recursive approach for solving problems
# practicing interview questions - following Udemy course
# September 2022

def factorial(n): #Compute the factorial of an integer number
    if n<=0 or int(n)!=n:
        print('The number must be positive integer only!')
    else:
        if n in [0,1]:
            return 1
        else:
            return n*factorial(n-1)

def fibonacci(n): #Compute the fibonnaci serie of an integer number
    if n <=0 or int(n)!= n:
        print('The number must be positive integer only!')
    else:
        if n in[0,1]:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

def sumDigits(n): #Compute the sum of digits of a given integer number
    assert n >=0 and int(n)==n, 'The number must be positive integer only!'
    if n == 0:
        return 0
    else:
        return int(n%10) + sumDigits(int(n/10))

def power(base,exp):#Compute the exponential of a number
    assert int(exp)==exp, 'The exponent must be an integer number only!'
    if exp == 0:
        return 1
    elif exp < 0:
        return 1/power(base,exp+1)
    return base*power(base,exp-1)

def gcd(a,b): #Compute the Greatest Common Divisor of two numbers
    # This solution uses the Euclidean algorithm formula
    assert int(a) == a and int(b)== b, 'The numbers must be integers!'
    if a < 0:
        a = -1*a
    if b < 0:
        b = -1*b
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def decimal2binary(n): #Convert a decimal number to its binary
    assert int(n) == n, 'The parameter must be an integer number'
    if n == 0:
        return 0
    else:
        return n%2 + 10*decimal2binary(int(n/2))

print(gcd(18,48))
a = [1,2,3]
n = len(a)
print(a[n-1])

