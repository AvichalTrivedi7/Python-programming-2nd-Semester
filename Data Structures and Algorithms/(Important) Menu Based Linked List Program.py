class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

        

class LinkedList:
    def __init__(self):
        self.start_node=None
        self.count=0



    def insert_begin(self,data):
        new_node=Node(data)
        new_node.next=self.start_node
        self.start_node=new_node
        self.count+=1
        print("Element added !")
        


    def insert_after_value(self,prev_value,data):
        ptr=self.start_node
        while ptr:
            if ptr.data==prev_value:
                new_node=Node(data)
                new_node.next=ptr.next
                ptr.next=new_node
                self.count+=1
                print("Element added !")
                return
            ptr=ptr.next
            
        print(f"Node with data {prev_value} not found!")



    def append(self,data):
        new_node=Node(data)
        if not self.start_node:
            self.start_node=new_node
            self.count+=1
            print("Element added !")
            return
        
        ptr=self.start_node
        while ptr.next: 
            ptr=ptr.next
        ptr.next=new_node
        self.count+=1
        print("Element added !")

        

    def display(self):
        ptr=self.start_node
        
        while ptr:
            print(ptr.data,end="->")
            ptr=ptr.next
    
        print(None)
        print(f"The total size ---> {self.count}")



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



    def delete_beginning(self):
        if not self.start_node:
            print("Underflow ! No element to be deleted.")
            return
        temp=self.start_node
        self.start_node=self.start_node.next
        self.count-=1
        print(f"Element <{temp.data}> deleted !")

        
         
    def delete_after(self, prev):
        if ll.search(prev):
            if not self.start_node:

                print("Underflow ! No element to be deleted.")
                return
            ptr=self.start_node
            while ptr.data!=prev:
                ptr=ptr.next

            if ptr.data==prev and ptr.next==None:
                print("There is no element after the element {prev} to delete")
                return

            if ptr.next==None:
                print("The element was not found")
                return
            
            temp=ptr.next
            ptr.next=ptr.next.next
            self.count-=1
            print(f"Element <{temp.data}> deleted !")
        else:
            print("The prev element was not found")  
            return



    def delete_end(self):
        if not self.start_node:
            print("Underflow ! No element to be deleted.")
            return

        if not self.start_node.next:
            temp=self.start_node
            self.start_node=None
            self.count-=1
            print(f"Element <{temp.data}> deleted !")
            
            return
            
        
        ptr=self.start_node
        while ptr.next.next:
            ptr=ptr.next
            
        temp=ptr.next
        ptr.next=None
        self.count-=1
        print(f"Element <{temp.data}> deleted !")



def menu():
    global choice
    print("\n\n\nChoose what you would like to do now at the workspace")
    print("*******************************")
    print("1. Create the Linked List\n2. Insert elements in the Linked List\n\
3. Traverse through the Linked List and Display it and Size of it\n4. Search an element of choice\n\
5. Delete an Element in the Linked List\n6. Exit\n")
    print("*******************************")
    choice=input()

    
if __name__=="__main__":
    ll=0
    menu()
    global limit
    limit=None
    
    while True:            
        if choice=="1":
            if ll!=0:
                ll.start_node = None
                ll.count = 0
            limit=input("Please enter the size of linked list: ")
            if limit.isdigit():
                limit=int(limit)
                ll=LinkedList()
                print("Linked list created !")
                menu()
            else:
                print("Please enter the size correctly ...\n")
                menu()
            

        
        elif choice=="2":                
            if ll!=0:
                if ll.count>=limit:
                        print("Overflow!! Kindly delete some elements first")
                        print(f"The limit is {limit}")
                        menu()
                else:
                    
                    print("Choose where to insert")
                    intra=input("1 -> Beginning of the linkedlist\n2-> Somewhere in Between\n\
3 -> At the end\n4 -> Exit\n")
                    
                    if intra=="1":
                        element=input("Enter the element to be added: ")
                        ll.insert_begin(element)
                        menu()
                    
                    elif intra=="2":
                        place=input("Enter the element after which you want your new element: ")
                        element=input("Enter the element to be added: ")
                        ll.insert_after_value(place,element)
                        menu()
                    
                    elif intra=="3":
                        element=input("Enter the element to be added: ")
                        ll.append(element)
                        menu()

                    elif intra=="4":
                        menu()

                    else:
                        print("Incorrect entry, Please enter from the list\n")
                        menu()
                    
            else:
                print("Please create the list first using option 1.")
                menu()


                
        elif choice=="3":
            if ll!=0:
                print("\nThe linked list is ---> \n")
                ll.display()
                menu()

            else:
                print("Please create the list first using option 1. There is nothing to display before that.")
                menu()

            

        elif choice=="4":
            if ll!=0:
                element=input("Enter the element you want to search: ")
                if ll.search(element):
                    print(f"The element {element} is found")
                    menu()
                else:
                    print(f"The element {element} was not found")
                    menu()

            else:
                print("Please create the list first using option 1.")
                menu()


                
        elif choice=="5":
            if ll!=0:
                print("Choose where to delete")
                intra=input("1 -> Beginning of the linkedlist\n2-> Somewhere in Between\n\
3 -> At the end\n4 -> Exit\n")
                
                if intra=="1":
                    ll.delete_beginning()
                    menu()
                    
                elif intra=="2":
                    place=input("Enter the element that is just behind the element to be deleted: ")
                    ll.delete_after(place)
                    menu()

                elif intra=="3":
                    ll.delete_end()
                    menu()

                elif intra=="4":
                    menu()

                else:
                    print("Incorrect entry, Please enter from the list\n")
                    menu()
                    
            else:
                print("Please create the list first using option 1.")
                menu()

                
                
        elif choice=="6":
            break


                
        else:
            print("Incorrect entry, Please enter from the list")
            menu()

