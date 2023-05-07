# ADD TWO NUMBERS: You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit. Add the
# numbers and return the sum as a linked list.

class Node(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def addTwoNumbers(l1,l2):
    ls = Node()
    carry =0 
    curt1 = l1
    curt2 = l2
    curts = ls
    while (curt1 is not None) and (curt2 is not None):
        sum = curt1.val+curt2.val+carry
        if sum//10 == 0:
            curts = add(sum,curts)
        else:
            carry = sum//10
            curts = add(sum%10,curts)
        curt1 = curt1.next
        curt2 = curt2.next
    if curt1 is not None:
        while curt1.next is not None:
            sum = curt1.val+carry
            if sum//10 == 0:
                curts = add(sum,curts)
            else:
                carry = sum//10
                curts = add(sum%10,curts)
            curt1 = curt1.next
    if curt2 is not None:
        while curt2.next is not None:
            sum = curt2.val+carry
            if sum//10 == 0:
                curts = add(sum,curts)
            else:
                carry = sum//10
                curts = add(sum%10,curts)
            curt2 = curt2.next
    return ls

def add(value, pointer):
    pointer.val = value
    newpointer = Node()
    pointer.next = newpointer
    return newpointer

l1 = Node(2)
d1 = Node(4)
d2 = Node(3)
l1.next = d1
d1.next = d2
l2 = Node(5)
d3 = Node(6)
d4 = Node(4)
l2.next = d3
d3.next = d4

result = addTwoNumbers(l1,l2)
print(result.val)

def printNodes(init):
    while init.next is not None:
        print(init.val)
        init = init.next

printNodes(result)
