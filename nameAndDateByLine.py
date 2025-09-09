file = open('lunchCount.tsv','r')

#Read the header line since we don't need it for the data
file.readline()

outputDict = {}

#Words and symbols that I found appearing in the values for student names
filterPhrases = ['hot pockets', 'hot pocket', '-', 'lasagna', '/', ]

for line in file:
    dataList = line.split('\t')
    dateTime, date, teacher, studentCsv = dataList[0], dataList[1], dataList[2], dataList[3]

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

csvString = 'Name,Date\n'

for key in outputDict:
    dates = list(outputDict[key])
    dates.sort()
    
    for date in dates:
        csvString += f'{key},{date}\n'

with open('nameAndDateByLine.txt', 'w') as writeFile:
    writeFile.write(csvString)