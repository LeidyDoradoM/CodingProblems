# From Codewars problems.
# Bit counting -> Write a function that takes an integer as input, and returns the number of bits 
# that are equal to one in the binary representation of that number. You can guarantee that input 
# is non-negative.
# Example: The binary representation of 1234 is 10011010010, so the function should return 5.
def count_bits(n):
    coeff = n
    count = 0
    while coeff >= 1:
        count += coeff%2
        coeff = coeff//2
    return count

print(count_bits(1234))

# Descending order -> function that takes any non-negative integer and returns it with its digits
# in descending order (rearrange the digits to create the highest possible number).
# Example: input: 42145; output: 54421
def descending_order(n):
    myarray = [int(x) for x in str(n)]
    for i in range(len(myarray)):
        for j in range(i+1,len(myarray)):
            if myarray[i] < myarray[j]:
                mini = myarray[i]
                myarray[i] = myarray[j]
                myarray[j] = mini
    newnumber = int(''.join(map(str,myarray)))
    return newnumber

print(descending_order(42145))

# 
def spin_words(sentence):
    words = sentence.split(' ')
    output = str()
    for word in words:
        listword = list(word)
        if len(listword) >= 5:
            for i in range(len(listword)//2):
                j = len(listword)-1-i
                temp = listword[i]
                listword[i] = listword[j]
                listword[j] = temp
            newwords = ''.join(listword)
            output = output+' '+newwords 
        else:
            output = output+' '+word
    output = output.strip()
    return output
print(spin_words('Hey fellow warriors'))

# Find the odd int -> given an array of integers, find the one that appears an odd number of 
# times.  Example: Input - [1,1,2]; Output - 2
def find_it(seq):
    mydict = dict()
    if len(seq) == 1:
        return seq[0]
    elif len(seq) == 2:
        print('this array length is not allowed')
        return
    else:
        for item in seq:
            if mydict.get(item) is not None:
                mydict[item] += 1
            else:
                mydict[item] = 1
        for item in mydict.keys():
            if mydict[item]%2 != 0:
                return item

print(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]))

# split strings -> function that splits a string into pairs of two characters. If the string contains
# an odd # of characters then it should replace the missing record character of the final pair with
# an underscore ("-"). Example: 'abc' -> ['ab','c-']
def splitstring(str):
    output = []
    for i in range(0,len(str),2):
        print(i,len(str))
        if i+1 >= len(str):
            output.append(str[i]+'-')
        else:
            output.append(str[i]+str[i+1])
    return output

print(splitstring('abcdefg'))

def climbStair(n):
    if n == 0 or  n == 1:
        return 1
    else: 
        output= climbStair(n-2) + climbStair(n-1)
        return output

print(climbStair(6)) 

def vert_mirror(s):
    output =[]
    phrase = s.split('\n')
    for item in phrase:
        output.append(item[::-1])
    return '\n'.join(output)

def hort_mirror(s):
    phrase = s.split('\n')
    output = '\n'.join(phrase[::-1])
    return output

s = 'abcd\nefgh\nijkl\nmnop'
print(vert_mirror("hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu"))

def unique_in_order(sequence):
    i = 0
    j = i+1
    output = [sequence[i]]
    while j < len(sequence):
        if sequence[i] != sequence[j]:
            output.append(sequence[j])
            i = j
            j = i+1
        else:
            j = j+1
    return output

sequence = [1,2,2,3,3]
print(unique_in_order(sequence))

init_tuple = ()
print (init_tuple.__len__())

init_tuple_a = 'a', 'b'
init_tuple_b = ('a', 'b')
 
print(init_tuple_b)

init_tuple_a = '1', '2'
init_tuple_b = ('3', '4')
 
print (init_tuple_a + init_tuple_b)

init_tuple = [(0, 1), (1, 2), (2, 3)]
 
result = sum(n for _, n in init_tuple)
 
print(result)

alphabets = 'abcd'
for i in range(len(alphabets)):
    print(alphabets[i].upper())

print(alphabets)

data = ['a','b','c','d']
newList = list(data)
print(newList)

z = set('abc')
z.add('san')
z.update(set(['p','q']))
print(z)

def listSkills(val,list=[]):
    list.append(val)
    return list

list1 = listSkills('NodeJs')
list2 = listSkills('Java',[])
list3 = listSkills('ReactJs')
print("%s" % list1)
print("%s" % list2)
print("%s" % list3)

x = 'abcdef'
i = 'a'
while i in x[:-1]:
    print(i,end=" ")
