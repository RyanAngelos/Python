#Print downward Half-Pyramid Pattern with Star (asterisk)
#prindi tagurpidi poolpüramiid

rida = 5

a = 0
# reverse for loop from 5 to 0
for i in range(rida, 0, -1):
    a += 1
    for j in range(1, i + 1):
        print(a, end=" ")
    print("")