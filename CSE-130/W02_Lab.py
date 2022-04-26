
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
#      The hardest part for me was outputing if the user 
#       was not authenticated becuae i could not put it in the 
#       for loop.
# 5. How long did it take for you to complete the assignment?
#      0.3
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
        at the same index in the list created from the json file 
    """
    authenticated = False #tells the computer if the user  has been authenticated yet 

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