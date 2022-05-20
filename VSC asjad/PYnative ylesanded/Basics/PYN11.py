# Write a Program to extract each digit from an integer in the reverse order.
#keera integer tagurpidi tühikutega stringiks

int1 = 7536
int1str = str(int1)

def flip(a):
    b = a[::-1]
    return (" ".join(b))

print(flip(int1str))