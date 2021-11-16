class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head 
        while(temp):
            print(temp)
            temp = temp.next

    def deletion(self,key):
        
        if (self.head is None):
            print("No Linked List")
            return

        temp = self.head
        
        if(temp):
            if(temp.head ==key):
                temp.head = None

        while(temp):
            if(temp.data == key):
                break

            prev = temp
            temp = temp.next
        

