#!/usr/bin/python3
import os
import requests
from bs4 import BeautifulSoup

# Currently just takes terminal user input,
# could easily be changed to take sys args
shortcode = str(input("Please enter the problem list shortcode: "))

count = 1

# Generate the base URL
URL = 'http://aimpl.org/' + shortcode + '/'

# create a requests object
response = requests.get(URL)

# create a bs4 object.. important for well formated output html
soup = BeautifulSoup(response.content, 'html5lib')

# create the initial directory and index.html file 
# if the webpage exists. Won't work if the directory already exists
if response.status_code == 200:
  try:
    os.mkdir(shortcode)
    # with handles open / close for us
    with open(shortcode + "/index.html", 'w') as file:
      file.write(str(soup))
  except OSError as error:
    print (error)

# update the requests object to the first section 
# We're assuming there is always at least 1
response = requests.get(URL + str(count))

# Will return status_code 400 if webpage doesn't exist
while response.status_code == 200:
  print (URL + str(count) + ' is a webpage')
  soup = BeautifulSoup(response.content, 'html5lib') # update soup object
  with open(shortcode + "/section" + str(count) +".html", 'w') as file:
    file.write(str(soup))
  count = count + 1
  response = requests.get(URL + str(count))