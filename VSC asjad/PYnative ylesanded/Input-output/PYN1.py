#Write a program to accept two numbers from the user and calculate multiplication
#võta kaks arvu ja korruta need

s1 = int(input("Siseta esimene arv: "))
s2= int(input("Siseta teine arv: "))

def korrutis(a,b):
    return "Kahe arvu korrutis on " + "".join(str(a * b))
    
print(korrutis(s1,s2))