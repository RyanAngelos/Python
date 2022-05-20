#Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
#korruta 1 kuni 10 igat arvu eelneva arvuga

    #read 7;8;9 on valikulised, väldivad negatiivse arvu printimist

for e in list(range(0, 10)):
    if (e - 1 < 1) and e == 0:
        print (0)
    else:
        print (e + (e - 1))