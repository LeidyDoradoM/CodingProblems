#1. Given a roman numeral, convert it to an integer
def romanToInt(s):
        romans = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total = 0
        i = 0
        while i <= len(s) and i+1<=len(s):
            value1 = romans[s[i]]
            if i+1 == len(s):
                total = total + value1
                break
            else:
                value2 = romans[s[i+1]]
                if value1 >= value2:
                    total = total + value1
                    i = i+1
                else:
                    total = total + (value2 - value1)
                    i = i+2
        return total

#print(romanToInt('VI'))
#-------------------------
#2. Find the Longest Common Prefix string amongst an array of strings. If there is no common
# prefix, return an empty string ""
def commonPrefx(arry):
    N = min(arry,key=len)
    output = ""
    if len(arry) == 1:
        output = arry[0]
    else:
        break_out = False
        for i in range(len(N)):
            count = 0
            for item in range(1,len(arry)):
                if arry[0][i] == arry[item][i]:
                    count = count+1
                    item = item + 1
                else:
                    break_out = True
                    break
                if count == len(arry)-1:
                    output = output+arry[item-1][i]
                    print(output)
            
            if break_out == True:
                break
    return output 

arry = ['car','cir']
result = commonPrefx(arry)
print(result)      
#---------------------------
#3. Given a string containing just the characters "(,),{,},[,]", determine if the input string
# is valid. A string is valid if: Open brackets must be closed by the same type of brackets,
# Open brackets must be closed in the correct order, Every close bracket has a corresponding open
# bracket of the same type.
def isValid(s):
    openlist = ['(','[','{']
    closelist = [')',']','}']
    stack = []
    for item in s:
        print(item)
        if item in openlist:
            stack.insert(0,item)
            print(stack)
        if item in closelist:
            pos = closelist.index(item)
            print(pos)
            if openlist[pos] == stack[0] and len(stack)>0:
                stack.pop(0)
                flag = True
                print(flag)
            else:
                flag = False
    if len(stack)==0:
        flag =True
    else:
        flag = False
    return flag

string = '([])'
print(isValid(string))