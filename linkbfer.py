#Importing:
from bs4 import BeautifulSoup
import requests

#Color codes and other variables:
color1 = "\033[32m"
color2 = "\033[36m"
color3 = "\033[31m"

#Inrtoduction
print(color3 + "Website Link bruteforcer:")
print(color2 + "This tool will require a custom wordlist, place it where this file is placed(same folder), with the name 'wordlist.txt' and each test keywords should be seperated without any spaces with commas. Avoid using any quotations for the keywords themselves, like 'keyword A' for seperation. You can however use them in between.")
#S1
print(color2 + "Result details: Responses with a code starting with 2 are success. Responses with a code starting with 4 are errors." + color1)

#Wordlist opener and converter:
wl = open("wordlist.txt","r")
wlprint = wl.read()
teststring = wlprint

#String into list for the 'worldlist.txt' + The comma/',' splitter:
input = input(str("Paste/Type your website home/main page URL with 'http(s)' and ending with a '/' to scan: "))
mod = teststring.split(",")
print("List you will use: ")

#Main run and loop for wordlist tester:
print(color3)	
print(mod)
m1 = ""
n = 0
for s in mod:
	consec = mod[n]
	m1 = input + consec
	print("Trying:" + m1)
	n = n + 1
	page = requests.get(m1)
	print(page)