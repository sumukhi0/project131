import csv

datarow = []

with open ("data.csv") as f:
    read = csv.reader(f)
    print(read)
    for i in read:
        datarow.append(i)

headers = datarow[0]
planetdata = datarow[1:]
# print(headers)
headers[0] = "rowno"
solarsystemcount = {}

for i in planetdata:
    if solarsystemcount.get(i[11]):
        solarsystemcount[i[11]] += 1
    else:
        solarsystemcount[i[11]] = 1

maxsolarsystem = max(solarsystemcount, key = solarsystemcount.get)
print(maxsolarsystem, solarsystemcount[maxsolarsystem])

temp = list(planetdata)
for i in temp:
    planetmass = i[3]
    if planetmass.lower() == "unknown":
        planetdata.remove(i)
        continue
    else:
        planetmass_value = planetmass.split(" ")[0]
        planetmass_ref = planetmass.split(' ')[1]
        if planetmass_ref == "Jupiters":
            planetmass_value = float(planetmass_value)* 317.8
        planetdata[3] == planetmass_value
        