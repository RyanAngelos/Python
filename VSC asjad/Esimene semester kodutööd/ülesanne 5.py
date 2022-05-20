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
#kontrollib kas tegemist on numbritega
def isdig(code):
    if code.isdigit():
        return True
    else:
        return False

#kontrollib kas pikkus on 11
def pikkus(code):
    if len(code) == 11:
        return True
    else:
        return False

#kontrollivad kas kuupäev on olemas

pikkus_err = "\nSellist kuupäeva pole olemas! "

def kuupaev30(code):
    a30 = (str(code[3:5]))
    if (a30 == "04" or "06" or "09" or "11") and  (int(code[5:7]) <= 30):
        return True
    else:
        return False

def kuupaev31(code):
    a31 = (str(code[3:5]))
    if (a31 == "01" or "03" or "05" or "07" or "08" or "10" or "12") and (int(code[5:7]) <= 31):
        return True
    else:
        return False

def kuupaev_veeb(code):
    a28 = (str(code[3:5]))
    
    if (a28 == "02") and (int(code[5:7]) <= 29):
        return True

    elif (a28 == "02") and (int(code[5:7]) <= 28):
        return True
    else:
        return False


#---------------------------------------------------------
#---------------------------------------------------------
#---------------------------------------------------------
 

def get_info(code: str) -> str:
    
    kuupaevad = ""

#kontrollib kas tegemist on numbritega   
    if not isdig(code):
        return "\nIsikukoodis '" + code + "' võib olla ainult numbreid!\n"

#kontrollib kas pikkus on 11
    elif not pikkus(code):
        return "\nIsikukoodi '" + code + "' pikkus ei ole õige!\n"
    
#kontrollib kas kuupäev on olemas
    elif not kuupaev30(code):
        return pikkus_err
    elif not kuupaev31(code):
        return pikkus_err
    elif ((int(code[1:3])) % 4 == 0) and (kuupaev_veeb(code)):
        return pikkus_err
    
#kontrollivad aastaarvu
    elif code[0] == "3" or "4":
        kuupaevad = ''.join(str(code[5:7]) + "-" + str(code[3:5]) + "-" + "19" + str(code[1:3]))
        return kuupaevad

    elif code[0] == "5" or "6":
        kuupaevad = ''.join(str(code[5:7]) + "-" + str(code[3:5]) + "-" + "20" + str(code[1:3]))
        return kuupaevad


#---------------------------------------------------------
#---------------------------------------------------------
#---------------------------------------------------------


if __name__ == '__main__':
    id_codes = [
        "43109224720",
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