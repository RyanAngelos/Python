#Write a program to accept a string from the user and display characters that are present at an even index number.
#loo list inputi igast teisest tähemärgist


def kaunt(sisend):

    nimekiri = list(sisend)

    for e in nimekiri[0::2]:
        print(e)

kaunt(input())