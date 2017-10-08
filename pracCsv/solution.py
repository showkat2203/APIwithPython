import csv
import json

row_count = -1
result = ""

fileName = 'test.csv'
fields = ""

with open(fileName, 'r') as inputFile:
    csvReader = csv.reader(inputFile)
    fields = next(csvReader)

    resList = []
    for row in csvReader:
        cnt = 0
        resDict = {}
        for i in row:
            if fields[cnt] == 'id':
                i = int(i)
            elif fields[cnt] == 'isStudent':
                i = bool(int(i))
            doubleQuKey = "{0}".format(fields[cnt])
            resDict.update({str(doubleQuKey): i})
            cnt += 1
        # print(dict)
        resList.append(resDict)
        numberOfData = csvReader.line_num

# print(fields)

ansDic = {"number_of_data": numberOfData - 1, "file_name": fileName}

ansDic.update({"data": resList})

# print(resList)
# print("\n\n")
ansDic = json.dumps(ansDic)

print(ansDic)