#Iterate the given list of numbers and print only those numbers which are divisible by 5
#prindi listist 5ga jagatavad arvud

x = [10, 20, 33, 46, 55]

def check(a):
    for e in a:
        if e%5==0:
            print(e)

print(check(x))
