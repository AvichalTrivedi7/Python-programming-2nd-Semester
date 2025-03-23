# User Input Matrix, Menu Based - Addition, Substraction

import numpy as np

def menu():
    print("Choose what you want to do with the matrices: \n1) Addition \n2) Subtraction\n")
    choice=input("Enter 1 or 2\n")
    if choice=="1":
        mat=matrix1+matrix2
        print(f"Result matrix ---> \n{mat}")
    elif choice=="2":
        mat=matrix1-matrix2
        print(f"Result matrix ---> \n{mat}")
    else:
        print("Please choose from the provided choices\n")
        menu()
        

matrix1=np.array(eval(input("Enter the matrix1 in the form of a nested list (Inner lists as rows): ")))
x=matrix1.shape
matrix2=np.array(eval(input("Enter the matrix2 in the form of a nested list (Inner lists as rows): ")))
y=matrix2.shape

if x==y:
    menu()
else:
    print("Please enter the matrices which can be added or subtracted.")
