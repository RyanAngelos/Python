
def get_info(code: str) -> str:

    kuupaevad = ''

    if len(code) == 11 and code.isdigit():
         
        and code[0] == "3":
        kuupaevad = ''.join(str(code[5:7]) + "-" + str(code[3:5]) + "-" + "19" + str(code[1:3]))
        
    elif len(code) == 11 and code.isdigit() and code[0] == "4":
        kuupaevad = ''.join(str(code[5:7]) + "-" + str(code[3:5]) + "-" + "19" + str(code[1:3]))
        
    elif len(code) == 11 and code.isdigit() and code[0] == "5":
        kuupaevad = ''.join(str(code[5:7]) + "-" + str(code[3:5]) + "-" + "20" + str(code[1:3]))
        
    elif len(code) == 11 and code.isdigit() and code[0] == "6":
        kuupaevad = ''.join(str(code[5:7]) + "-" + str(code[3:5]) + "-" + "20" + str(code[1:3]))
          
    elif len(code) != 11:
        return "\nIsikukoodi '" + code + "' pikkus ei ole õige!"
    
    elif code.isdigit() == False:
        return "\nIsikukoodis '" + code + "' võib olla ainult numbreid!"
    
    else:
        return "\nIsikukoodi '" + code + "' pikkus on vale ja võib olla ainult numbreid!"


    return kuupaevad 
    



    


if __name__ == '__main__':
    id_codes = [
        "43108224720",
        "4360812523",
        "32605022755",
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
