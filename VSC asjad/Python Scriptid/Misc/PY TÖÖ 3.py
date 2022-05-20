def counter(a):
    loetelu = dict()
    
    for e in a:
        if e in loetelu:
            loetelu[e] += 1
        else:
            loetelu[e] = 1

    print("Tähed lauses:\n " + str(loetelu))

counter(input("Sisesta tekst: "))