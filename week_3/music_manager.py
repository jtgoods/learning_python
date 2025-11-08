#this program manages a music playlist, adds songs, removes songs, and gives the user average song length and playlist length
#initial data
playlist = [
    {"title": "seven", "artist": "Taylor Swift", "duration": 3.47, "genre": "pop"},
    {"title": "WYM Freestyle", "artist": "Doja Cat", "duration": 2.05, "genre": "hip hop"},
    {"title": "So We Won't Forget", "artist": "Khruangbin", "duration": 4.95, "genre": "psychedelic rock"}
]

#function to add a song to the end of the playlist
def add_song(playlist, title, artist, duration, genre):
    if type(duration) == float: #validation checking for duration as a float
        song = {"title": title, "artist": artist, "duration": duration, "genre": genre}
        playlist.append(song)
    else:
        return
print(add_song(playlist, "Jeannie Becomes A Mom", "Caroline Rose", 4.33, "Art Pop"))

#function to remove a song by searching by title
def remove_song(playlist, title):
    for index, song in enumerate(playlist):
        if song["title"] == title: #searches for title in each dictionary within playlist
            playlist.pop(index) 
            print(f"deleted {title}")
            return
    print("not found")
remove_song(playlist, "hello")

#function to sort the playlist
def sorted_by(playlist, key_name, reverse=False):
    new = sorted(playlist, key=lambda song: song[key_name], reverse=reverse)
    return new
print(sorted_by(playlist, "duration"))

#function for average song duration & playlist length
def average_duration(playlist):
    total = 0
    for song in playlist:
        total += song["duration"]
    print("playlist length:", len(playlist))
    return total/len(playlist)
print(average_duration(playlist))
