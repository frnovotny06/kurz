from logging.config import stopListening

numbers = [1, 2, 4, -6, 7, 8, 100, -125, 11, 123]
names = ["Petr", "Ales", "Honza", "Lenka", "Andrea", "Alice"]
random_codes = ["1-okdsaaa", "0-nFnldd", "0-AA", "0-uwqqq", "2-ZSTh", "0-RKOcsxxx", "1-LwWtss", "0-cdKiddd", "2-KpAAaa", "3-sOdSxhcds"]

o=0
for x in numbers:
    if x >= o:
     print(x)

print(" ")



i = 0

while i < len(names) and names[i] != "Alice":
    print(names[i])
    if names[i] == "Alice" :
        break
    i += 1

newlist = []

for y in random_codes:
    if "0" in y:
        newlist.append(y)
print(newlist)
