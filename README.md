## Description
Script to web scrape Learning Equality's Team Page and Core Values Page
* teamPage.py - scrapes Team Page and gather's members information. Creates a CSV in the current directory which includes name, title, and path to the member's image's image. Images are saved to a folder, **team_images**, which is created in the current directory. 
* coreValues.py - scrapes Core Values Page. Generates a HTML that recreates just the Core Values text with the necessary styling. Creates a folder in the current directory called **public** which stores all necessary files 

## Installation
Required modules for script:
```bash
  pip install csv
  pip install request
  pip install beautifulsoup4
```

## Installation
To run this script:
```bash
  python coreValues.py
  python teamPage.py
```