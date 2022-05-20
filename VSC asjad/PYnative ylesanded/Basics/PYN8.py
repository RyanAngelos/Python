#Print the following pattern:
#prindi püramiid

#1 
#2 2 
#3 3 3 
#4 4 4 4 
#5 5 5 5 5

rida = 5
for e in range(rida+1):
    for a in range(e):
        print (e,end=" ")
    print("")