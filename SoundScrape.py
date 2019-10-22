from selenium import webdriver
import os
import bs4
import requests


top_url = "https://soundcloud.com/charts/top"
new_url = "https://soundcloud.com/charts/new"
mix_url = "&filter.duration=epic"
artist_url = "https://soundcloud.com/search/people?q="
song_url = "https://soundcloud.com/search/sounds?q="

page = webdriver.Chrome('/usr/local/bin/chromedriver')
page.get("https://soundcloud.com")

print()
print(">>> Welcome to the Python Soundcloud Scraper")
print(">>> Explore the Top / New & Hot Charts for all Genres")
print(">>> Search Soundcloud for Tracks, Artist, and Mixes")
print()

while True:
    print(">>> Menu: ")
    print(">>> 1 . Search for a song  ")
    print(">>> 2 . Search for an artist  ")
    print(">>> 3 . Search for a mix  ")
    print(">>> 4 . Top charts ")
    print(">>> 5 . Hot charts ")
    print(">>> 0 . EXIT  ")
    print()
    choice = int(input(">>> Your choice  "))
    if choice == 0:
        page.quit()
        break
    print()


    if choice == 1:
        name = input("Song name: ")
        print()
        "20%".join(name.split(" "))
        page.get(song_url + name)
        continue
    
    if choice == 2:
        name = input("Artist name: ")
        print()
        "20%".join(name.split(" "))
        page.get(artist_url + name)
        continue

    if choice == 3:
        name = input("Mix name: ")
        print()
        "20%".join(name.split(" "))
        page.get(song_url + name + mix_url)
        continue

    while True:
        print(">>> Generes:  ")
        print()

        url = ''
        if choice == 4:
            url = top_url
        else:
            url = new_url

        request = requests.get(url)
        soup = bs4.BeautifulSoup(request.text, "lxml")

        genres = soup.select("a[href*=genre]")[2:]

        genre_link = []

        for index, genre in enumerate(genres):
            print(str(index) + ": " + genre.text)
            genre_link.append(genre.get("href"))

        print()
        choice = input(">>> Your choice (x to re-select chart type):")
        print()

        if choice == 'x':
            break
        else:
            choice = int(choice)

        url = "http://soundcloud.com" + genre_link[choice]
        request = requests.get(url)
        soup = bs4.BeautifulSoup(request.text, "lxml")

        songs = soup.select("h2")[3:]
        song_links = []
        song_names = []

        for index, track in enumerate(tracks):
            track_links.append(track.a.get("href"))
            track_names.append(track.text)
            print(str(index+1) + ": " + track.text)
            print()

        while True:
            choice == input(">>> Your choice (x to re-select genre): ")
            print()

            if choice == 'x':
                break
            else:
                choice = int(choice)-1

            print("Playing: " + song_names[choice])
            print()

            page.get("http://soundcloud.com" + song_links[choice])

print()
print("Bye!")
print()
