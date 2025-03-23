import numpy as np

x="x"
o="o"
list1=eval(input("Enter the row1 for the array :"))
list2=eval(input("Enter the row2 for the array :"))
list3=eval(input("Enter the row3 for the array :"))

arr=np.array([list1,list2,list3])
print(f"This is your current board position ---> \n{arr}")

def check(pos):
    flag=0
    global winner
    winner=0
    #for rows
    if pos[0,0]==pos[0,1]==pos[0,2]!=None:
            flag+=1
            winner=pos[0,0]
    elif pos[1,0]==pos[1,1]==pos[1,2]!=None:
            flag+=1
            winner=pos[1,0]
    elif pos[2,0]==pos[2,1]==pos[2,2]!=None:
            flag+=1
            winner=pos[2,0]

    #for columns
    elif pos[0,0]==pos[1,0]==pos[2,0]!=None:
            flag+=1
            winner=pos[0,0]
    elif pos[0,1]==pos[1,1]==pos[2,1]!=None:
            flag+=1
            winner=pos[0,1]
    elif pos[0,2]==pos[1,2]==pos[2,2]!=None:
            flag+=1
            winner=pos[0,2]

    #for diagonals
    elif pos[0,0]==pos[1,1]==pos[2,2]!=None:
        flag+=1
        winner=pos[0,0]
    elif pos[0,2]==pos[1,1]==pos[2,0]!=None:
        flag+=1
        winner=pos[0,2]
        
    return flag

if check(arr)==1:
    print(f"Player <{winner}> has won the game !")
else:
    print("Draw")



        
            
            

