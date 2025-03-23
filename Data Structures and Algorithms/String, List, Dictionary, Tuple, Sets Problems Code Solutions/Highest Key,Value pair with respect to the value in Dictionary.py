def find_largest(d):
    highest_value= max(d.values())
    corresponding_key= [key for key,value in d.items() if value==highest_value]
    
    print(f"The highest key : value pair with respect to the value is ---> {corresponding_key[0]}:{highest_value}")

    
find_largest({"hi":10,"bye":5,"see you":15,"take care":30,"night":0})
