# Raian Lents


def isConvertibleToInt(value):


    try:
        int(value)

        return True
    except ValueError:
        
        return False

def isConvertibleToFloat(value):

    try:


        float(value)
        return True

    except ValueError:
        return False

def isConvertibleToBool(value):
    
    if value == "True" or value == "False":

        return True
    else:
        return False

    
   

def main():

    toCheck = input("Give me an input: ")

    if(isConvertibleToInt(toCheck)):

        print("Input can be converted to integer")

    elif (isConvertibleToFloat(toCheck)):

        print("Input can be converted to float")

    elif(isConvertibleToBool(toCheck)):

        print("Input can be converted to boolean")

    else:

        print("Input cannot be converted to anything")





main()
