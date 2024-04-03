#Question 3
#Task 1

artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]
unique_artists = set(artist_names)
print(f"The lineup for the festival is: {unique_artists}")

#Task 2
artists_genres = {
    "The Lumineers": "Folk",
    "Tame Impala": "Psychedelic Rock",
    "Billie Eilish": "Pop",
    "Arctic Monkeys": "Indie Rock"
}
genres_artists= set()

for artists, genre in artists_genres.items():
    if genre not in genres_artists:
        genres_artists.add((genre, artists))
    
print(genres_artists)

#Task 3

playlist1 = {"Song A", "Song B", "Song C"}
playlist2 = {"Song D", "Song E", "Song F"}
playlist3 = {"Song A", "Song B", "Song C"}

playlists = [playlist1, playlist2, playlist3]

if playlists[0]== playlists[1] or playlists[2]:
    print("Duplicate playlist found")
elif playlists[1]== playlists[2]:
    print("Duplicate playlist found")
else: 
    print("Duplicate was not found.")





