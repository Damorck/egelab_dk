import requests
import json
import datetime

dagsDato = datetime.date.today()
newConstructedUrl = 'http://hydrometri.azurewebsites.net/api/hyd/getplotdata?tsid=2140&enddate=' + str(dagsDato) + 'T16:00:00.000Z&days=8&pw=267'
# vandstand urf

url = newConstructedUrl
response = requests.get(url)
theContent = response.content
decodeIt = theContent.decode("UTF-8")
parsed_json = json.loads(decodeIt)
levelDown = (parsed_json['PlotRecs'])
byAll = levelDown[0:]


def dayRecord(byItem):
    byVs = dict(byItem[0])
    #date = byVs['dt']
    level = byVs['V'][0]
    #nameAndData = 'Date and name:  ' + str(date) + ' ' + str(level)
    vandstand = round((level * 10), 2)
    return(vandstand)



#(dayRecord(byItem=byAll[25:26]))
day1 = dayRecord(byItem=byAll[25:26])
day2 = dayRecord(byItem=byAll[63:64])
day3 = dayRecord(byItem=byAll[101:102])
day4 = dayRecord(byItem=byAll[139:140])
day5 = dayRecord(byItem=byAll[193:194])
day6 = dayRecord(byItem=byAll[231:232])
day7 = dayRecord(byItem=byAll[253:254])

byItem = byAll[10:11]

def Dato(byItem):
    byVs = dict(byItem[0])
    date = byVs['dt']
    #level = byVs['V'][0]
    #output = round((level * 10), 2)
    return(date[0:10])


#skal omskrives så det passer til dato
vandstand1 = Dato(byItem=byAll[25:26])
vandstand2 = Dato(byItem=byAll[63:64])
vandstand3 = Dato(byItem=byAll[101:102])
vandstand4 = Dato(byItem=byAll[139:140])
vandstand5 = Dato(byItem=byAll[193:194])
vandstand6 = Dato(byItem=byAll[231:232])
vandstand7 = Dato(byItem=byAll[253:254])