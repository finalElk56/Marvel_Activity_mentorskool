import hashlib
import requests
import json
import pandas as pd


BASE_url = "http://gateway.marvel.com/v1/public/characters?"
API_key = "Your API Key"
time_stamp = "1"
Hash = "Your hash code"

#Creating a list of alphabets and digits with which the names of marvel characters can start
starts_with_char = list(range(ord('a'),ord('z')+1)) + list(range(ord('1'),ord('9')+1)) 

#Creating List of all individual characters info sublists
all_characters_list = []
for i in starts_with_char: 
    char = chr(i)
    #Request call url
    url = BASE_url + "ts=" + time_stamp + "&apikey=" + API_key + "&hash=" + Hash
    k = 0
    #Creating a dictionary of parameters to pass in the API call url
    parameters = {'nameStartsWith': char, 'limit': 100, 'offset' : k}
    response = requests.get(url, params=parameters).json()
    requests.get(url, params=parameters).raise_for_status()
    #Creating a list for storing the info of individual characters
    individual_character_info = []
    for j in range(len(response['data']['results'])):
        character_name = response['data']['results'][j]['name']
        num_events_appearences = response['data']['results'][j]['events']['available']
        num_series_appearences = response['data']['results'][j]['series']['available']
        num_stories_appearences = response['data']['results'][j]['stories']['available']
        num_comics_appearences = response['data']['results'][j]['comics']['available']
        character_id = response['data']['results'][j]['id']

        individual_character_info = [character_name, num_events_appearences, num_series_appearences, num_stories_appearences, num_comics_appearences, character_id]
        all_characters_list.append(individual_character_info)

    k+=100

df = pd.DataFrame(all_characters_list, columns = ['character_name', 'num_events_appearences', 'num_series_appearences', 'num_stories_appearences', 'num_comics_appearences', 'character_id']) 

print(len(df))
print(df.head())
