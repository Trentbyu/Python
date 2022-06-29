
"""
run this file to make sense of what is going on 
"""
lst = [0,1,2,5,32,12,3,4,456,21,1,2,3]#here is a list full of numbers

print(lst)

lst.pop()#this will pop the last item in the list
print(lst)

lst.pop(0)#this will pop the item at index 0
print(lst)

lst.pop(4)#this will pop the item at index 4
print(lst)

lst.pop(5)#this will pop the item at index 5

lst.pop(0)#this will pop the item at index 0
print(lst)

lst.pop(0)#this will pop the item at index 0
print(lst)
remove = 0
lst.pop(remove)#this will pop the item at index 0
print(lst)
"""
make sure that you try the pop function it will be easier for this assignment than .remove
alos pay attention what happned to the list when it got printed out 
"""