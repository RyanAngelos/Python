kujund = input("Palun sisesta geomeetriline kujund:")

if (kujund == "ring"):
    raadius = float(input("Palun sisesta raadius (cm):"))
    pindala = 3.14 * raadius ** 2
    print("Pindala on " + str(round(pindala, 2)) + " cm^2")

elif (kujund == "ruut"):
    külg = float(input("Palun sisesta küljepikkus (cm):"))
    pindala = külg ** 2
    print("Pindala on " + str(pindala) + " cm^2")

elif (kujund == "ristkülik"):
    külg1 = float(input("Palun sisesta esimese külje pikkus (cm):"))
    külg2 = float(input("Palun sisesta teise külje pikkus (cm):"))
    pindala = (külg1 + külg2) * 2
    print("Pindala on " + str(pindala) + "cm^2")

elif (kujund == "kolmnurk"):
    külg1 = float(input("Palun sisesta küljepikkus (cm):"))
    pindala = (3 * 0.5) * (külg1 ** 2) /4
    print("Pindala on " + str(pindala) + "cm^2")

else:
    print ("Antud sisend ei ole toetatud kujund")