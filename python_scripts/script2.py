import json
import re

l2004 = json.load(open('data\\2004.json'))
l2021 = json.load(open('data\\2021.json'))
c=0

min_year = 2024
genres2021 ={}
artist2021 ={}
years2021 = {}
for song in l2021:
    year =int(song[3])
    genre = (re.sub(r'\d{4}s?', '', song[5])).replace(" ", "")
    artist = song[2].lstrip().rstrip()
    
    if not year in years2021.keys():
        years2021[year] = 1
    else:
        years2021[year] += 1
    if not artist in artist2021.keys():
        artist2021[artist] = 1
    else:
        artist2021[artist] += 1
    if not genre in genres2021.keys():
        genres2021[genre] = 1
    else:
        genres2021[genre] += 1
    if(year<min_year):
        min_year = year
    if (len(song) < 6):
        c += 1
# print(c)
print("2021:")
# print(min_year)#min_year year
# print(genres2021)
val =sorted(years2021.items(),key = lambda x:x[0])
a=[]
for e in val:
    a.append(e[1])
print(a)
# print(json.dumps(sorted(artist2021.items(), key=lambda x:x[1])))

min_year = 2024
genres2004 ={}
artist2004 ={}
years2004 ={}
for song in l2004:
    year =int(song[5])
    genre = re.sub(r'\d{4}s?', '', song[6]).replace(" ", "")
    artist = song[1].lstrip().rstrip()
    
    if not artist in artist2004.keys():
        artist2004[artist]=1
    else:
        artist2004[artist] += 1
    if not genre in genres2004.keys():
        genres2004[genre] = 1
    else:
        genres2004[genre] += 1
    if not year in years2004.keys():
        years2004[year] = 1
    else:
        years2004[year] += 1
    if(year<min_year):
        min_year = year
    if (len(song) < 6):
        c += 1
# print(c)
print("2004:")
# print(min_year)#min_year year
# print(genres2004)
# print(json.dumps(sorted(artist2004.items(), key=lambda x:x[1])))
print(sorted(years2004.items(),key = lambda x:x[0]))
#dict(sorted(my_dict.items(), key=lambda x: x[1]))
