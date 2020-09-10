# request to fetch data from url
import requests
# beautifulSoup to parse data received from requests
from bs4 import BeautifulSoup
# os to create new folder to store images
import os

def scrapeCoreValuesPage(htmlUrl, cssUrl, bootstrapUrl):
  # GET request for html data then parsing the data
  htmlResponse = requests.get(htmlUrl, timeout=10)
  htmlSoup = BeautifulSoup(htmlResponse.content, 'html.parser')
  # GET request for CSS file data then parsing the data
  cssResponse = requests.get(cssUrl, timeout=10)
  cssSoup = BeautifulSoup(cssResponse.content, 'html.parser')
  # GET request for bootstrap styling data then parsing the data
  bootstrapResponse = requests.get(bootstrapUrl, timeout=10)
  bootstrapSoup = BeautifulSoup(bootstrapResponse.content, 'html.parser')
  # Extracting only Core Values text
  coreValuesInfo = htmlSoup.find('div', {'id': 'about-body'})
  # Generating the HTML markup
  htmlMarkUp = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link href="./bootstrap.min.css" rel="stylesheet">
  <link rel = "stylesheet" href = "./styles.css">
</head>
<body>
  <div class = "container">
    <div class = "col-sm-3 hidden-xs side-nav">
    </div>
    {}
  </div>
</body>
</html>""".format(coreValuesInfo)
  # format the CSS and Bootstrap parsed data into strings
  cssMarkUp = '{}'.format(cssSoup)
  bootstrapMarkup = '{}'.format(bootstrapSoup)
  
  createMarkUp(htmlMarkUp, cssMarkUp, bootstrapMarkup)
  return

def createMarkUp(htmlMarkUp, cssMarkUp, bootstrapMarkup):
  # Create directory public to hold data files
  if not os.path.exists('public'):
    os.makedirs('public')
  # Get current working directory
  cwd = os.getcwd()
  # Create index.html in public and write to it
  writer = open('{}/public/index.html'.format(cwd), 'w')
  writer.write(htmlMarkUp)
  writer.close()
  # Create styles.css in public and write to it
  writer = open('{}/public/styles.css'.format(cwd), 'w')
  writer.write(cssMarkUp)
  writer.close()
  # Create bootstrap.min.css in public and write to it
  writer = open('{}/public/bootstrap.min.css'.format(cwd), 'w')
  writer.write(bootstrapMarkup)
  writer.close()
  return

scrapeCoreValuesPage('https://learningequality.org/about/values/', 'https://learningequality.org/static/css/styles.css', 'https://learningequality.org/static/bootstrap/css/bootstrap3.min.css')