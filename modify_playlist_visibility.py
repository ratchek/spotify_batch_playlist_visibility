import spotipy
from spotipy.oauth2 import SpotifyOAuth
import credentials

# TODO make_private and make_public are essentially the same and could be one
# funciont that takes a parameter

def make_private():
    no_of_modified_playlists = 0
    playlists = sp.current_user_playlists(limit=50)
    # It seems that the highest number to which you can set limit in the above code is 50
    # So this while loop cycles through all your playlists 50 at a time
    offset = 0
    while (len(playlists["items"]) > 0):
        for idx, item in enumerate(playlists['items']):
            sp.playlist_change_details(item['id'], public=False)
            print ("Changed playlist " + item['name'] + " to private")
            print()
            no_of_modified_playlists += 1        
            
        offset += 50
        playlists =  sp.current_user_playlists(limit=50, offset = offset)
    print(f'Changed {no_of_modified_playlists} to private')
    
def make_public():
    no_of_modified_playlists = 0
    playlists = sp.current_user_playlists(limit=50)
    # It seems that the highest number to which you can set limit in the above code is 50
    # So this while loop cycles through all your playlists 50 at a time
    offset = 0
    while (len(playlists["items"]) > 0):
        for idx, item in enumerate(playlists['items']):
            sp.playlist_change_details(item['id'], public=True)
            print ("Changed playlist " + item['name'] + " to public")
            print()
            no_of_modified_playlists += 1        

        offset += 50
        playlists =  sp.current_user_playlists(limit=50, offset = offset)
    print(f'Changed {no_of_modified_playlists} to public')

scope = "user-library-read playlist-modify-private playlist-modify-public playlist-read-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=credentials.client_id, client_secret= credentials.client_secret, redirect_uri=credentials.redirect_url, scope=scope))

make_private()

print("Done!")
