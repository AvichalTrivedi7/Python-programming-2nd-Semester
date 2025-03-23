def sorted_dict(d):
    dict1= sorted(d.items(),key=lambda item:item[1])
    return dict(dict1)

print(sorted_dict({"hi":10,"bye":5,"see you":15,"take care":30,"night":0}))
