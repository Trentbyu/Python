
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
        purchase_hotel_nc = int(input("do you want to purchase a hotel on nc type 1? if no type 0. "))
        purchase_hotel_pa = int(input("do you want to purchase a hotel on pa type 1? if no type 0. "))  
        purchase_hotel = [purchase_hotel_pc, purchase_hotel_nc, purchase_hotel_pa]        
    else:
        purchase_hotel = [0,0,0]
    
    purchase_house = input("do you want to purhcase a house? y/n")
    if purchase_house.lower() == "y":
        purchase_house_pc = int(input("do you want to purchase a house on pc type 1-4? if no type 0. "))
        purchase_house_nc = int(input("do you want to purchase a house on nc type 1-4? if no type 0. "))
        purchase_house_pa = int(input("do you want to purchase a house on pa type 1-4? if no type 0. "))
        purchase_house = [purchase_house_pc, purchase_house_nc, purchase_house_pa]  
    else:
        purchase_house = [0,0,0] 

    swap_hotel = input("do you want to swap a hotel? y/n ")
    if swap_hotel.lower() == "y":
        s_h = input("swap pc? nc? or pa?")
        s_h2 = input(f'swap {s_hl} with pc? nc? or pa?')
        s_hotel = [s_h, s_h2] 
    else:
        s_hotel = []

    swap_house = input("do you want to swap a house? y/n ")
    if swap_house.lower() == "y":
        s_hl = input("swap pc? nc? or pa?")
        s_hl2 = input(f'swap {s_hl} with pc? nc? or pa?')
        s_house = [s_hl, s_hl2]
    else:
        s_house = [] 
    return purchase_hotel, purchase_house, s_hotel, s_house 

def calculations(pacific_avenue, north_carolina, pennsylvania_avenue, cash, houses,
 hotels, purchase_hotel, purchase_house, swap_hotel, swap_house):
    price = 0
    final = True
    
    for x in range(0,3):
        price += purchase_hotel[x] * 200
        price += purchase_house[x] * 200
        

    if price > cash: 
        print("You do not have sufficient funds to purchase a hotel at this time.")
        final = False
    if hotels < 1 or hotels < purchase_hotel[0] + purchase_hotel[1] + purchase_hotel[2]: 
        print("There are not enough hotels available for purchase at this time.")
        final = False
    if houses < 1 or  houses < purchase_house[0] + purchase_house[1] + purchase_house[2]: 
        print("There are not enough houses available for purchase at this time.")
        final = False
    if pacific_avenue ==5 and purchase_hotel[0] == 1 or north_carolina ==5 and purchase_hotel[1] == 1 or pennsylvania_avenue ==5 and purchase_hotel[2] == 1 :
        print("You cannot purchase a hotel if the property already has one.")
        final = False
    

    
    return price , final


def print_final(price, final):
    if final == True:
        print(f'This will cost ${price}.')
           


def main():

    owned = input("Do you own pacific_avenue, north_carolina, pennsylvania_avenue? Y/N")
    if owned.lower() == "y":

        pacific_avenue, north_carolina, pennsylvania_avenue, cash, houses, hotels = get_info()
        purchase_hotel, purchase_house, swap_hotel, swap_house = user_choice()
        price, final = calculations(pacific_avenue, north_carolina, pennsylvania_avenue, cash, houses, hotels, purchase_hotel,
         purchase_house, swap_hotel, swap_house)

        
        print_final(price, final)
        
    else: 
        print("You cannot purchase a hotel until you own all the properties of a given color group.")






if __name__ == "__main__":
    main()

