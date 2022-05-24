
import json



def search_words(search_word, file_name):
    """
    This function puts all the words from the arrray inside the json file into a list 
    the list in then put into the find_word function
    """
    try:
        file = open(file_name)
        single_string = file.read() # trys to find the file name 
        file.close()
    except:
        print("could not find file name\n")

    json_convert = json.loads(single_string)
    try:
        for item in json_convert["array"]: #sees if anythin is in the array
            ary.append(item)
        min =0
        max = len(ary)
        prnt = 0
        find_word(min, max, search_word, file_name, prnt)
    except:
        print(f"{search_word} in {file_name} was not found\n")

    
    return ""


def find_word(min, max, search_word, file_name, prnt):
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
            prnt += 1
        elif search_word < dict_word: # if the word is less than the dict_word it will use the bottom half of the list 
            max = search_index 
            find_word(min, max, search_word, file_name, prnt)
        elif search_word > dict_word:  # if the word is more than the dict_word it will use the top half of the list
            min = search_index 
            find_word(min, max, search_word, file_name, prnt)
        
        
    else:
        print(f"{search_word} in {file_name} was not found\n")

            

    if prnt == 1:
        print(f"We found {search_word} in {file_name}\n")






prnt = 0
ary = []

print("1.empy_case: ")
print(search_words("empty", "CSE-130/Lab06.empty.json"))
ary = []

print("2.Single item found: ")
print(search_words("trivial", "CSE-130/Lab06.trivial .json"))
ary = []

print("3.Single item not found: ")
print(search_words("missing ", "CSE-130/Lab06.trivial .json"))

ary = []

print("4.Small list found: ")
print(search_words("C++", "CSE-130/Lab06.languages.json"))
ary = []

print("5.Small list not found: ")
print(search_words("Lisp", "CSE-130/Lab06.languages.json"))
ary = []


print("6.Big list founde: ")
print(search_words("United States of America", "CSE-130/Lab06.countries.json"))
ary = []

print("7.Big list not found: ")
print(search_words("United States", "CSE-130/Lab06.countries.json"))


