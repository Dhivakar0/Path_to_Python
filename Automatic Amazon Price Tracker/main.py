from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

my_email = os.environ["my_email"]
password = os.environ["password"]
recipient_email = os.environ["recipient_email"]

# url = "https://appbrewery.github.io/instant_po/t/"
# url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
url = "https://www.amazon.in/Axor-Apex-Hunter-Black-Helmet-M/dp/B08L84TB6R/ref=sr_1_1_sspa?crid=3SOJS95RWGTWS&dib=eyJ2IjoiMSJ9.KFylZ37Uju3MRyYqDqXozGLmzPIOYQbpsmlWDpaoi-l2HL2r_r-d2HllDPzLUFOJCN9YK0s8pmc_7LRu6_CAP1jGScoNtvPlQ3sgWqZ08dv-gy-hij8okgPOTVWpKaMnAqBj0t0lpISA7hV9dYBk70dQi6NJELmuf48JBggjYvu7hbrs5eW80z2GMHpR89eRboud08yLnvwCeZV_-jacv6bJVKSsEHywesBU-RyMq8MiCISnbjzJsbSyKt937sisWl3hkApgRQK5tmBw4DF0Xi5Rp_0Rich9oU-1S8vi2uc.6JdtKXnlNtcES0m_GCgUeFNzeh2pKFH0AwbTdars8YI&dib_tag=se&keywords=axor%2Bapex%2Bhunter&nsdOptOutParam=true&qid=1744402773&sprefix=axor%2Bapex%2Bhu%2Caps%2C304&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"

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
print(product)
# current_price = float(soup.select_one(".aok-offscreen").getText().strip()[1:6])
current_price = float(soup.select_one(".a-price-whole").getText().replace(",","").replace(".",""))
print(current_price)

lowest_price = 5000.00

if current_price < lowest_price:
    try:
        with smtplib.SMTP(host="smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(my_email,password)
            connection.sendmail(my_email,recipient_email,msg=f"Subject:Amazon Price Alert!\n\n{product_title} is now ${current_price}.".encode("utf-8"))
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending mail: {e}.")




