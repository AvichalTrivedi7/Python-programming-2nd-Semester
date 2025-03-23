def mode(list1):
    count=0
    element=0
    for i in list1:
        if list1.count(i) > count:
            element=i
            count=list1.count(i)
    print(f'The mode (most appeared element) of the provided list is : {element}')
    print(f'which appeared {count} times...')
            
    
lis= eval(input("Enter the list :"))
mode(lis)
