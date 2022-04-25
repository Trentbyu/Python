
# 1. Name:
#      Trent Black
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#     this program decideds if a user is authenticated 
#     by telling the user if their password and user name 
#     is correct or if it is wrong.
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
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

    authenticated = False


    user_name_list = []
    for i in data['username']:
        user_name_list.append(i)

    pass_word_list = []
    for i in data['password']:
        pass_word_list.append(i)

    for x in range(len(user_name_list)):
        if user_name == user_name_list[x] and pass_word == pass_word_list[x]:
            print("You are authenticated!")
            authenticated = True
            

    return authenticated


def vaild(authenticated):
    if authenticated == False: 
        print("You are not authorized to use the system.")


def main():
    user_name, pass_word = get_user_info()
    authenticated = check_info(user_name, pass_word)
    vaild(authenticated)




if __name__ == "__main__":
    main()