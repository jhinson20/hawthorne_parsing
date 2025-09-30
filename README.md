# hawthorne_parsing
The **hawthorne_parsing** application is designed to parse a tsv file with headers. The data will be parsed into two separate files: **nameAndDateByLine.csv** and **totalsByMonth.csv**.

## Requirements
* [Python](https://www.python.org/downloads/)
* Data file, named **lunchCount.tsv**, is in the same directory as the python file

## lunchCount.tsv
The application makes assumptions about the input data file, which must be named **lunchCount.tsv**. These assumpations are:
* The first line of the file consists only of headers, no data
* The first tsv value is dateTime values
* The second tsv value is date values in the form **m/d/yyyy**, for example **1/2/2025** is January 2nd, 2025
* The third tsv value is a string value
* The fourth tsv value is a string value, which consists of names separated by commas. Commas with no names between them will be ignored
* Name casing is ignored (i.e. john = John), but other than that name inputs should be consistent. Every name that is not input the same way will be considered unique (i.e. John Doe != John). For this reason it would be best to input full names everytime in **lunchCount.tsv**

## nameAndDateByLine.py
Outputs **nameAndDateByLine.csv**, which contains every instance of a person in the fourth column of **lunchCount.tsv** in alphabetical order. The output file is in the form [Name, Date].

## totalsByMonth.py
Outputs **totalsByMonth.csv**, which contains every unique name in alphabetical order followed by the number of times they appeared in a specific month. The output file is in the form [Name, Month/Year, Total].