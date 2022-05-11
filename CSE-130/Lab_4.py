
# 1. Name:
#      Trent Black
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      -to inform the user if he or she is able to build a hotel or house on a green property or to swap with another green property 
# 4. What was the hardest part? Be as specific as possible.
#      Was it the syntax of Python? yes it can be hard to remember the syntax 
#      Was it an aspect of the problem you are to solve? yes all the if else statemnets were hard to keep track of i wasnt sure if there was a better way to do it 
#      Was it the instructions or any part of the problem definition? the instructions were not clear on the testcases i wasnt sure what the test cases wanted me to do
#      Was it the submission process? the submission was ok
#      i struggled the most on knowing what to do i did not understand the test cases very well so i tried to debugg as much as possible 
#      there was alot of times i feel i added more than was required becuase i wanted to get a good grade but was unsure if it was needed
# 5. How long did it take for you to complete the assignment?
#      -5 hours 




def get_info():
    '''
    This function askes the user what is on the propertys
    asks how many house and hotels are avilble to purchase
    '''
    pacific_avenue = int(input("what is on  Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
    north_carolina = int(input("what is on  North Carolina? (0:nothing, 1:one house, ... 5:a hotel) "))
    pennsylvania_avenue = int(input("what is on  Pennsylvania avenu? (0:nothing, 1:one house, ... 5:a hotel) "))
    cash = int(input("How much cash do you have to spend? "))
    houses = int(input("How many houses are there to purchase?  "))
    hotels = int(input("How many hotels are there to purchase? "))

    return pacific_avenue, north_carolina, pennsylvania_avenue, cash, houses, hotels


def user_choice(pacific_avenue, north_carolina, pennsylvania_avenue):
    '''
    this askes the user what they want to do
    they can purchase a hotel or houses
    if they purchase a hotel they can not swap propertys
    they can purchase 1-4 houses and 1 hotel
    '''
    
  
    
    purchase_house = input("do you want to purhcase a house? y/n")
    if purchase_house.lower() == "y":
       
        purchase_house_pc = int(input("do you want to purchase a house on pc type 1-4? if no type 0. "))
    
        purchase_house_nc = int(input("do you want to purchase a house on nc type 1-4? if no type 0. "))
       
        purchase_house_pa = int(input("do you want to purchase a house on pa type 1-4? if no type 0. "))
     
        if purchase_house_pc + pacific_avenue >= 5 or purchase_house_nc + north_carolina >= 5 or purchase_house_pa + pennsylvania_avenue >= 5:
            print("already built too many houses")
        if purchase_house_pc + pacific_avenue >= 5:
            purchase_house_pc = 0
        if purchase_house_nc + north_carolina >= 5:
            purchase_house_nc =  0
        if purchase_house_pa + pennsylvania_avenue >= 5:
            purchase_house_pa = 0
            

        purchase_house = [purchase_house_pc, purchase_house_nc, purchase_house_pa]  
    else:
        purchase_house = [0,0,0] # if they dont want to purchase a house than the vaules are 0
    
    purchase_hotel = input("do you want to purhcase a hotel? y/n")
    if purchase_hotel.lower() == "y":
        
        purchase_hotel_pc = int(input("do you want to purchase a hotel on pc type 1? if no type 0. "))
        purchase_hotel_nc = int(input("do you want to purchase a hotel on nc type 1? if no type 0. "))
        purchase_hotel_pa = int(input("do you want to purchase a hotel on pa type 1? if no type 0. "))
        
        purchase_hotel = [purchase_hotel_pc, purchase_hotel_nc, purchase_hotel_pa]        
    else:
        purchase_hotel = [0,0,0]# if they dont want to purchase a hotel than the vaules are 0

    # can only swap if they dont want to buy a house or hotel
    if purchase_house == [0, 0, 0] and purchase_hotel == [0, 0, 0]:
        swap_hotel = input("do you want to swap a hotels or houses from a property? y/n: ")
        if swap_hotel.lower() == "y":
            s_h = input("swap pc? nc? or pa?: ")
            s_h2 = input(f'swap {s_h} with pc? nc? or pa?: ')
            s_hotel = [s_h, s_h2] 
        else:
            s_hotel = [' ',' ']
    else:
         s_hotel = [' ',' ']
    
    return purchase_hotel, purchase_house, s_hotel

def calculations(pacific_avenue, north_carolina, pennsylvania_avenue, cash, houses,
 hotels, purchase_hotel, purchase_house,  s_hotel ):
    '''
    the user is not allowed to purchase a hotel if they already have one on their property
    calculations adds up the houses and hotels to decided what the price is 
    calculations does the work to set up a property swap
    calculations makes sure the user can not add houses more than can fit on a property
    '''
    price = 0
    final = True
    swap = ' '

    if s_hotel[0].lower() == "pc":
        temp = pacific_avenue
        if s_hotel[1] == "nc":
            pacific_avenue = north_carolina
            north_carolina = temp
            swap = 'pcnc'
        if s_hotel[1] == "pa":
            pacific_avenue= pennsylvania_avenue
            pennsylvania_avenue = temp
            swap = 'pcpa'
    

    if s_hotel[0].lower() == "nc":
        temp = north_carolina
        if s_hotel[1] == "pc":
            north_carolina = pacific_avenue
            pacific_avenue = temp
            swap = 'ncpc'

        if s_hotel[1] == "pa":
            north_carolina = pennsylvania_avenue
            pennsylvania_avenue = temp
            swap = 'ncpa'

    if s_hotel[0].lower() == "pa":
        temp = pennsylvania_avenue
        if s_hotel[1] == "pc":
            pacific_avenue = pacific_avenue
            pacific_avenue = temp
            swap = 'papc'

        if s_hotel[1] == "nc":
            pacific_avenue = north_carolina
            north_carolina = temp
            swap = 'panc'

    for x in range(0,3):
        price += purchase_hotel[x] * 200
        price += purchase_house[x] * 200
        

    if price > cash: 
        print("You do not have sufficient funds to purchase a hotel at this time.")
        final = False
    if  hotels < purchase_hotel[0] + purchase_hotel[1] + purchase_hotel[2]: 
        print("There are not enough hotels available for purchase at this time.")
        final = False
    if houses < purchase_house[0] + purchase_house[1] + purchase_house[2]: 
        print("There are not enough houses available for purchase at this time.")
        final = False
    if pacific_avenue ==5 and purchase_hotel[0] == 1 or north_carolina ==5 and purchase_hotel[1] == 1 or pennsylvania_avenue ==5 and purchase_hotel[2] == 1 :
        print("You cannot purchase a hotel if the property already has one.")
        final = False
    if pacific_avenue ==5 and purchase_house[0] >= 1 or north_carolina ==5 and purchase_house[1] >= 1 or pennsylvania_avenue ==5 and purchase_house[2] >= 1 :
        print("You cannot put a house on a hotel.")
        final = False
    if pacific_avenue >=6 or purchase_house[0] >= 6 or north_carolina >=6 or purchase_house[1] >= 6 or pennsylvania_avenue >=6 or purchase_house[2] >= 6 :
        print("no more room for hosues or hotels on this property ")
        final = False
    if pacific_avenue + purchase_house[0] < 4 and purchase_hotel[0] == 1 or north_carolina + purchase_house[1] < 4 and purchase_hotel[1] == 1 or pennsylvania_avenue + purchase_house[2] < 4 and purchase_hotel[2] == 1:
        print("You do not have enough houses to build here ")
        final = False
    if pacific_avenue == 5 and purchase_hotel[0] >= 1 or north_carolina == 5 and purchase_hotel[1] >= 1 or pennsylvania_avenue == 5 and purchase_hotel[2] >= 1:
        print("There is already a hotel there.")
        final = False
    
    return price , final, swap #final is if there was an error or not 


def print_final(price, final, purchase_hotel, purchase_house, swap, pacific_avenue, north_carolina, pennsylvania_avenue,):
    '''
    this functiuon prints out all the different cases 
    can not print out if there is an error in the calculations throws one 

    '''
    houses = ' '
    property = '' #property for the second property to be swaped
    property1 = 'hotel' # property for the first property to be swaped
    num = ''
    if swap != ' ':
        if swap == 'pcnc': #this is what property is to be swpaed to what. this was decided in calculations function
            if north_carolina < 5: #if it is not a hotel
                houses = north_carolina
            if north_carolina == 5: # if it is a hotel
                property = "hotel" 
            else:
                property="houses"
            if pacific_avenue < 5: #if it is not a hotel
                num = pacific_avenue
                property1 = 'houses'
            print(f"\nSwap Pacific Avenue {str(num)} {property1 } with North Carolina {houses} {property} .")
        if swap == 'pcpa':
            if pennsylvania_avenue < 5:
                houses = pennsylvania_avenue
            if pennsylvania_avenue == 5:
                property = "hotel" 
            else:
                property="houses"
            if pacific_avenue < 5:
                num = pacific_avenue
                property1 = 'houses'
            print(f"\nSwap Pacific Avenue {str(num)} {property1 } with Pennsylvania avenu {houses} {property}.")
        if swap == 'ncpa':
            if pennsylvania_avenue < 5:
                houses = pennsylvania_avenue
            if pennsylvania_avenue == 5:
                property = "hotel" 
            else:
                property="houses"
            if north_carolina < 5:
                num = north_carolina
                property1 = 'houses'
            print(f"\nSwap North Carolina {str(num)} {property1 } with Pennsylvania avenu {houses} {property}.")
        if swap == "ncpc":
            if pacific_avenue < 5:
                houses = pacific_avenue
            if pacific_avenue == 5:
                property = "hotel" 
            else:
                property="houses"
            if north_carolina < 5:
                num = north_carolina
                property1 = 'houses'
            print(f"\nSwap North Carolina {str(num)} {property1 } with Pacific Avenue {houses} {property} .")
        if swap == "panc":
            if north_carolina < 5:
                houses = north_carolina
            if north_carolina == 5:
                property = "hotel" 
            else:
                property="houses"
            if pennsylvania_avenue < 5:
                num = pennsylvania_avenue
                property1 = 'houses'
            print(f"\nSwap Pennsylvania avenu {str(num)} {property1 } with North Carolina {houses} {property}.")
        
        if swap == "papc":
            if pacific_avenue < 5:
                houses = pacific_avenue
            if pacific_avenue == 5:
                property = "hotel" 
            else:
                property="house"
            if pennsylvania_avenue < 5:
                num = pennsylvania_avenue
                property1 = 'houses'
            print(f"\nSwap pa {str(num) } {property1} with Pacific Avenue {houses} {property}.")

    
    if final == True and price > 0:# true if there are no previous erros 


        print(f'\nThis will cost ${price}.')
        print (f'\tPurchase {purchase_hotel[0] + purchase_hotel[1] + purchase_hotel[2]} hotel(s) and {purchase_house[0] + purchase_house[1] + purchase_house[2]} house(s).')
        if purchase_hotel[0]== 1 :
            print("Put 1 hotel on Pacific Avenue and return any houses to the bank.")
        if purchase_hotel[1]== 1 :
            print("Put 1 hotel on Norh carloina and return any houses to the bank.")
        if purchase_hotel[2]== 1 :
            print("Put 1 hotel on Pennsylvania avenu and return any houses to the bank.")
        if purchase_house[0] < 5 and purchase_house[0] != 0 and purchase_house[0]+pacific_avenue!=5 and purchase_hotel[0] !=1 :
            print(f"Put {purchase_house[0]} house(s) on Pacific Avenue.")
        if purchase_house[1] < 5 and purchase_house[1] != 0 and purchase_house[1]+north_carolina!=5 and purchase_hotel[1] !=1 :
            print(f"Put {purchase_house[1]} house(s) on North Carolina.")
        if purchase_house[2] < 5 and purchase_house[2] != 0 and purchase_house[2]+pennsylvania_avenue != 5 and purchase_hotel[2] !=1:
            print(f"Put {purchase_house[2]} house(s) on Pennsylvania avenu.")
         

def main():

    owned = input("Do you own pacific avenue, north carolina, and pennsylvania avenue? Y/N: ")# returns if the user owns all green
    if owned.lower() == "y":# can only purchase if popertys are all owned

        pacific_avenue, north_carolina, pennsylvania_avenue, cash, houses, hotels = get_info()
        purchase_hotel, purchase_house, s_hotel = user_choice(pacific_avenue, north_carolina, pennsylvania_avenue)
        price, final,swap = calculations(pacific_avenue, north_carolina, pennsylvania_avenue, cash, houses, hotels, purchase_hotel,
         purchase_house, s_hotel)

        
        print_final(price, final, purchase_hotel, purchase_house, swap, pacific_avenue, north_carolina, pennsylvania_avenue)
        
    else: 
        print("You cannot purchase a hotel until you own all the properties of a given color group.")



if __name__ == "__main__":
    main()

