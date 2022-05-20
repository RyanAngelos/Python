"""
Printida välja info iga isikukoodi kohta.
Kui isikukood ei ole korras:
    Kui pikkus on paigast ära: tagasta "Pikkus ei ole õige!"
    Kui isikukoodis muid asju kui numbrid: tagasta "Isikukoodis võib olla ainult numbreid!"
    Kui kuupäeva ei eksisteeri näiteks on märgitud 35 päev või 14. kuu või 29 veebruar 2019: tagasta "Isikukoodi kuupäev ei ole korrektne!"
Kui isikukood on korras:
    Tagasta kuupäev stringina sellises formaadis: dd-mm-yyyy
                                               nt 03-05-1999

"""

def get_info(code: str) -> str:
    
    kuupaevad = ""
    
#kontrollib kas tegemist on numbritega
    def isdig(a):
        if code.isdigit():
            a == True
        else: print ("\nIsikukoodis '" + code + "' võib olla ainult numbreid!")

#kontrollib kas pikkus on 11
    def pikkus(a):
        if len(code) == 11:
            a == True
        else: print("\nIsikukoodi '" + code + "' pikkus ei ole õige!")

    pikkus_err = "Sellist kuupäeva pole olemas! "

#kontrollivad kas kuupäev on olemas
    def kuupaev31(a):
        a31 = (str(code[5:6]))
        if a31 == ("01" or "03" or "05" or "07" or "08" or "10" or "12") and a31 <= 31:
            a == True
        else: print(pikkus_err)

    def kuupaev30(a):
        a30 = (str(code[5:6]))
        if a30 == ("04" or "06" or "09" or "11") and a30 <= 30:
            a == True
        else: print(pikkus_err)

    def kuupaev_veeb(a):
        a28 = (str(code[5:6]))
        if a28 == "02" and a28 <= 28:
            a == True
        else: print(pikkus_err)

    
#kontrollivad aastaarvu
    if code[0] == "3" or "4" and (isdig() and pikkus()) == True:
        kuupaevad = ''.join(str(code[5:7]) + "-" + str(code[3:5]) + "-" + "19" + str(code[1:3]))
        return kuupaevad

    elif code[0] == "5" or "6" and (isdig() and pikkus()) == True:
        kuupaevad = ''.join(str(code[5:7]) + "-" + str(code[3:5]) + "-" + "20" + str(code[1:3]))
        return kuupaevad

    """
    if isdig() == False:
        return "\nIsikukoodis '" + code + "' võib olla ainult numbreid!"

    elif pikkus() == False:
        return "\nIsikukoodi '" + code + "' pikkus ei ole õige!"
    """
    
if __name__ == '__main__':
    id_codes = [
        "43108224720",
        "4360812523",
        "32605022755",
        "61106064780",
        "4720807276a",
        "42605150146",
        "382050247",
        "42404123759",
        "45905232713442d",
        "39412304990",
        "389092049622"
    ]

    for id_code in id_codes:    
        print(get_info(id_code))