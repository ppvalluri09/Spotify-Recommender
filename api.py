import requests

def get_song_data(song_id, api):
    API_ENDPOINT = f'https://api.spotify.com/v1/audio-features/{song_id}'
    headers = {'Accept': 'application/json',
                   'Content-Type': 'appication/json',
                   'Authorization': f'Bearer {api}'}
    resp = requests.get(API_ENDPOINT, headers=headers).json()
    return {'danceability': resp['danceability'],
            'energy': resp['energy'],
            'key': resp['key'],
            'loudness': resp['loudness'],
            'speechiness': resp['speechiness'],
            'acousticness': resp['acousticness'],
            'instrumentalness': resp['instrumentalness'],
            'liveness': resp['liveness'],
            'valence': resp['valence'],
            'tempo': resp['tempo']}

def get_data(api):
    try:
        API_ENDPOINT = 'https://api.spotify.com/v1/me/tracks?market=ES&limit=50&offset=1'
        headers = {'Accept': 'application/json',
                   'Content-Type': 'appication/json',
                   'Authorization': f'Bearer {api}'}
        resp = requests.get(API_ENDPOINT, headers=headers).json()
        data = []
        for item in resp['items']:
            entries = item['track']
            artist_name = []
            artist_id = []
            for artist in entries['artists']:
                artist_name.append(artist['name'])
                artist_id.append(artist['id'])
            meta = {'name': entries['name'] ,
                    'song_id': entries['id'],
                    'artist': artist_name,
                    'artist_id': artist_id}
            data.append(meta)
        response = []
        for ele in data:
            each_data = get_song_data(ele['song_id'], api)
            song_data = {'name': ele['name'],
                         'artist': ele['artist']}
            for key in each_data.keys():
                song_data[key] = each_data[key]
            response.append(song_data)
        return response
    except Exception as e:
        return str(e)
