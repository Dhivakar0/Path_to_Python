from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

my_email = os.environ["my_email"]
password = os.environ["password"]
recipient_email = os.environ["recipient_email"]

url = "https://appbrewery.github.io/instant_pot/"
# url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
  }

response = requests.get(url=url,headers=headers,verify=False)
webpage = response.text

soup = BeautifulSoup(webpage,"html.parser")
product = soup.select_one("#productTitle")
product_title =  " ".join(product.getText(strip=True).split())
print(product_title)
current_price = float(soup.select_one(".aok-offscreen").getText().strip()[1:])
print(current_price)

lowest_price = 100.00

if current_price < lowest_price:
    try:
        with smtplib.SMTP(host="smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(my_email,password)
            connection.sendmail(my_email,recipient_email,msg=f"Subject:Amazon Price Alert!\n\n{product_title}is now ${current_price}.".encode("utf-8"))
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending mail: {e}.")




