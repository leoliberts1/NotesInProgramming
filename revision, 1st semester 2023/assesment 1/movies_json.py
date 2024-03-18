

import json

jsonDataFile = "movies-2020s.json"


def getYears(filename):
    with open(filename) as f:
        data = json.load(f)
    years =[]
    for film in data:
        year = str(film.get("year"))
        if year not in years:
            years.append(year)
    return(years)


print(getYears(jsonDataFile))


def getGenres(filename):
    with open(filename) as f:
        data = json.load(f)
    genres = set()
    for movie in data:
        for genre in movie.get("genres"):
            genres.add(genre)
    return genres


print((getGenres(jsonDataFile)))
def getCountsPerYear (genre, filename):
    with open(filename) as f:
        data = json.load(f)
    num_genres = {}
    for movie in data :
        if genre in movie.get("genres"):
            if genre not in num_genres:
                num_genres.update({genre:1})
            num_genres.update({genre:num_genres.get(genre)+1})
    return num_genres
print(getCountsPerYear('Legal',jsonDataFile))