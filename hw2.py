def readDates(filename):
    dateList = []
    file = open(filename)
    for line in file:
        dateList.append(int(line.rstrip()))
    file.close()
    return dateList

#Given integer date returns
#the month as an integer
def getMonth(date):
    return (date//100)%100

#Given integer date returns
#the year as an integer
def getYear(date):
    return date//10000  

#Given integer date returns
#the day as an integer
def getDay(date):
    return date%100


def lastDay(date):
    lastDay = 31
    if(getMonth(date) == 2 and isLeap(getYear(date)) == True):
        lastDay = 29
    if(getMonth(date) == 2 and isLeap(getYear(date)) == False):
        lastDay = 28
    if(getMonth(date) == 4 or getMonth(date) == 6 or getMonth(date) == 9 
       or getMonth(date) == 11):
        lastDay = 30
    return lastDay


def isLeap(year):
    leap = False
    if((year % 400) == 0):
        leap = True
    elif((year % 100) == 0):
        leap = False
    elif((year % 4) == 0):
        leap = True
    return leap

 
def areValidDates(dateList):
    for date in dateList:
        if(not isValidDate(date)):
            return False

    for i in range(0, len(dateList)-1, 1):
        isValid = True
        if(((getYear(dateList[i])==getYear(dateList[i+1])) 
            and (getMonth(dateList[i]) == getMonth(dateList[i+1])) 
             and (getDay(dateList[i+1]) - getDay(dateList[i]) != 1))):
            return False
        if((getYear(dateList[i]) == getYear(dateList[i+1])) and (getMonth(dateList[i+1]) - getMonth(dateList[i]) == 1)
           and (getDay(dateList[i]) == lastDay(dateList[i])) and (getDay(dateList[i+1]) != 1)):
            return False
        if((getYear(dateList[i+1])-getYear(dateList[i]) == 1) and (getMonth(dateList[i]) == 12 and getMonth(dateList[i+1]) == 1) 
           and (getDay(dateList[i]) == 31 and getDay(dateList[i+1]) != 1)):
            return False
    return True

#function checks both that it is in range, and that the year is correct
def isInRange(date):
    return (date >= 17520914 and date <= 20180117)

def isValidMonth(date):
    month = getMonth(date)
    return (month >= 1 and month <= 12)


def isValidDay(date):
    
    year = getYear(date)
    month = getMonth(date)
    day = getDay(date)

    monthsWith31 = [1, 3, 5, 7, 8, 10, 12]
    monthsWith30 = [4, 6, 9, 11]
    
    if(month in monthsWith31):
        return(day >= 1 and day <=31)
    elif(month in monthsWith30):
        return(day >= 1 and day <=30)
    elif(month == 2 and isLeap(year)):
        return(day >=1 and day <=29)
    elif(month == 2 and not isLeap(year)):
        return(day >=1 and day <= 28)
    else:
        return False


def isValidDate(date):
    return (isInRange(date) and isValidMonth(date) and isValidDay(date))



def main():
    dates = readDates("dates.txt")
    print(areValidDates(dates))
    
    dates2 = readDates("dates2.txt")
    print(areValidDates(dates2))
    
    dates3 = readDates("dates3.txt")
    print(areValidDates(dates3))    
    
main()