def Max(List):
    maxNo = List[0]
    for i in range(len(List)):
        if List[i] > maxNo:
            maxNo = List[i]
    i = i + 1
    return maxNo
List1 = [1, 3, 6, 10, 11]
List2 = [10, 30, 60, 100, 110]
maxNo = Max(List1)
print(maxNo)

maxNo = Max(List2)
print("this is the")
print(maxNo)

    


""""

List = [1, 3, 6, 10, 11]
maxNo = List[0]
for i in range(len(List)):
    if List[i] > maxNo:
        maxNo = List[i]
    i = i + 1
print(maxNo)

#####################################3

List1 = [1, 3, 6, 10, 11]
maxNo1 = List1[0]
i = 0
while i < 5:
    if List[i] > maxNo1:
        maxNo1 = List[i]
    i = i + 1
print(maxNo1)
"""
