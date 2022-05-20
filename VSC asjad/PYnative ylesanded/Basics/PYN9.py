#Write a program to check if the given number is a palindrome number.
#kontrolli kas number on palindroom

x = "12345"
y = "12321"

def convert(a):
    txt = a[::-1]
    return txt
x1 = (convert(x))
y1 = (convert(y))

if y == y1:
    print("True")
else:
    print("False")

if x == x1:
    print("True")
else:
    print("False")