class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
 
class DLList:
 
    def __init__(self):
        self.head = None
 
    def insertAfter(self,new_data,pos):
        new_node = Node(new_data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            i=1
            while temp.next is not None and i<pos:
                temp=temp.next
                i=i+1
            new_node.next=temp.next
            temp.next = new_node
            new_node.prev = temp
            if new_node.next:
                new_node.next.prev = new_node
            node=self.head
        while node:
            print(node.data)
            last = node
            node = node.next

    def insertBegin(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        self.head.prev=new_node
        new_node.next=self.head
        self.head=new_node
        node=self.head
        while node:
            print(node.data)
            last = node
            node = node.next
        
    def insertatend(self, new_data):
            new_node = Node(new_data)
            if self.head is None:
                self.head = new_node
                return
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
            new_node.prev = last
            node=self.head
            while node:
                print(node.data)
                last = node
                node = node.next   
            return
    def append(self, new_data):
            new_node = Node(new_data)
            if self.head is None:
                self.head = new_node
                return
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
            new_node.prev = last 
            return
         
 
    def printList(self):
        node=self.head
        print("\ndisplay")
        while node:
            print(node.next)
            last = node
            node = node.next
    def reverse(self):
        node=self.head
        while node:
            last = node
            node = node.next
        print("\nTraversal in reverse direction")
        while last:
            print(last.data)
            last = last.prev
    def deleteNode(self, del_node):
    
        if(self.head == None or del_node == None):
            print("Node not found")
            return
        if(self.head == del_node):
            self.head = del_node.next
        if(del_node.next != None):
            del_node.next.prev = del_node.prev
        if(del_node.prev != None):
            del_node.prev.next = del_node.next
        node=self.head
        while node:
            print(node.data)
            last = node
            node = node.next
    
    def deleteNodeAtPos(self,n):
        if (self.head == None or n <= 0):
            return
        current = self.head
        i = 0
        while ( current != None and i < n ):
            current = current.next
            i = i + 1
        if (current == None):
            return
        l.deleteNode(current)
        
    def getNode(self,data):
        temp=self.head
        while temp:
            if data==temp.data:
                return temp
            temp=temp.next
        node=self.head
        while node:
            print(node.data)
            last = node
            node = node.next
     
l=DLList()
N=int(input("Enter how many elements in linked list: "))
for i in range(N):
    data=int(input("Enter data: "))
    l.append(data)
while True:
    choice=int(input("Enter 1.Display/Forward Traversal 2.Insert at begininng 3.Insert at end 4.Insert after position \n5.Delete at index 6.Delete node 7.reverse 8.Exit: "))
    if choice==1:
        l.printList()
    elif choice==2:
        d=int(input("Enter data to add in the begining"))
        l.insertBegin(d)
    elif choice==3:
        d=int(input("Enter data to add at the end :"))
        l.insertatend(d)
    elif choice==4:
        d=int(input("Enter data : "))
        p=int(input("Enter position : "))
        l.insertAfter(d,p)
    elif choice==5:
        n=int(input("Enter postion to delete the node :"))
        l.deleteNodeAtPos(n)
    elif choice==6:
        d=int(input("Enter data to delete the node :"))
        node=l.getNode(d)
        l.deleteNode(node)
   
    elif choice==7:
        l.reverse()
    else:
        break