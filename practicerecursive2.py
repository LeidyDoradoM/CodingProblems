# practice of recursive functions part 3

def CapitalizeFirst(arr):
    if len(arr) == 1:
        out = [arr[0].capitalize()]
        return out
    else:
        out = CapitalizeFirst(arr[1:])
        arr = [arr[0].capitalize()]
        arr.extend(out)
        return arr

#print(CapitalizeFirst(['car','taco','banana']))

obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}

def NestedEvenSum(obj,sum):
    for value in obj.values():
        if type(value) == int:
            if value % 2 == 0:
                sum = sum+value
        if type(value) == dict:
            sum = NestedEvenSum(value,sum)
    return sum

#print(NestedEvenSum(obj1,0))

def CapitalizeWords(words):
    if len(words) == 1:
        return [words[0].upper()]
    else:
        out = CapitalizeWords(words[1:])
        words1 = [words[0].upper()]
        words1.extend(out)
        return words1

words = ['i','am','learning','recursion']
#print(CapitalizeWords(words))

def stringifyNumbers(obj):
    for key,value in obj.items():
        if type(value) == int:
            obj[key] = str(value)
        if type(value) == dict:
            stringifyNumbers(value)
    return obj

obj = {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}

#print(stringifyNumbers(obj))

def collectStrings(obj,arr):
    for key,value in obj.items():
        if type(value) == str:
            arr.append(value)
        if type(value) == dict:
            collectStrings(value,arr)
    return arr

obj3 = {"stuff":'foo',
        "data": {"val":{"thing":{"info":'bar',
                                 "moreinfo":{"evenMoreInfo":{"weMadeIt":'baz'
                                                            }
                                            }
                                }
                        }
                }
        }
print(collectStrings(obj3,[]))