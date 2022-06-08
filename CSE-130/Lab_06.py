
# 1. Name:
#      Trent Black
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      Search for a word in a really fast time using big o notation 
# 4. Algorithmic Efficiency
#      this algorithm is really efficent becuase it does the job really fast with O(log n) time 
# 5. What was the hardest part? Be as specific as possible.
#      UNderstanding how to get the right indexs and how to split the data the right way depeding on if it was higher or lower
#       overall it was hard but i now understand how to do this assignment
# 6. How long did it take for you to complete the assignment?
#      4.5 Hrs





import json



def search_words(search_word, file_name):
    """
    This function puts all the words from the arrray inside the json file into a list 
    the list in then put into the find_word function
    """


    ary = []

    try:
        file = open(file_name)
        single_string = file.read() # trys to find the file name 
        file.close()
        json_convert = json.loads(single_string)

    except:
        print("\ncould not find file name\n")

    try:
        for item in json_convert["array"]: #sees if anythin is in the array
            ary.append(item)
        min =0
        max = len(ary)
        prnt = False
        find_word(min, max, search_word, file_name, prnt, ary)
    except:
        print(f"{search_word} in {file_name} was not found\n")

    
    return ""


def find_word(min, max, search_word, file_name, prnt, ary):
    """
    uses the searched word to find the word in the array 
    """

    search_index  = ((max - min) // 2) + min

    dict_word = ary[search_index ]

    if search_word != dict_word or max != 0: 
        search_index  = ((max - min) // 2) + min
        dict_word = ary[search_index ]

        if search_word == dict_word:
            max = search_index
            min = search_index 
            prnt = True
        elif search_word < dict_word: # if the word is less than the dict_word it will use the bottom half of the list 
            max = search_index 
            find_word(min, max, search_word, file_name, prnt, ary)
        elif search_word > dict_word:  # if the word is more than the dict_word it will use the top half of the list
            min = search_index 
            find_word(min, max, search_word, file_name, prnt, ary)
        
        
    else:
        print(f"{search_word} in {file_name} was not found\n")

            

    if prnt:
        print(f"We found {search_word} in {file_name}\n")




file_name = input("what is the file name?: ")
search_word = input("what word are you looking for?: ")

print("\n\n", search_words(search_word, file_name), "\n")


choice = input("do you want to see all the test cases? \"Y/N\": ")

if choice.lower() == "y":
    print("1.empy_case: ")
    print(search_words("empty", "CSE-130/Lab06.empty.json"))

    print("2.Single item found: ")
    print(search_words("trivial", "CSE-130/Lab06.trivial .json"))

    print("3.Single item not found: ")
    print(search_words("missing ", "CSE-130/Lab06.trivial .json"))


    print("4.Small list found: ")
    print(search_words("C++", "CSE-130/Lab06.languages.json"))

    print("5.Small list not found: ")
    print(search_words("Lisp", "CSE-130/Lab06.languages.json"))


    print("6.Big list founde: ")
    print(search_words("United States of America", "CSE-130/Lab06.countries.json"))

    print("7.Big list not found: ")
    print(search_words("United States", "CSE-130/Lab06.countries.json"))


