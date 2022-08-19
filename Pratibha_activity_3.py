import requests
import json
import pandas as pd

def create_character_df(API_key, Hash, nameStartsWith):
    all_characters_list = []
    time_stamp = '1'
    BASE_url = "http://gateway.marvel.com/v1/public/characters?"
    url = BASE_url + "ts=" + time_stamp + "&apikey=" + API_key + "&hash=" + Hash
    parameters = {'nameStartsWith': nameStartsWith, 'limit': 100}
    response = requests.get(url, params=parameters).json()
    requests.get(url, params=parameters).raise_for_status()

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

    return pd.DataFrame(all_characters_list, columns = ['character_name', 'num_events_appearences', 'num_series_appearences', 'num_stories_appearences', 'num_comics_appearences', 'character_id'])


#Sample function call 
print(create_character_df(API_key = "Your API Key", Hash = "Your hash code", nameStartsWith="z"))