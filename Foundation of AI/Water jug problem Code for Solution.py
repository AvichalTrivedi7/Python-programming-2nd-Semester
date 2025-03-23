
jug1=[] #4L
jug2=[] #3L

#Fill the jug2 (3L) completely
for i in range(3):
    jug2.append(1)
print("Jug1 has been filled completely --->",jug1)
print("Jug2 is empty for now --->",jug2)
print("**********************\n")

#Empty the jug1 into jug2
for i in range(3):
    jug2.append(jug1.pop())
print(f"Jug1 has been emptied in Jug2, hence Jug1 {jug1} and Jug2 {jug2}")
print("**********************\n")

#Empty the jug2
jug2.clear()
print(f"Jug2 has been emptied, hence Jug1 {jug1} and Jug2 {jug2}")
print("**********************\n")

#Pour 1L from jug1 to jug2
jug2.append(jug1.pop())
print(f"1L from Jug1 is poured into Jug2, hence Jug1 {jug1} and Jug2 {jug2}")
print("**********************\n")

#Fill the jug1 again
for i in range(4):
    jug1.append(1)
print(f"Jug1 is filed again, hence Jug1 {jug1} and Jug2 {jug2}")
print("**********************\n")

#Empty in the jug2 again and you have jug1 filled with 2L
for i in range(2):
    jug2.append(jug1.pop())

print("Jug1 is emptied into Jug2 and we have Jug1 filled with 2L")
print(f"Hence Jug1 {jug1} and Jug2 {jug2}")
print("**********************\n")
