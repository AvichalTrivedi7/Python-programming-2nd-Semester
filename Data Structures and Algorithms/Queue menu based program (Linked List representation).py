class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

        

class Queue:
    def __init__(self):
        self.start_node=None
        self.count=0
        

    def enqueue(self,data):
        new_node=Node(data)
        if not self.start_node:
            self.start_node=new_node
            self.count+=1
            print(f"Element {data} enqueued !")
            return
        
        ptr=self.start_node
        while ptr.next: 
            ptr=ptr.next
        ptr.next=new_node
        self.count+=1
        print(f"Element {data} enqueued !")
        return

        

    def display(self):
        ptr=self.start_node
        
        while ptr:
            print(ptr.data,end="->")
            ptr=ptr.next
    
        print(None)
        print(f"The total size ---> {self.count}")
        return



    def search(self,key):
        ptr=self.start_node
        c=0
        while ptr:
            c+=1
            if str(ptr.data)==key:
                print(f"At place no. {c}")
                return True
            ptr=ptr.next
        return False
    


    def dequeue(self):
        if not self.start_node:
            print("Underflow ! No element to be deleted.")
            return
        temp=self.start_node
        self.start_node=self.start_node.next
        self.count-=1
        print(f"Element <{temp.data}> deleted !")
    


def menu():
    global choice
    print("\n\n\nChoose what you would like to do now at the workspace")
    print("*******************************")
    print("1. Create the Queue\n2. Enqueue an element in the Queue\n\
3. Traverse through the Queue and Display it and Size of it\n4. Search an element of choice\n\
5. Dequeue an element off the Queue\n6. Exit\n")
    print("*******************************")
    choice=input()

    
if __name__=="__main__":
    que=0
    menu()
    global limit
    limit=None
    
    while True:            
        if choice=="1":
            if que!=0:
                que.start_node = None
                que.count = 0
            limit=input("Please enter the size of Queue: ")
            if limit.isdigit():
                limit=int(limit)
                que=Queue()
                print("Queue created !")
                menu()
            else:
                print("Please enter the size correctly ...\n")
                menu()
            

        
        elif choice=="2":                
            if que!=0:
                if que.count>=limit:
                        print("Overflow!! Kindly delete some elements first")
                        print(f"The limit is {limit}")
                        menu()
                else:
                    element=input("Enter the element to be enqueued: ")
                    que.enqueue(element)
                    menu()
                    
            else:
                print("Please create the Queue first using option 1.")
                menu()


                
        elif choice=="3":
            if que!=0:
                print("\nThe Queue is ---> \n")
                que.display()
                menu()

            else:
                print("Please create the Queue first using option 1. There is nothing to display before that.")
                menu()

            

        elif choice=="4":
            if que!=0:
                element=input("Enter the element you want to search: ")
                if que.search(element):
                    print(f"The element {element} is found")
                    menu()
                else:
                    print(f"The element {element} was not found")
                    menu()

            else:
                print("Please create the Queue first using option 1.")
                menu()


                
        elif choice=="5":
            if que!=0:
                que.dequeue()
                menu()

            else:
                print("Please create the Queue first using option 1.")
                menu()

                
                
        elif choice=="6":
            break


                
        else:
            print("Incorrect entry, Please enter from the list of choices.")
            menu()

