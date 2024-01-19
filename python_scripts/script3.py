import json


l2004 = json.load(open('data\\2004.json'))
l2021 = json.load(open('data\\2021.json'))


# CROSS INFO BETWEEN LIST
for song in l2004:
    match=False
    title2004 = song[2]
    for song2 in l2021:
        title2021 = song2[1]
        if(''.join(title2021.split()).lower() == ''.join(title2004.split()).lower()):
            match=True
            song[6]=song2[5]
    print(json.dumps(song) + ",")
    
