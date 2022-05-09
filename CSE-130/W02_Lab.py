
# 1. Name:
#      Trent Black
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#     this program decideds if a user is authenticated 
#     by telling the user if their password and user name 
#     is correct or if it is wrong. in a json file there are a list of passwords
#       and usernames that will get authentication if use.
# 4. What was the hardest part? Be as specific as possible.
'''
1.Was the syntax of Python the hardest part? If so, what part?
    i dont think was the hardest part but it is hard to remember all of the syntax rules.
    the hardestr rules to remeber for me are how things are supposed to be written.

2.Was there some aspect of the problem that was particularly difficult to solve?
    it took me a little while to figure out how to add the comment you are not authenticated 
    if the user did not get enter in a combination. i first had it in the for loop but then it would display for every
    loop. which is not what i wanted. 
3.Was there an especially difficult bug? If so, how did you resolve it?
    i think the bug was the same as the hardest problem from the question above and i solved it by when
    a user was authenticated it returned a False vaule and was pasted to a new function and then displayed
    you are not authenticated. This way it only dispalys it one time.
4.Was there some difficulty with the instructions or any part of the problem definition?
    for the instruction were not hard but i needed to read all of them. i did not realise unitl i read carefully 
    that it is important to you the test cases given not my own. 

'''
# 5. How long did it take for you to complete the assignment?
#      1.5




import json

# Opening JSON file
f = open('CSE-130/doc_lab2.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)
 
# Closing file
f.close()

def get_user_info():
    user_name = input("Username: ")
    pass_word = input("Password: ")

    return user_name, pass_word

def check_info(user_name, pass_word):
    """This function checks if the user name and password are 
        at the same index in the list created from the json file.
    """
    #tells the computer if the user  has been authenticated yet 
    authenticated = False 

    user_name_list = [] #creates a list for the usernames  
    for i in data['username']:# only appends data inside the username 
        user_name_list.append(i)

    pass_word_list = [] #creates a list for the passwords 
    for i in data['password']: # only appends data inside the password
        pass_word_list.append(i)

    for x in range(len(user_name_list)):
        if user_name == user_name_list[x] and pass_word == pass_word_list[x]: #checks if the password and username has the same index in their lists
            print("You are authenticated!")
            authenticated = True
            
    return authenticated


def vaild(authenticated): #if the user is not authenticated the computer responds 
    if authenticated == False: 
        print("You are not authorized to use the system.")


def main(): #main function
    user_name, pass_word = get_user_info() # getting varibles for other function
    authenticated = check_info(user_name, pass_word) #returns the authentication 
    vaild(authenticated) #prints out if the user was not authenticated 


if __name__ == "__main__":
    main()