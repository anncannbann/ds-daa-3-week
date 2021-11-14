#this connects the nodes
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    

#this creates the nodes
class LinkedList:
    def __init__(self):
        self.head = None

    #the head pointer moves through the nodes and prints the list
    def displayList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


if __name__ =='__main__':
    lList = LinkedList()


    #Created different nodes, they are not connected
    lList.head = Node(1)
    second = Node(2)
    third = Node(3)

    #connect first to second
    lList.head.next = second
    #second to third. Head will stay on first only isliye second.next
    second.next = third

    lList.displayList()