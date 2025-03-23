def word_count(s):
    list1= s.split()
    list2= [list1.count(i) for i in list1] 
    return {word:count for word,count in zip(list1,list2)}

sentence=input("Enter the sentence: ")
print(word_count(sentence))

