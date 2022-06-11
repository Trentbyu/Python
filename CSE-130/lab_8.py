
# 1. Name:
#      Trent Black
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      The porgram is meant to sort a list in  a json file alphabeticily 
# 4. What was the hardest part? Be as specific as possible.
#      I had a hard time getting the pivoit to work the way i wanted it to i was trying to use a couple different ways 
#      But they did not all work out and some trys were better than others. 
#      I also struggled with the 
# 5. How long did it take for you to complete the assignment?
#      5 HR



import json 
import os.path




def sort(f):
   
    #asserts if the file exists 
    assert os.path.exists(f) == True, "This file dose not exist"
    #opens the file 
    f = open(f)
    #loads the file 
    string = f.read()
    #closes the file 
    f.close()
    #creates a list
    lst = []
    #converts the json file
    json_convert = json.loads(string)
    #appends everything inside the array inside the file 
    assert isinstance(json_convert, dict), "error with json file"
    for x in json_convert["array"]:
        #appends it to the list 
        lst.append(x)
    assert isinstance(lst, list), " Json file was not converted correctly to a list" 
    #aserts if there are 1 thing in the list 
    assert  len(lst) != 1  , f"list has 1 item and is sorted already\n {lst}"
    #asserts if there are no things in the list
    assert 0 != len(lst), f"This list is empty"
    
    
    # for every item inside of the lst it checks for the higest and puts it at the back of the list   
    for i in range(len(lst)):
        #starts with the first item in the list 
        high = lst[0]
        #creates the pivot 
        pivot = len(lst) - i -1
        for a in range(0, (pivot +1)):
            #if an item is more than the current high than it becomes the high
            if lst[a] > high:
                high = lst[a]
        #switches the indexes 
        #gets the index of the current high 
        index_high = lst.index(high)
        pivot_i = lst[(pivot)]
        #this pviots the pivot to the right spot if it is not equal to the high 
        if high != pivot_i:


            #moves the hight point 
            lst.pop(index_high)
            #moves the pviot 
            lst.insert(pivot, high)
            lst.pop(pivot-1)


            if index_high -1 <0:
                lst.insert(0, pivot_i)
            else:
                lst.insert(index_high-1, pivot_i)

    #makes sure the list was sorted correctly 
    assert lst[-1] > lst[-2], " this list is not sorted correctly "
    #prints out everything in the list
    for i in range(len(lst)):
        print("\t", lst[i])


#this makes it easier to type in test cases 




"""
CSE-130/Lab08.empty.json

CSE-13-/Lab08.trivial.json

CSE-130/Lab08.languages.json

CSE-130/Lab08.states.json

CSE-130/Lab08.cities.json

"""

answer = ' '
while answer.lower() != "n":
    f = input("\nwhat is the file name you want to be sorted: ")

    sort(f)

    answer = input("\ndo you want to test another case?: Y/N: ")




