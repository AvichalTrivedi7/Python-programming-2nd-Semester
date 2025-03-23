class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

        

class Stack:
    def __init__(self):
        self.start_node=None
        self.count=0
        

    def push(self,data):

        new_node=Node(data)
        if not self.start_node:
            self.start_node=new_node
            self.count+=1
            print(f"Element {data} pushed !")
            return
        
        ptr=self.start_node
        while ptr.next: 
            ptr=ptr.next
        ptr.next=new_node
        self.count+=1
        print(f"Element {data} pushed !")
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
    


    def pop(self):
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
        return


def menu():
    global choice
    print("\n\n\nChoose what you would like to do now at the workspace")
    print("*******************************")
    print("1. Create the Stack\n2. Push an element in the Stack\n\
3. Traverse through the Stack and Display it and Size of it\n4. Search an element of choice\n\
5. Pop an element off the stack\n6. Exit\n")
    print("*******************************")
    choice=input()

    
if __name__=="__main__":
    stk=0
    menu()
    global limit
    limit=None
    
    while True:            
        if choice=="1":
            if stk!=0:
                stk.start_node = None
                stk.count = 0
            limit=input("Please enter the size of Stack: ")
            if limit.isdigit():
                limit=int(limit)
                stk=Stack()
                print("Stack created !")
                menu()
            else:
                print("Please enter the size correctly ...\n")
                menu()
            

        
        elif choice=="2":                
            if stk!=0:
                if stk.count>=limit:
                        print("Overflow!! Kindly delete some elements first")
                        print(f"The limit is {limit}")
                        menu()
                else:
                    element=input("Enter the element to be pushed: ")
                    stk.push(element)
                    menu()
                    
            else:
                print("Please create the Stack first using option 1.")
                menu()


                
        elif choice=="3":
            if stk!=0:
                print("\nThe Stack is ---> \n")
                stk.display()
                menu()

            else:
                print("Please create the Stack first using option 1. There is nothing to display before that.")
                menu()

            

        elif choice=="4":
            if stk!=0:
                element=input("Enter the element you want to search: ")
                if stk.search(element):
                    print(f"The element {element} is found")
                    menu()
                else:
                    print(f"The element {element} was not found")
                    menu()

            else:
                print("Please create the Stack first using option 1.")
                menu()


                
        elif choice=="5":
            if stk!=0:
                stk.pop()
                menu()

            else:
                print("Please create the Stack first using option 1.")
                menu()

                
                
        elif choice=="6":
            break


                
        else:
            print("Incorrect entry, Please enter from the list of choices.")
            menu()

