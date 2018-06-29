with open('./problem.csv') as file:
    lines = file.readlines()
print(lines)

def createDictionary(line):
    temp = line.strip().split(',')
    return { 'child': temp[0], 'value': temp[1], 'parent': temp[2] }

outputList = map(createDictionary, lines)
print '\nList'
print outputList

childWithValueZero = filter(lambda record: record['value'] == '0', outputList)
print '\nFiltered by Value 0'
print childWithValueZero

childWithValueZeroParent = map(lambda record: record['parent'] ,childWithValueZero)
print '\nchildWithValueZeroParent'
print childWithValueZeroParent

childWithValueZeroParentRecord = map(lambda parentValue: filter(lambda record: { record['child'] == parentValue }, outputList) ,childWithValueZeroParent)

print '\nchildWithValueZeroParentRecord'
print childWithValueZeroParentRecord

#childWithValueZeroParentRecord = (map(lambda record1: filter(lambda record: record['child'] == record1,outputList) ,childWithValueZeroParent))
#print '\nchildWithValueZeroParentRecord'
#print childWithValueZeroParentRecord


#abcdList = filter(lambda record: record['company'].lower() == 'abcd', outputList)
#print '\nfiltered by abcd'
#print abcdList
#
#namesWithCompany = [ { 'name': record['name'], 'company': record['company'] } for record in outputList]
#print '\nname and company'
#print namesWithCompany
#
#sortedRecord = sorted(outputList, key=lambda record: record['name'])
#print '\nSorted Record'
#print(sortedRecord)
