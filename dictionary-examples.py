# A dictionary is a collection of pairs: key-values
myDict = dict()  #create an empty dictionary
engToSpanish = {'one':"uno",'two':"dos",'three':"tres"} #create a dictionary w/elements
# accessing elements using key values: O(1) complexity
print(engToSpanish['one'])
# traverse and search for in a dictionary
def searchForValue(mydict, value):
    for key in mydict: #using in operator
        if mydict[key] == value:
            print(key,value)
    print('The value is not in the dictionary')

searchForValue(engToSpanish,"cuatro")