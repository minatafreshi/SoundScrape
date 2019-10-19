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

    choice == int(input(">>> Your choice  "))
    