from pyflix2 import *

netflix = NetflixAPIV2( 'appname', 'key', 'shared_secret')
movies = netflix.title_autocomplete('Terminator', filter='instant')
for title in movies['autocomplete']['title']:
    print(title)

user = netflix.get_user('use_id', 'access_token', 'access_token_secret')
reco = user.get_reccomendations()
for movie in reco['recommendations']:
    print(movie['title']['regular'])
