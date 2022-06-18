import json
import re

from attr import field


def main():
    array = receive_array(None)

    sorted_array = sort(array)

    print(sorted_array)

def test_main():

    for i in range(1,9):
        file_name = "test"+str(i)+".json"

        array = receive_array(file_name)

        sorted_array = sort(array)

        print(sorted_array)


def receive_array(file_name = None):

    if file_name != None:
        file_loc = file_name
        with open(file_loc, "r") as array:
            loaded_file = json.load(array)
            array = loaded_file["array"]
        return array
    vaild = False
    while vaild == False:
        try:
            file_loc = input("type the array/lists file location")
            with open(file_loc, "r") as array:
                loaded_file = json.load(array)
                array = loaded_file["array"]
            return array
        except FileNotFoundError:
            print(" gay fag")

def sort(array):
    size = len(array)
    source = array

    destination = [0] *size

    number = 2 

    while number >1:

        number =0
        begin1 = 0

        while begin1 < size:

            end1 = begin1 + 1

            while end1 < size and source[end1 - 1] <= source[end1]:
                end1+1
            
            begin2 = end1

            if begin2<size:
                end2 = begin2 

            while end2 <size and source[end2-1] <= source[end2]:
                end2+=1
            number += 1 

            combine(source, destination, begin1, begin2, end2)

            begin1 = end2
        
        for i in range(0,size):
            source[i] = destination[i]


    return source 



def combinbe(source, destination, begin1, begin2, end2):

    end1 = begin2 




    for i in range(begin1, end2):


        if begin1 < end1 and (begin2 == end2 or source[begin1] < source[begin2]):


            begin1 += 1 

        else:
            destination[i] = source[begin2]
            begin += 1 

    return destination


if __name__ == "__main__":
    test_main()



