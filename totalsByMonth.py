from datetime import datetime

def printTotalsByMonth(dict):
    csvString = 'Name,Month,Total\n'

    for key in dict:
        monthTotals = {}
        for date in dict[key]:
            month, year = date.month, date.year
            monthYear = f'{month}/{year}'

            if monthYear in monthTotals:
                monthTotals[monthYear] += 1
            else:
                monthTotals[monthYear] = 1

        monthTotals = {key: monthTotals[key] for key in sorted(monthTotals)}

        for monthYearKey in monthTotals:
            csvString += f'{key},{monthYearKey},{monthTotals[monthYearKey]}\n'


    with open('totalsByMonth.csv', 'w') as writeFile:
        writeFile.write(csvString)

file = open('lunchCount.tsv','r')

#Read the header line since we don't need it for the data
file.readline()

outputDict = {}

#Words and symbols that I found appearing in the values for student names
filterPhrases = ['hot pockets', 'hot pocket', '-', 'lasagna', '/', '(', ')' ]

for line in file:
    dataList = line.split('\t')
    dateTime, date, teacher, studentCsv = dataList[0], datetime.strptime(dataList[1], "%m/%d/%Y").date(), dataList[2], dataList[3]

    #Remove '"' and split on ','
    studentList = studentCsv.replace('\"','').split(',')

    #Remove occurences of filterPhrases from names
    for i in range(len(studentList)):
        for phrase in filterPhrases:
            studentList[i] = studentList[i].lower().replace(phrase, '')

    #Remove whitespace from both ends of the name string and remove blank entries
    studentList = [x.strip() for x in studentList if x.strip() != '']

    #Remove any entries that do not contain at least 1 letter
    studentList = [x for x in studentList if any(c.isalpha() for c in x)]

    for student in studentList:
        if student in outputDict:
            outputDict[student].append(date)
        else:
            outputDict[student] = [date]

file.close()

#Sort outputDict alphabetically by the key, which is the name
outputDict = {key: outputDict[key] for key in sorted(outputDict)}

printTotalsByMonth(outputDict)