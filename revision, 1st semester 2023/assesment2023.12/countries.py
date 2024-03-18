import json

jsonDataFile = "people-json.json"


def getCountries(filename):
    countries = []
    with open(filename,'r') as f:
        data = json.load(f)
    for person in data:
        countries.append(person.get("country"))

    return list(set(countries))



print(getCountries(jsonDataFile))
print(len(getCountries(jsonDataFile)))


def getVIPSPerCountry(filename):
    with open(filename,"r") as f:
        data = json.load(f)
    num_countries = {}
    for person in data:
        if person.get("vip"):
            if person.get("country") not in num_countries:
                num_countries.update({person.get("country"):1})
            else:
                num_countries.update({person.get("country"):(int(num_countries.get(person.get("country"))+1))})
        if person.get("country") not in num_countries and person.get("vip") == False:
            num_countries.update({person.get("country"):0})

    return num_countries

print(getVIPSPerCountry(jsonDataFile))
print(len(''))