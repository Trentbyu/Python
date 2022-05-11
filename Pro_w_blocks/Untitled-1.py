user_input = int(input("pick a number: "))


if user_input <=9:
    print(f"{user_input:<3} is lest than 10")
elif user_input >= 11:
    print(f"{user_input:<3} is greator than 10")
else:
    print(f"{user_input} is equal to 10")
