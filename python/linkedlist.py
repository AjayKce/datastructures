class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        
    def insert(self,data):
        if(self.head == None):
            self.head=Node(data)
        else:
            temp = self.head
            while temp.next:
                temp=temp.next
            temp.next = Node(data)
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp=temp.next
            
    def pushatfirst(self, new_data): 
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node 
    
    def delete(self, position): 
        if self.head == None: 
            return 
        temp = self.head 
        if position == 0: 
            self.head = temp.next
            temp = None
            return 
        for i in range(position -1 ): 
            temp = temp.next
            if temp is None: 
                break
        if temp is None: 
            return 
        if temp.next is None: 
            return 
        
        next = temp.next.next
        temp.next = None
        temp.next = next


if __name__=='__main__':
    li = LinkedList()
    li.insert(2)
    li.insert(6)
    li.insert(16)
    li.pushatfirst(8)
    li.delete(1)
    li.printList()
