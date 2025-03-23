def reverse_string(s):
    if s:
        return reverse_string(s[1:])+s[0]
    else:
        return ""
    
string= input("Enter the string to be reversed :")
print(reverse_string(string))
