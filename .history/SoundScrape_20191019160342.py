from selenium import webdriver
import os
import bs4
import requests

top_url = ""
new_url = ""
mix_url = ""
artist_url = ""
song_url = ""

page = webdriver.Chrome('')
page.get("")

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
        "20%".join(name.split)