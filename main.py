import json 

f = open('routes/yellow.json')
 
data = json.load(f)
 
answer = []

for each in data:
    answer.append(each["Hindi"].lower())


with open("sample.json", "w") as outfile:
    json.dump(answer, outfile)