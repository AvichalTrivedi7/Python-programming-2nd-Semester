#Stack menu based program (array representation)

def menu():
    global choice
    print("\n\n\nChoose what you would like to do now at the workspace")
    print("*******************************")
    print("1. Push\n2. Peek\n3. Pop\n4. Display\n5. Exit\n")
    print("*******************************")
    choice=input()


if __name__=="__main__":
    import numpy as np
    
    print("Your stack has been created. It is empty now.")
    arr1 = []
    stk = np.array(arr1)
    print(stk)

    menu()
    
    while True:            
        if choice=="1":
            ele=input("Enter the element to be pushed: ")
            stk = np.append(stk, ele)
            print(f"The element `{ele}` has been pushed into the stack.")
            print(f"The size of the stack: `{stk.size}`.")
            menu() 
    
        elif choice=="2":
            if stk.size>0:
                print(f"The element at the TOP is `{stk[-1]}`.")
                menu()
            else:
                print("Empty stack.")
                menu()
                
        elif choice=="3":
            if stk.size>0:
                print(f"The element `{stk[-1]}` has been popped out of the stack.")
                stk = np.delete(stk, [-1])
                menu()
            else:
                print("Empty stack.")
                menu()
                

        elif choice=="4":
            if stk.size>0:
                print(f"The elements in the stack are `{stk}`.")
                menu()
            else:
                print("Empty stack.")
                menu()

        elif choice=="5":
            break

        else:
            print("Incorrect entry, Please enter from the list of choices.")
            menu()




