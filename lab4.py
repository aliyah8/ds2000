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

def readFiles(filename):
    dateList = []
    file = open(filename)
    for line in filename:
        splitlist = []
        splitlist.append(int(line.split[0]))
        splitlist.append(int(line.split[1]))
        dateList.append(splitList)
    file.close()
    return dateList
        
    

def main():
    hYears = readFile("lab4temps.txt")
    print(listHotYears(hYears))


main()
    
