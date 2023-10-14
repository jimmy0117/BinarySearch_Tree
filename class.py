class Node(): #節點
    def __init__(self,v):
        self.value = v #value值 
        self.left = None
        self.right = None

def add(n):
    temp = root
    while(temp!=None):
        if(temp.value>n):
            if(temp.left==None):
                temp.left = Node(n)
                return
            temp = temp.left
        if(temp.value<n):
            if(temp.right==None):
                temp.right = Node(n)
                return
            temp = temp.right 
def BinarySearch(n):
    temp = root
    while(temp!=None):
        if(temp.value==n):
            return n
        elif(temp.value>n):
            temp = temp.left
        elif(temp.value<n):
            temp = temp.right
    return -1

def PreOrder(n:Node):  #前序 中左右
    if n!=None:
        print(n.value)
        PreOrder(n.left)
        PreOrder(n.right)
def InOrder(n:Node):   #中序 左中右
    if n!=None:
        InOrder(n.left)
        print(n.value)
        InOrder(n.right)
def PostOrder(n:Node): #後序 左右中
    if n!=None:
        PostOrder(n.left)
        PostOrder(n.right)
        print(n.value)
global root
root = Node(5)
print(root.value)

value_list = [3,7,2,4,6,8]

for i in value_list:
    add(i)
PostOrder(root)
