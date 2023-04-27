import datetime
import math

def solution(fees, records):
    answer = {}
    recordsDict = {}
    
    for idx in range(len(records)):
        record = records.pop(0).split(' ')
        
        if record[2]=='IN':
            recordsDict[record[1]] = record
        else:
            inRecord = recordsDict.pop(record[1])
            parkingTime = timeCalculation(inRecord[0], record[0])
            
            if record[1] in answer:
                answer[record[1]] += parkingTime
            else:
                answer[record[1]] = parkingTime
            
    for carNo, record in recordsDict.items():
        if carNo in answer:
            answer[carNo] += timeCalculation(record[0], '23:59')
        else:
            answer[carNo] = timeCalculation(record[0], '23:59')
        
    result = []
    for key in sorted(answer):
        fee = fees[1]
        if answer[key] > fees[0]:
            fee = fees[1] + math.ceil((answer[key] - fees[0]) / fees[2]) * fees[3]
    
        result.append(fee)
    
    return result

def timeCalculation(inTime, outTime):
    dateFormat = '%H:%M'
    
    inTime = datetime.datetime.strptime(inTime, dateFormat)
    outTime = datetime.datetime.strptime(outTime, dateFormat)
    parkingTime = int((outTime - inTime).seconds / 60)
    
    return parkingTime