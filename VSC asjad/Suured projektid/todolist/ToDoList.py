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
        Ava task                                                                TEHTUD 
            -kuvab tehtud ja tegemata taske prioriteedi järjekorras             TEHTUD
            Vali task                                                           TEHTUD
                -kuvab taski                                                    TEHTUD
                Muuda prioriteeti                                               
                Redigeeri                                                       
                Märgi tehtuks                                                   
        Muuda nime                                                              ------
        Kustuta                                                                 TEHUTD
        Märgi tehtuks                                                           ------
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
from dataclasses import field
kasutaja_valik = ""
import pandas as pd

###SEE SITT ON KUSAGILT STACKOVERFLOWST ma ei ole kindel kuidas see töötab aga ma ei suutnud ise lahendust välja mõelda
###answered Jul 25, 2021 at 10:36 Gavriel Cohen
def remove_specific_row_from_csv(file, column_name, *args):#kustutab taski

 
    #:param file: file to remove the rows from
    #:param column_name: The column that determines which row will be deleted
    #(e.g. if Column == Name and row-*args contains "Gavri", All rows that contain this word will be deleted)
    #:param args: Strings from the rows according to the conditions with the column
   
    row_to_remove = []
    for row_name in args:
        row_to_remove.append(row_name)
    try:
        df = pd.read_csv(file)
        for row in row_to_remove:
            df = df[eval("df.{}".format(column_name)) != row]
        df.to_csv(file, index=False)
    except Exception  as e:
        raise Exception("Error message....")

def taskide_kuvar(index):#Teeb lahti csv faili, ja kuvab kõik taski nimed valitud projekti nime all
    #loeb csv faili
    with open('andmed.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        emp2 = []
        s = 0
        #paneb taski nimed listi
        for row in reader:
            s = s + 1
            if row["Projekt"] == index:
                emp2.append(row["Taski Nimi"])
                print( str(s) + ") " + row["Taski Nimi"])
                print("   Tähtaeg: " + row["Tahtaeg"] + row["Prioriteet"]"\n")
            else:
                pass
        emp2 = list(set(emp2))
        csvfile.close
    
    #Taskide nimekiri
    print("Millist taski soovite vaadata?")
    kasutaja_valik = input()
    sittpask = emp2[int(kasutaja_valik) - 1]
    kasutaja_valik = sittpask
    print("\t-" + sittpask + "-\n")

    with open('andmed.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["Taski Nimi"] == kasutaja_valik:
                print(row["Taski sisu"])
                print("\nTähtaeg: " + row["Tahtaeg"])
        csvfile.close



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
print("Uus task     - 4\n")
kasutaja_valik = input()



if kasutaja_valik == "1": #AVAB PROJEKTID
    
    #Projektide nimekiri
    with open('andmed.csv') as csvfile:
        data = csv.DictReader(csvfile)
        emp = []
        s = 0
        print("\nSiin on nimekiri teie projektidest:\n")
        for row in data:
            if row["Projekt"] != "":
                emp.append(row["Projekt"])
            else:
                pass
    csvfile.close

    emp = list(set(emp))
    for e in emp:
        s = s + 1
        print(str(s) + ") " + e)

    print("\nMillist projekti soovite käsitleda?\n")
    kasutaja_valik_2 = input()
    sittpask = emp[int(kasutaja_valik_2) - 1]
    kasutaja_valik_2 = sittpask

    print("\nKuidas soovite käituda?")
    print("\n-" + sittpask + "-")    
    print("\nAva              - 1")
    print("Muuda nime       - 2")
    print("Kustuta          - 3")
    print("Tagasi           - 4\n")
    kasutaja_valik = input()    

    if kasutaja_valik == "1": #AVAB PROJEKTI
        print("\t-" + sittpask + "-\n")
        taskide_kuvar(kasutaja_valik_2)


    #(see sitt on katki ja ei tööta)
    if kasutaja_valik == "2": #MUUDAB PROJEKTI NIME
        pass
        """    
            with open('andmed.csv') as csvfile:
                fieldnames = ["Projekt" ,"Taski Nimi" ,"Taski sisu" ,"Prioriteet" ,"Staatus" ,"Tahtaeg" ]
                writer = csv.DictWriter(csvfile, fieldnames= fieldnames)
                reader = csv.DictReader(csvfile)
                sisend = input("Projekti uus nimi: ")
                for row in reader:
                    if row ["Projekt"] == kasutaja_valik_2:
                        writer.writerow("Projekt", sisend)
                    else:
                        pass
            """

    # Jällegi see funktsioon on mingi hindu kirjutatud ma tõesti proovisin ise Pana libraryga seda kustutamis asja
    # Tööle saada aga ma ei suutnud. See vähemalt töötab i guess ¯\_(ツ)_/¯
    if kasutaja_valik == "3": #KUSTUTAB SPETSIIFILISE PROJEKTI
        sisend = input("Kas oled kindel, et soovid projekti kustutada? ")
        if sisend == "yes" or "jah" or "y" or "Y":
            remove_specific_row_from_csv("andmed.csv", "Projekt", kasutaja_valik_2)
        print("Projekt " + str(kasutaja_valik_2) + " on kustutatud.")

if kasutaja_valik == "2": #AVAB TASKID
    taskide_kuvar("")

#if kasutaja_valik == "3":
    #print("kuidas soovite nimetada oma uut projekti?")

#if kasutaja_valik == "4":
    #print("Kuidas soovite nimetada oma uut taski?")
