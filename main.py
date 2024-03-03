import webbrowser as web
import requests

web.open("http://192.168.1.109:30038")


user_search = input("input you want to search at google search : ")
web.open("https://www.google.com/search?q=" + user_search)
'''web.open("http://192.168.1.109")'''

