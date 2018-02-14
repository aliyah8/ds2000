# Aliya Tyshkanbayeva
# homework 4
import math

# function that reads the file and creats a dictionary
# it stores data in the dictionary and adds values to years based on
# if there is a shadow or no
def readGround(fileName):
    shadowTable = {}
    file = open(fileName)
    for line in file:
        l = line.split()        
        if(l[1]=="Full" and (int(l[0]) >= 1936)):
            shadowTable[int(l[0])] = True
        if(l[1]=="No" and l[2]=="Shadow" and (int(l[0]) >= 1936)):
            shadowTable[int(l[0])] = False
    file.close()
    print(shadowTable)
    return shadowTable

# function that reads the file and creats the list
def readSpring(filename):
    springList = []
    file = open(filename)
    for line in file:
        springList.append(int(line.rstrip()))
    file.close()
    return springList    

# function to calculate Phi Coefficient, that takes in two arguments
# springList and shadowTable
def calculatePhi(springList, shadowTable):
    c1=0
    c2=0
    i1=0
    i2=0
    for k in shadowTable:
        if k in springList and shadowTable[k] == True:
            i1 += 1
        if k not in springList and shadowTable[k] == True:
            c1 += 1
        if k in springList and shadowTable[k] == False:
            c2 += 1
        if k not in springList and shadowTable[k] == False:
            i2 +=1
    x = math.sqrt(c1*c2*i1*i2)
    return (c1*c2 - i1*i2)/x

def main():
    
    groundHogYears = readGround("groundhog.txt")
    dates = readSpring("springyears.txt")   
    print(dates)
    print(calculatePhi(dates, groundHogYears))

main()

    
            
