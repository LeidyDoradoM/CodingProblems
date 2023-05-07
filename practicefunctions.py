# more practice in recursion functions ...Practice 2
import math

def reverse(strng):
    if len(strng) == 1:
        return strng
    else:
        middle = len(strng)/2
        if ~middle.is_integer():
            middle = math.floor(middle)
        L = reverse(strng[:middle])
        R = reverse(strng[middle:])
        return R+L

def palindrome(strng): 
    output = reverse(strng)
    if strng == output:
        return True
    else:
        return False

def Ispalindrome(strng):  #without using reverse function
    if len(strng) == 1:
        return True
    if strng[0] != strng[len(strng)-1]:
        return False
    else:
        return Ispalindrome(strng[1:-1])

# print(palindrome('amanaplanacanalpandemonium'))

def isOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True

def somerecursive(arr,cb):
    n = len(arr)
    if n == 1:
        print(arr[0])
        return cb(arr[0])
    else:
        print(arr[1:])
        out = cb(arr[0]) or somerecursive(arr[1:],cb)
        return out

#print(somerecursive([2,4,6],isOdd))

def flatten(A):
    b = []
    for item in A:
        if type(item) is list:
            b.extend(flatten(item))
        else:
            b.append(item)
    return b

print(flatten([1,2,[3, 4],5]))