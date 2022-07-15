
WELCOME
1.	Introduction
2.	Contact




STACK
1.	Introduction: A stack is a data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. This means that an item you put inside of this stack will end up on top and when grabbing data from the list the ithem on top is grabed first hence last in first out. In stack, a new element is added at one end and an element is removed from that end only weather that be the top or the bottom.The stack is nothing but the linear data structure where insertion and deletion take place only at one end.


2.	Last in first out: This is what was descirbed in the intro the item last put into the stack is the first item out of the stack


3.	Types of stack: There are two types of stacks they are register stack and the memory stack. In the memory stack, the stack depth is flexible. It occupies a large amount of memory data, whereas in the register stack only a finite number of memory words will be stored.The register stack is also a memory device present in the memory unit, but it handles only a small amount of data. The stack depth is always limited in the register stack because the size of the register stack s very small compared to the memory.


4.	Applications of stack: A Stack can be used for evaluating expressions consisting of operands and operators. Stacks can be used for Backtracking, i.e., to check parenthesis matching in an expression.It can also be used to convert one form of expression to another form.It can be used for systematic Memory Management.
5.	Push():  stack.append('a') ,stack.append('b') , stack.append('c') this is a fucntion to add items to the stack. You have to specifiy what you want to add inside the () like done earlier. 
6.	Pop(): stack.pop() this is a function to delete an item from the stack. This will delte the last item put into the stack first in last out.
7.	Top(): Returns a reference to the topmost element of the stack stack.top(). The top element will be the last item put in 
8.	isEmpty(): reutrns if the the stack is empty or has any amount of items in it. stack.isEmpty()
9.	size(): This function returns the size of the stack stack.size()
10.	advantages and disadvantages: Advantages of Stack, A Stack helps to manage the data in the ‘Last in First out’ method. When the variable is
not used outside the function in any program, the Stack can be used. It allows you to control and handle memory allocation and deallocation.
It helps to automatically clean up the objects. Disadvantages of Stack It is difficult in Stack to create many objects as it increases the risk of the Stack overflow. It has very limited memory. In Stack, random access is not possible.



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





TREE
1.	Introduction 
2.	When to use a Tree
3.	Parent Node
4.	Child Node
5.	Root Node
6.	Degree of a Node
7.	Leaf Node or External Node
8.	Ancestor of a Node
9.	Descendant
10.	Sibling
11. Depth of a node
12.	Height of a node
13.	Height of a tree
14.	Level of a node
15.	Internal node
16.	Neighbour
17.	Subtree
