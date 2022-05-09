
# 1. Name:
#      -your name-
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#      Was it the syntax of Python?
#      Was it an aspect of the problem you are to solve?
#      Was it the instructions or any part of the problem definition?
#      Was it the submission process?
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-




def get_info():
    
    pacific_avenue = int(input("what is on  Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
    north_carolina = int(input("what is on  North Carolina? (0:nothing, 1:one house, ... 5:a hotel) "))
    pennsylvania_avenue = int(input("what is on  Pennsylvania avenu? (0:nothing, 1:one house, ... 5:a hotel) "))
    cash = int(input("How much cash do you have to spend? "))
    houses = int(input("How many houses are there to purchase?  "))
    hotels = int(input("How many hotels are there to purchase? "))

    return pacific_avenue, north_carolina, pennsylvania_avenue, cash, houses, hotels


def user_choice():
    purchase_hotel = input("do you want to purhcase a hotel? y/n")
    if purchase_hotel.lower() == "y":
        purchase_hotel_pc = int(input("do you want to purchase a hotel on pc type 1? if no type 0. "))
        purchase_hotel_pc = int(input("do you want to purchase a hotel on nc type 1? if no type 0. "))
        purchase_hotel_pc = int(input("do you want to purchase a hotel on pa type 1? if no type 0. "))
            
    purchase_house = int(input("do you want to purchase a house type how many 1-12? if no type 0 "))
    swap_hotel = input("do you want to swap a hotel? y/n ")
    if swap_hotel.lower() == "y":
        s_hl = input("swap pc? nc? or pa?")
        s_hl2 = input(f'swap {s_hl} with pc? nc? or pa?') 
    swap_house = input("do you want to swap a house? y/n ")

    return purchase_hotel, purchase_house, swap_hotel, swap_house 

def calculations(pacific_avenue, north_carolina, pennsylvania_avenue, cash, houses,
 hotels, purchase_hotel, purchase_house, swap_hotel, swap_house):

    price = 200 * purchase_house + 200 * purchase_house

    if price < 200: 
        print("You do not have sufficient funds to purchase a hotel at this time.")
    if hotels < 1: 
        print("There are not enough hotels available for purchase at this time.")
    if houses < 1: 
        print("There are not enough houses available for purchase at this time.")
    if pacific_avenue == 5:
        print()
    

    
    return price 
    
def main():

    owned = input("Do you own pacific_avenue, north_carolina, pennsylvania_avenue? Y/N")
    if owned.lower() == "y":

        pacific_avenue, north_carolina, pennsylvania_avenue, cash, houses, hotels = get_info()
        purchase_hotel, purchase_house, swap_hotel, swap_house = user_choice()
        price = calculations(pacific_avenue, north_carolina, pennsylvania_avenue, cash, houses, hotels, purchase_hotel,
         purchase_house, swap_hotel, swap_house)


        print(f'''This will cost ${price}.
        Purchase 1 hotel and [number of houses] house(s).
        Put 1 hotel on Pennsylvania and return any houses to the bank.
        Put [number of houses] house(s) on North Carolina.
        Put [number of houses] house(s) on Pacific.''')
    else: 
        print("You cannot purchase a hotel until you own all the properties of a given color group.")






if __name__ == "__main__":
    main()

