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
    print(">>> 1 . Search for ")