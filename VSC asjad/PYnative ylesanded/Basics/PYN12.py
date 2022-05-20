#Calculate income tax for the given income by adhering to the below rules:
#arvuta maksuvaba tulu

#First $10,000	0
#Next $10,000	10
#The remaining	20

tulu = 45000

def maksuvaba(a):
    x = a - (10000 / 100 * 0) - (10000 / 100 * 10) - (25000 / 100 * 20)
    y = a - x
    return y

print(maksuvaba(tulu))