#Create a new list from a two list using the following condition:
#Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

def kontroll(l1, l2):
    list3 = []
    for e in l1:
        if e % 2 != 0:
            list3.append(e)
    for e in l2:
        if e % 2 == 0:
            list3.append(e)
    print(list3)
        
print(kontroll(list1, list2))