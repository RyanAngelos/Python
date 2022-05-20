#Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
#arvuta astendajaga arv

def astend(base, exp):
    num = exp
    vaste = 1
    while num > 0:
        vaste = vaste * base
        num = num - 1
    return vaste

print(astend(5, 4))