def loo_dict(a, b):
    dict1 = dict(zip(a,b))
    if len(a) == len(b):
        print(dict1)
    else:
        print (dict())

l1 = [1, 2, 3]
l2 = ["a", "abc 123", "fortnait"]
l3 = ["Lembit", "Visnapuu", "on", "rassist"]
l4 = ["a", "b", "c", "d"]

print (loo_dict(l4, l3))

