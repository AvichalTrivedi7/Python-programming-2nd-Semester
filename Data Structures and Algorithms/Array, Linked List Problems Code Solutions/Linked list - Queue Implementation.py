class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.start_node=None

    def insert_end(self,data):
        new_node=Node(data)
        if not self.start_node:
            self.start_node=new_node
            print(f"Element {data} added !")
            return
        
        ptr=self.start_node
        while ptr.next:
            ptr=ptr.next
            
        ptr.next=new_node
        print(f"Element {data} added !")
        

    def delete_beginning(self):
        if not self.start_node:
            print("Underflow ! No element present.")
            return
        
        temp=self.start_node
        self.start_node=self.start_node.next
        print(f"Element {temp.data} deleted !")

    def display(self):
        ptr=self.start_node
        
        while ptr:
            print(ptr.data,end="->")
            ptr=ptr.next
            
        print(None)


if __name__=="__main__":
    
    ll=LinkedList()
    ll.insert_end(1)
    ll.display()

    ll.insert_end(2)
    ll.display()

    ll.insert_end(3)
    ll.display()

    ll.delete_beginning()
    ll.display()
        
