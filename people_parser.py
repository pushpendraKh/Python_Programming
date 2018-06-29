print('-------------- Problem 1: Read from a file and perform operations------------')
with open('people.csv') as file:
    lines = file.readlines()
print(lines)

def createDictionary(line):
    temp = line.strip().split(',')
    return { 'name': temp[0], 'email': temp[1], 'company': temp[2] }

outputList = map(createDictionary, lines)
print '\nList'
print outputList

kulizaList = filter(lambda record: record['company'].lower() == 'kuliza', outputList)
print '\nFiltered by Kuliza'
print kulizaList

abcdList = filter(lambda record: record['company'].lower() == 'abcd', outputList)
print '\nfiltered by abcd'
print abcdList

namesWithCompany = [ { 'name': record['name'], 'company': record['company'] } for record in outputList]
print '\nname and company'
print namesWithCompany

sortedRecord = sorted(outputList, key=lambda record: record['name'])
print '\nSorted Record'
print(sortedRecord)



# General SQL
# -> Select <-> map
# -> where <-> filter

