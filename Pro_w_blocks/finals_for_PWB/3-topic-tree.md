

TREE
1.	Introduction: a tree or a bst tree is a way of spliting numbers by largest to smallest. Largest go to the right and smallest go to the left. It is a tree beause every node has two branches(children) underneateh them the right is bigger then the one on the left.
2.	When to use a Tree:  Implementing a binary search tree is useful in any situation where the elements can be compared in a less than / greater than manner
3.	 Root Node: root node is the starting node. This is where the first item added to the tree goes. IF a bst tree is created from a list than the item closet to the median of the list becomes the root.
4.	Parent Node: a parent node is the first nodes off the root node
5.	child: the child node is the first nodes of the parent nodes.
6.	Degree of a Node: thios is the Height of the node it could be 
10.	Sibling: sibling nodes are nodes that are underneat the same node 
11. speed: For a Graph, the complexity of a Depth First Traversal is O(n + m), where n is the number of nodes, and m is the number of edges.
Since a Binary Tree is also a Graph, the same applies here. The complexity of each of these Depth-first traversals is O(n+m).
Since the number of edges that can originate from a node is limited to 2 in the case of a Binary Tree, the maximum number of total edges in a Binary Tree is n-1, where n is the total number of nodes.
The complexity then becomes O(n + n-1), which is O(n)
12. The Disadvantages: Shape of the tree depends upon order of insertion and it can be degenerated. Searching takes long time. (When tree is not balanced) 
13. Advantages: BST is fast in insertion and deletion etc when balanced. Very efficient and its code is easier than link lists.

    ![](2022-07-15-13-10-03.png)






    ```python
        class BST:
            """
            Implement the Binary Search Tree (BST) data structure.  The Node 
            class below is an inner class.  An inner class means that its real 
            name is related to the outer class.  To create a Node object, we will 
            need to specify BST.Node
            """

            class Node:
                """
                Each node of the BST will have data and links to the 
                left and right sub-tree. 
                """

                def __init__(self, data):
                    """ 
                    Initialize the node to the data provided.  Initially
                    the links are unknown so they are set to None.
                    """
            
                    self.data = data
                    self.left = None
                    self.right = None

            def __init__(self):
                """
                Initialize an empty BST.
                """
                self.root = None

            def insert(self, data):
                """
                Insert 'data' into the BST.  If the BST
                is empty, then set the root equal to the new 
                node.  Otherwise, use _insert to recursively
                find the location to insert.
                """
                if self.root is None:
                    self.root = BST.Node(data)
                else:
                    self._insert(data, self.root)  # Start at the root

         
          
            def _insert(self, data, node):
                """
                This function will look for a place to insert a node
                with 'data' inside of it.  The current sub-tree is
                represented by 'node'.  This function is intended to be
                called the first time by the insert function.
                """

                if data != node.data:
                    if data < node.data:
                        # The data belongs on the left side.
                        if node.left is None:
                            # We found an empty spot
                            node.left = BST.Node(data)
                        else:
                            # Need to keep looking.  Call _insert
                            # recursively on the left sub-tree.
                            self._insert(data, node.left)
                    else:
                        # The data belongs on the right side.
                        if node.right is None:
                            # We found an empty spot
                            node.right = BST.Node(data)
                        else:
                            # Need to keep looking.  Call _insert
                            # recursively on the right sub-tree.
                            self._insert(data, node.right)
            
  
            def __contains__(self, data):
                """ 
                Checks if data is in the BST.  This function
                supports the ability to use the 'in' keyword:

                if 5 in my_bst:
                    ("5 is in the bst")

                """
                return self._contains(data, self.root)  # Start at the root

            def _contains(self, data, node):
                """
                This funciton will search for a node that contains
                'data'.  The current sub-tree being search is 
                represented by 'node'.  This function is intended
                to be called the first time by the __contains__ function.
                """
            
                
                
                
                
                if not node:
                    return False
                if node.data == data:
                    return True
                if node.data > data:
                    return self._contains(data, node.left)
                if node.data < data:
                    return self._contains(data, node.right)

                


            def __iter__(self):
                """
                Perform a forward traversal (in order traversal) starting from 
                the root of the BST.  This is called a generator function.
                This function is called when a loop	is performed:

                for value in my_bst:
                    print(value)

                """
                yield from self._traverse_forward(self.root)  # Start at the root
                
            def _traverse_forward(self, node):
                """
                Does a forward traversal (in-order traversal) through the 
                BST.  If the node that we are given (which is the current
                sub-tree) exists, then we will keep traversing on the left
                side (thus getting the smaller numbers first), then we will 
                provide the data in the current node, and finally we will 
                traverse on the right side (thus getting the larger numbers last).

                The use of the 'yield' will allow this function to support loops
                like:

                for value in my_bst:
                    print(value)

                The keyword 'yield' will return the value for the 'for' loop to
                use.  When the 'for' loop wants to get the next value, the code in
                this function will start back up where the last 'yield' returned a 
                value.  The keyword 'yield from' is used when our generator function
                needs to call another function for which a `yield` will be called.  
                In other words, the `yield` is delegated by the generator function
                to another function.

                This function is intended to be called the first time by 
                the __iter__ function.
                """
                if node is not None:
                    yield from self._traverse_forward(node.left)
                    yield node.data
                    yield from self._traverse_forward(node.right)
                
            def __reversed__(self):
                """
                Perform a formward traversal (in order traversal) starting from 
                the root of the BST.  This function is called when a the 
                reversed function is called and is frequently used with a for
                loop.

                for value in reversed(my_bst):
                    print(value)

                """        

                
                return self._traverse_backward(self.root)  # Start at the root


            def _traverse_backward(self, node):
                """
                Does a backwards traversal (reverse in-order traversal) through the 
                BST.  If the node that we are given (which is the current
                sub-tree) exists, then we will keep traversing on the right
                side (thus getting the larger numbers first), then we will 
                provide the data in the current node, and finally we will 
                traverse on the left side (thus getting the smaller numbers last).

                This function is intended to be called the first time by 
                the __reversed__ function.        
                """
                
        
                res = []
                if node:
                    res = self._traverse_backward(node.left)
                    res.append(node.data)
                    res = res + self._traverse_backward(node.right)

            
                return res

            
 

            def get_height(self):
                """
                Determine the height of the BST.  Note that an empty tree
                will have a height of 0 and a tree with one item (root) will
                have a height of 1.
                
                If the tree is empty, then return 0.  Otherwise, call 
                _get_height on the root which will recursively determine the 
                height of the tree.
                """
                if self.root is None:
                    return 0
                else:
                    return self._get_height(self.root)  # Start at the root

            def _get_height(self, node):
                """
                Determine the height of the BST.  The height of a sub-tree 
                (represented by 'node') is 1 plus the height of either the 
                left sub-tree or the right sub-tree (whichever one is bigger).

                This function intended to be called the first time by 
                get_height.
                """
                if node is None:
                    return 0 
            
                else :
            
                    # Compute the depth of each subtree
                    lDepth = self._get_height(node.left)
                    rDepth = self._get_height(node.right)
            
                    # Use the larger one
                    if (lDepth > rDepth):
                        return lDepth+1
                    else:
                        return rDepth+1
      


        # NOTE: Functions below are not part of the BST class above. 

        def create_bst_from_sorted_list(sorted_list):
            """
            Given a sorted list (sorted_list), create a balanced BST.  If 
            the values in the sorted_list were inserted in order from left
            to right into the BST, then it would resemble a linked list (unbalanced). 
            To get a balanced BST, the _insert_middle function is called to 
            find the middle item in the list to add first to the BST.  The 
            _insert_middle function takes the whole list but also takes a 
            range (first to last) to consider.  For the first call, the full 
            range of 0 to len()-1 used.
            """
            bst = BST()  # Create an empty BST to start with 
            _insert_middle(sorted_list, 0, len(sorted_list)-1, bst)
 
        def _insert_middle(sorted_list, first, last, bst):
            """
            This function will attempt to insert the item in the middle
            of 'sorted_list' into the 'bst' tree.  The middle is 
            determined by using indicies represented by 'first' and 'last'.
            For example, if the function was called on:

            sorted_list = [10, 20, 30, 40, 50, 60]
            first = 0
            last = 5

            then the value 30 (index 2 which is the middle) would be added 
            to the 'bst' (the insert function above can be used to do this).   

            Subsequent recursive calls are made to insert the middle from the values 
            before 30 and the values after 30.  If done correctly, the order
            in which values are added (which results in a balanced bst) will be:

            30, 10, 20, 50, 40, 60

            This function is intended to be called the first time by 
            create_bst_from_sorted_list.

            The purpose for having the first and last parameters is so that we do 
            not need to create new sublists when we make recursive calls.  Avoid 
            using list slicing to create sublists to solve this problem.

            """



            length = len(sorted_list)
            if length==0: return None
            if length==1: return bst.Node(sorted_list[0])
            root = bst.Node(sorted_list[length//2])
            root.left = _insert_middle(sorted_list[:length//2], 0, 0, bst)
            root.right = _insert_middle(sorted_list[length//2+1:],0,0,bst)
            return root



        # Sample Test Cases (may not be comprehensive) 
        print("\n=========== PROBLEM 1 TESTS ===========")
        tree = BST()
        tree.insert(5)
        tree.insert(3)
        tree.insert(7)
        # After implementing 'no duplicates' rule,
        # this next insert will have no effect on the tree.
        tree.insert(7)  
        tree.insert(4)
        tree.insert(10)
        tree.insert(1)
        tree.insert(6)
        for x in tree:
            print(x)  # 1, 3, 4, 5, 6, 7, 10

        print("\n=========== PROBLEM 2 TESTS ===========")
        print(3 in tree) # True
        print(2 in tree) # False
        print(7 in tree) # True
        print(6 in tree) # True
        print(9 in tree) # False

        print("\n=========== PROBLEM 3 TESTS ===========")
        for x in reversed(tree):
            print(x)  # 10, 7, 6, 5, 4, 3, 1

        print("\n=========== PROBLEM 4 TESTS ===========")
        print(tree.get_height()) # 3
        tree.insert(6)
        print(tree.get_height()) # 3
        tree.insert(12)
        print(tree.get_height()) # 4


        print("\n=========== PROBLEM 5 TESTS ===========")
        tree1 = create_bst_from_sorted_list([10, 20, 30, 40, 50, 60])
        tree2 = create_bst_from_sorted_list([x for x in range(127)]) # 2^7 - 1 nodes
        tree3 = create_bst_from_sorted_list([x for x in range(128)]) # 2^7 nodes
        tree4 = create_bst_from_sorted_list([42])
        tree5 = create_bst_from_sorted_list([])
        print(tree1.get_height()) # 3
        print(tree2.get_height()) # 7 .. any higher and its not balanced
        print(tree3.get_height()) # 8 .. any higher and its not balanced
        print(tree4.get_height()) # 1
        print(tree5.get_height()) # 0
    ```







# YOUR TURN
    ```python
            class add :
                @staticmethod
                def main( args) :
                    tree = BST()
                    tree.insert(30)
                    tree.insert(50)
                    tree.insert(15)
                    tree.insert(20)
                    tree.insert(10)
                    tree.insert(40)
                    tree.insert(60)
                    tree.inorder()
            class Node :
                left = None
                val = 0
                right = None
                def __init__(self, val) :
                    self.val = val
            class BST :
                root = None
                def insert(self, key) :
                    node = Node(key)
                    if (self.root == None) :
                        self.root = node
                        return
                    prev = None
                    temp = self.root
                    while (temp != None) :
                        if (temp.val > key) :
                            prev = temp
                            temp = temp.left
                        elif(temp.val < key) :
                            prev = temp
                            temp = temp.right
                    if (prev.val > key) :
                        prev.left = node
                    else :
                        prev.right = node
                def inorder(self) :
                    temp = self.root
                    stack =  []
                    while (temp != None or not (len(stack) == 0)) :
                        if (temp != None) :
                            #enter your code here
                        else :
                            #enter your code here
                
            if __name__=="__main__":
                add.main([])

    ```