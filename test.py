#This program will print every name of a person that eats in alphabetical order along with the date on a line
#The name and date will be separated by a ','. There will be a line for everytime someone eats
from datetime import datetime

def printMealsByLine(dict):
    csvString = 'Name,Date\n'

    for key in dict:
        for date in dict[key]:
            csvString += f'{key},{date}\n'

    with open('nameAndDateByLine.csv', 'w') as writeFile:
        writeFile.write(csvString)

def printTotalsByMonth(dict):
    csvString = 'Name,Month,Total\n'

    for key in dict:
        month, year = dict[key][0].month, dict[key][0].year
        monthTotal = 0
        for date in dict[key]:
            if date.month == month:
                monthTotal += 1
            else:
                csvString += f'{key},{month}/{year},{monthTotal}\n'
                monthTotal, month, year = 1, date.month, date.year
        if monthTotal != 0:
            csvString += f'{key},{month}/{date.year},{monthTotal}\n'


    with open('totalsByMonth.csv', 'w') as writeFile:
        writeFile.write(csvString)

file = open('lunch count 2025.txt','r')

#Read the header line since we don't need it for the data
file.readline()

outputDict = {}

#Words and symbols that I found appearing in the values for student names
filterPhrases = ['hot pockets', 'hot pocket', '-', 'lasagna', '/', ]

for line in file:
    dataList = line.split('\t')
    dateTime, date, teacher, studentCsv = dataList[0], datetime.strptime(dataList[1], "%m/%d/%y").date(), dataList[2], dataList[3]

    #Remove '"' and split on ','
    studentList = studentCsv.replace('\"','').split(',')

    #Remove occurences of filterPhrases from names
    for i in range(len(studentList)):
        for phrase in filterPhrases:
            studentList[i] = studentList[i].lower().replace(phrase, '')

    #Remove whitespace from both ends of the name string
    studentList = [x.strip() for x in studentList if x != '']

    for student in studentList:
        if student in outputDict:
            outputDict[student].append(date)
        else:
            outputDict[student] = [date]

file.close()

#Sort outputDict alphabetically by the key, which is the name
outputDict = {key: outputDict[key] for key in sorted(outputDict)}
printMealsByLine(outputDict)
printTotalsByMonth(outputDict)