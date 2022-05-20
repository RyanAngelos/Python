# TODO list rakendus
    # CRUD - Create Reade Update Delete
    # Igal asjal on due date
    # Kui tegid midagi ära, liigutatakse element tehtud asjade nimekirja
    # Saad määrata asjadele prioriteeti - Näiteks Kõige tähtsam, Tähtis, Võiks teha, Pohhuj võib kunagi hiljem
    # Optional
        # Projektid - todo liste saab jaotada eraldi gruppidesse
    
"""
TIITEL                                                                          STATUS:
    -Kuvab tervituse                                                            TEHTUD
    Ava Projekt                                                                 TEHTUD
        -kuvab tehtud ja tegemata projektid                                     TEHTUD 
        Ava projekt                                                             TEHTUD 
            -kuvab tehtud ja tegemata taske prioriteedi järjekorras             
            Vali task
                -kuvab taski
                Muuda prioriteeti
                Kustuta
                Muuda nime
                Redigeeri
                Märgi tehtuks
        Muuda nime
        Kustuta
        Märgi tehtuks
    Ava unassigned
        -kuvab tehtud ja tegemata taske prioriteedi järjekorras
            Vali task
                -kuvab taski
                Muuda prioriteeti
                Kustuta
                Muuda nime
                Redigeeri
                Märgi tehtuks
        Muuda nime
        Kustuta
        Märgi tehtuks
    Loo uus projekt
        Projekti nimi
            Lisa taske unassigned listist
            Lisa uus task
    Loo uus task
        Taski nimi
            Taski tekst
                Lisa prioriteet
    OPTIONAL
        Sätted
            Format
            Muuda nime
"""
#GLOBAL
import csv
import os
kasutaja_valik = ""

#Kasutajanimega tervitus, kasutajanime loomine
with open("kasutajanimi.txt", "r") as r:
    kasutajanimisisu = r.read()
    if kasutajanimisisu != "":
        print("Tere, " + kasutajanimisisu + "!")
        r.close()
    else:
        with open("kasutajanimi.txt", "w") as r:
            r.write(input("Kuidas on Teie nimi? "))
            print("Tere, " + kasutajanimisisu + "!")
            r.close()


#Avamenüü
print(kasutajanimisisu + ", kuidas soovid käituda?")
print("\nAva projekt  - 1")
print("Ava task     - 2")
print("Uus projekt  - 3")
print("Uus task     - 4")
kasutaja_valik = input()

#PROJEKTIPÕHINE NAVIGEERIMINE
if kasutaja_valik == "1":
    
    #Projektide nimekiri
    with open('andmed.csv', newline='') as csvfile:
        data = csv.DictReader(csvfile)
        emp = []
        s = 0
        print("Siin on nimekiri teie projektidest:\n")
        for row in data:
            emp.append(row["Projekt"])
    csvfile.close

    emp = list(set(emp))
    for e in emp:
        s = s + 1
        print(e + "\t- " + str(s))

    print("\nMillist projekti soovite käsitleda?")
    kasutaja_valik_2 = input()

    print("\nKuidas soovite käituda?")
    print("\n-" + emp[int(kasutaja_valik)- 1] + "-")    
    print("\nAva              - 1")
    print("Muuda nime       - 2")
    print("Kustuta          - 3")
    print("Tagasi           - 4")
    kasutaja_valik = input()    
    
""" if kasutaja_valik == 1:
        print("\t-" + emp[int(kasutaja_valik_2)- 1] + "-")
        with open('andmed.csv', newline='') as csvfile:
            for line in csvfile:"""
                
            
    

        





#if kasutaja_valik == "2":
    #print("Siin on nimekiri teie taskidest:")

#if kasutaja_valik == "3":
    #print("kuidas soovite nimetada oma uut projekti?")

#if kasutaja_valik == "4":
    #print("Kuidas soovite nimetada oma uut taski?")
