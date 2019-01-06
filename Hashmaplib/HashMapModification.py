# Program for Modifications in  Hash Table 
class Node: 
  
    # Constructor to create a new node 
    def __init__(self, key): 
        self.key = key  
        self.left = None
        self.right = None
  
  
# Traverse and print Function 
def inorder(root): 
    if root is not None: 
        inorder(root.left) 
        print (root.key) 
        inorder(root.right) 
  
  
# A utility function to insert a new node 
def insert(node, key): 
  
    if node is None: 
        return Node(key) 
  
    if key < node.key: 
        node.left = insert(node.left, key) 
    else: 
        node.right = insert(node.right, key) 
  
    return node 
  
# delete the key 
def deleteNode(root, key): 
  
    # Base Case 
    if root is None: 
        return root  
  
    # key is smaller 
    if key < root.key: 
        root.left = deleteNode(root.left, key) 
  
    # Key is Greater 
    elif(key > root.key): 
        root.right = deleteNode(root.right, key) 
  
  #key is root
    else: 
          
        if root.left is None : 
            temp = root.right  
            root = None 
            return temp  
              
        elif root.right is None : 
            temp = root.left  
            root = None
            return temp 
  
        temp = minValueNode(root.right)   
        root.key = temp.key 
        root.right = deleteNode(root.right , temp.key) 
  
  
    return root  

#Returns Min Value
def minValueNode( node): 
    
    current = node 
  
    while(current.left is not None): 
        current = current.left  
  
    return current  

#search the element
def Lookup(root, key):
    
    
    if not root:
        return 'Not Found'
    
    if root.key == key:
        return 'Found'

    elif root.key < key:
        return Lookup(root.right, key)
    
    elif root.key > key:
        return Lookup(root.left, key)

def display():  
    
    #print ("elements are")
    inorder(root) 
    #print ("\n")

 
# root = None
# root = insert(root, 50) 
# root = insert(root, 30) 
# root = insert(root, 20) 
# root = insert(root, 40) 
# root = insert(root, 80) 

# print('\nList is ')
# display()
# root = deleteNode(root, 20)

# print('\nList after deleting 20 is: ')
# display()

# root = insert(root, 70) 
# root = insert(root, 60) 

# print('\n New Elemnts Inserted:')
# display()


# find = Lookup(root, 81)
# print('\n finding element',find)
 

 
