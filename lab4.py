### Code from HW1 Solution
def getYear(date):
    return date // 10000

#Given integer date returns
#the month as an integer
def getMonth(date):
    return ((date // 100) % 100)

#Given integer date returns
#the day as an integer
def getDay(date):
    return date % 100

def readFile(filename):
    dateList = []
    file = open(filename)
    for line in file:
        splitlist = []
        l = line.split()
        splitlist.append(int(l[0]))
        splitlist.append(int(l[1]))
        dateList.append(splitlist)
    file.close()
    return dateList

def listHotYears(dateList):
    listYears=[]
    for i in dateList:
        if i[1]>=100:
            listYears.append(getYear(i[0]))
    listYears = set(listYears)
    listYears = list(listYears)
    return listYears
    

def main():
    hYears = readFile("lab4temps.txt")
    print(listHotYears(hYears))


main()
    
