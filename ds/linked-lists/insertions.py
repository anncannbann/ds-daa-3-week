class Node:
    def __init__(self,data):
        self.data = data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        print("LinkedList is:")
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


    def push_in_Front(self,new_data): # time complexity 0(1)
        print(("Adding to the Front"))

        #STEP1&2: make new Node and send data of new node
        new_node = Node(new_data)

        #STEP3: NEW NODE NEXT TO HEAD
        new_node.next = self.head

        #STEP4: Move HEAD
        self.head = new_node

    def in_between(self,prev,new_data):
        print("adding after Node")
        if prev is None:
            print("Node doesnt Exist")
            return

        new_node = Node(new_data)

        new_node.next = prev.next

        prev.next = new_node

    def in_the_end(self,new_data):
        print("adding in the end")

        new_node = Node(new_data)
        #new_node.next = None

        if(self.head is None):
           self.head = new_node
           print('New node made')
           return

        else:
            temp = self.head
            while(temp.next):
                temp =temp.next
            temp.next = new_node


if __name__=='__main__':
    
    ll =LinkedList()

    ll.in_the_end(6)
    ll.push_in_Front(7)
    ll.push_in_Front(1)
    ll.in_the_end(4)
    ll.in_between(ll.head.next,8)
    ll.display()