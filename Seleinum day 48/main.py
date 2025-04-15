from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.amazon.in/Axor-Apex-Hunter-Black-Helmet-M/dp/B08L84TB6R/ref=sr_1_1_sspa?crid=3SOJS95RWGTWS&dib=eyJ2IjoiMSJ9.KFylZ37Uju3MRyYqDqXozGLmzPIOYQbpsmlWDpaoi-l2HL2r_r-d2HllDPzLUFOJCN9YK0s8pmc_7LRu6_CAP1jGScoNtvPlQ3sgWqZ08dv-gy-hij8okgPOTVWpKaMnAqBj0t0lpISA7hV9dYBk70dQi6NJELmuf48JBggjYvu7hbrs5eW80z2GMHpR89eRboud08yLnvwCeZV_-jacv6bJVKSsEHywesBU-RyMq8MiCISnbjzJsbSyKt937sisWl3hkApgRQK5tmBw4DF0Xi5Rp_0Rich9oU-1S8vi2uc.6JdtKXnlNtcES0m_GCgUeFNzeh2pKFH0AwbTdars8YI&dib_tag=se&keywords=axor%2Bapex%2Bhunter&nsdOptOutParam=true&qid=1744402773&sprefix=axor%2Bapex%2Bhu%2Caps%2C304&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")

dollar_price = driver.find_element(By.ID,value="a-price-whole")
print(dollar_price)

driver.quit()