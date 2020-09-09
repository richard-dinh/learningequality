# csv to write to csv
import csv
# request to fetch data from url
import requests
# beautifulSoup to parse data received from requests
from bs4 import BeautifulSoup
# os to create new folder to store images
import os
# save images to folder

def scrapeTeamPage(url):
  response = requests.get(url, timeout=10)
  soup = BeautifulSoup(response.content, 'html.parser')
  # find all div with class visibile-sm
  visibleSmDiv = soup.find('div', {"class": "visible-sm"})
  names = []
  titles = []
  images = []
  # get all team member names and strip all the whitespace
  for visibleH3 in visibleSmDiv.findAll('h3'):
    names.append(visibleH3.get_text(strip=True))

  for visibleH4 in visibleSmDiv.findAll('h4'):
    titles.append(visibleH4.get_text(strip=True))

  # extracting image src and appending into images arr
  for visibleImg in visibleSmDiv.findAll('img'):
    images.append('https://learningequality.org'+visibleImg['src'])

  print(images)
  print(names)
  print(titles)
  print('Images length: ', len(images))
  print('Names length: ', len(names))
  print('Titles length: ', len(titles))
  writeToCSV(names, titles, images)
  return

def writeToCSV(names, titles, images):
  f = open('teamPage.csv', 'w')
  headers = 'Name, Title, Image\n'
  f.write(headers)
  # get current working directory
  cwd = os.getcwd()
  print(cwd)
  # create folder to store folders
  if not os.path.exists('team_images'):
    os.makedirs('team_images')

  for index in range(len(names)):
    # removing all whitespace
    imgName = names[index].replace(' ', '') + '.png'
    # saving image to cwd/team_images
    imageResponse = requests.get(images[index])
    # open and save to team_images foler
    writer = open('{}\\team_images\\{}'.format(cwd, imgName), 'wb')
    writer.write(imageResponse.content)
    writer.close()
    strInsert = '{}, {}, {}\n'.format(names[index], titles[index], '.\\team_images\\{}'.format(imgName))
    f.write(strInsert)
  
  f.close()
  return

scrapeTeamPage('https://learningequality.org/about/team/')
