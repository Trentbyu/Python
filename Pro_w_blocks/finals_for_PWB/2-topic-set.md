
SET
1.	Introduction: In Python, a Set is an unordered collection of data types that is iterable, mutable and has no duplicate elements. The order of elements in a set is undefined though it may consist of various elements. Sets can be created by using the built-in set() function 
2.	Internal working of Set: If Multiple values are present at the same index position, then the value is appended to that index position, to form a Linked List. In, CPython Sets are implemented using dictionary with dummy variables, where key beings the members set with greater optimizations to the time complexity.
3.	Adding elements, add(): Elements can be added to the Set by using the built-in add() function. Only one element at a time can be added to the set by using add() method, loops are used to add multiple elements at a time with the use of add() method.
4.	Copy(): set_name.copy(), The copy() method returns a shallow copy of the set in python. The copy() method for sets doesn’t take any parameters
5.	Operators for Sets: Intersection , Union, and Difference
6.	Union: Two sets can be merged using union() function or | operator. Both Hash Table values are accessed and traversed with merge operation perform on them to combine the elements, at the same time duplicates are removed.
7.	Intersection: This can be done through intersection() or & operator. Common Elements are selected. They are similar to iteration over the Hash lists and combining the same values on both the Table.
8.	Difference: To find difference in between sets. Similar to find difference in linked list. This is done through difference()
9.	Clearing sets clear():  set_name.clear(), The clear() method doesn't take any parameters. The clear() method doesn't return any value. clear() method to remove all the elements of the set so it will then be blank.
10.	Time complexity of Sets:  O(1) on average. However in worst case it can become O(n).
11.	Pros and cons: The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set.
12. The top 3 erros of a set: syntax errors. logic errors. runtime errors.




    ```python
        def intersection(set1, set2):
            """
            Perform an intersection between 2 sets.  An intersection will contain
            the items in common between both sets.  Do not use the set 
            operators (+, -, *, &, |) and functions (intersection, union) 
            that are built-in to Python.
            """

            


            inters = []

            for num in set1: # if the item in set1 is equal to any items in set2 
                for item in set2:
                    if num == item:
                        inters.append(num)
            return inters


        def union(set1, set2):
            """
            Perform a union between 2 sets.  A union will contain all the items
            from both sets.   Do not use the set operators (+, -, *, &, |)
            and functions (intersection, union) that are built-in to Python.
            """

            lst = list(set1) 
            for item in set2: 
                if item not in lst: 
                    lst.append(item) 
                                        #this will not take any repeated vaules 
            

            return lst

        s1 = {1,2,3,4,5}
        s2 = {4,5,6,7,8}
        print(intersection(s1,s2))  # Should show {4, 5}
        print(union(s1,s2)) # Should show {1, 2, 3, 4, 5, 6, 7, 8}

        s1 = {1,2,3,4,5}
        s2 = {6,7,8,9,10}
        print(intersection(s1,s2))  # Should show an empty set
        print(union(s1,s2)) # Should show {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

        ----------------------------------------------------------------------
        def find_pairs(words):
        """
        The words parameter contains a list of two character 
        words (lower case, no duplicates). Using sets, find an O(n) 
        solution for displaying all symmetric pairs of words.  

        For example, if words was: [am, at, ma, if, fi], we would display:

        am & ma
        if & fi

        The order of the display above does not matter.  'at' would not 
        be displayed because 'ta' is not in the list of words.

        As a special case, if the letters are the same (example: 'aa') then
        it would not match anything else (remember no the assumption above
        that there were no duplicates) and therefore should not be displayed.
        """ 
    
        words = set(words) # creates a set using the words or letters given below 
        pairs = set() # will hold the pairs of words 

        for char in words: # for the characters in the words get the reverse of the way they came in 
            reverse = char[::-1]
            if reverse < char:
                pair = (reverse, char)
            else:
                pair = (char, reverse)
            
        
            if reverse in words:
                pairs.add(pair) 
            
        for x,y in pairs:
            if x !=y:
                print(x,"&",y) # this way only the number s and letter combinations below come out
                # this could be printed with out this last bit
    
        
    


        find_pairs(["am","at","ma","if","fi"])      # ma & am, fi & if
        print("=============")
        find_pairs(["ab", "bc", "cd", "de", "ba"])  # ba & ab
        print("=============")
        find_pairs(["ab","ba","ac","ad","da","ca"]) # ba & ab, da & ad, ca & ac
        print("=============")
        find_pairs(["ab", "ac"])                    # None
        print("=============")
        find_pairs(["ab", "aa", "ba"])              # ba & ab
        print("=============")
        find_pairs(["23","84","49","13","32","46","91","99","94","31","57","14"])
                                                    # 32 & 23, 94 & 49, 31 & 13


        set = set(["a", "b","c"])
        set.add("d")

    ```
# YOUR TURN

The task i have for you is the make a set using python and add numbers to a set using a for loop 
Then take all the items out of the set. Then demonstrate the intersection and union function with python 

## soultion in python file.