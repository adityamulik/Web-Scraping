import requests, time, smtplib, json
from bs4 import BeautifulSoup

# Accessing Credentials
secrets_path = "./.secrets.json"

with open(secrets_path, "r") as handler:
    secrets = json.load(handler)

url = 'https://www.amazon.com/Apple-iPhone-64GB-Space-Gray/dp/B07ZPKZSSC/ref=sr_1_5?dchild=1&keywords=iphone+11&qid=1603338202&sr=8-5'

headers = {
        'authority': 'www.amazon.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

# Sleep to avoid API overload
time.sleep(5)

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

price = soup.find_all('span', {'class': 'a-size-medium a-color-price priceBlockBuyingPriceString'})[0].text.strip()

in_stock = soup.find('div', {"id": "availability"}).find('span').text.strip()

product_name = soup.find('h1', {"id": "title"}).find('span').text.strip()

# Email function to send the details

def my_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(secrets["email"], secrets["app_password"])

    subject = f'{product_name} is available'
    body = f'\n{product_name} current price is {price} and the remaining stock is {in_stock}! '

    message = subject + body

    server.sendmail(secrets["from"], secrets["to"], message)

    server.quit()

my_email()