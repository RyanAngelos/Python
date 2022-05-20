#Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.
#Kui esimene ja viimane number listis on samad, tagasta TRUE else FALSE

def check(a):

    esimene = a[0]
    viimane = a[-1]
    if esimene == viimane:
        return True
    else:
        return False

x = [10, 20, 30, 40, 10]
y = [75, 65, 35, 75, 30]

print(check(x))
print(check(y))