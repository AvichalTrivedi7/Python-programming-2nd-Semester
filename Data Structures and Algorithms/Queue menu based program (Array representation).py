def menu():
    global choice
    print("\n\n\nChoose what you would like to do now at the workspace")
    print("*******************************")
    print("1. Enqueue\n2. Check End\n3. Dequeue\n4. Display\n5. Exit\n")
    print("*******************************")
    choice=input()


if __name__=="__main__":
    import numpy as np
    
    print("Your queue has been created. It is empty now.")
    arr1 = []
    que = np.array(arr1)
    print(que)

    menu()
    
    while True:            
        if choice=="1":
            ele=input("Enter the element to be enqueued: ")
            que = np.append(que, ele)
            print(f"The element `{ele}` has been enqueued into the queue.")
            print(f"The size of the queue: `{que.size}`.")
            menu() 
    
        elif choice=="2":
            if que.size>0:
                print(f"The element at the END is `{que[-1]}`.")
                menu()
            else:
                print("Empty queue.")
                menu()
                
        elif choice=="3":
            if que.size>0:                
                print(f"The element `{que[0]}` has been dequeued out of the queue.")
                que = np.delete(que, [0])
                menu()
            else:
                print("Empty queue.")
                menu()

        elif choice=="4":
            if que.size>0:
                print(f"The elements in the queue are `{que}`.")
                menu()
            else:
                print("Empty queue.")
                menu()

        elif choice=="5":
            break

        else:
            print("Incorrect entry, Please enter from the list of choices.")
            menu()

