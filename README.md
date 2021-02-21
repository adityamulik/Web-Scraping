# Web-Scraping using BeautifulSoup

Using Python's most coveted modules used for Web Scraping, this code is intended to scrape the available stock information and price of the Apple iPhone 11 on amazon.com which can be run using cron on linux or windows task scheduler to get the information at regular intervals on email.
**Programming Language:**

Python Version 3.8.1 

**Dependencies:**

* Git CLI / Bash
* Python Virtualenv wrapper or venv

**Libraries/Modules:**

* requests (To make HTTP Requests to fetch data)
* BeautifulSoup (To extract/scrape data from websites)
* smtplib (To make a connection string to send emails)
* json (To parse secrets config file to store credentials)
* time 

**Setup:**

  1. Clone the repository to your local environment using git. 
  2. Create a virual environment using Python's virtualenv or venv modules.\
     e.g. python -m pip venv venv
  3. Install the libraries required to run the program. A text file requirements.txt will be present in the folder for installing the packages.\
     pip install -r requirements.txt
  4. Create a config.json file to add username, app_password, from (Email sent from) and to (Email sent to) in the file as a json object.
  5. Once the packages are installed, the application scrapper.py can be run from the command prompt / terminal.\
     python scrapper.py
  6. Email with the intended receipient who will recieve the required information.
  
**Author: Aditya Mulik**
