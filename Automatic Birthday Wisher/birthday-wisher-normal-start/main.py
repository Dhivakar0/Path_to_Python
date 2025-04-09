import datetime as dt
import pandas
import random
import smtplib

my_email = "pythontestingku@gmail.com"
password = "bfwtawemsvrruiue"
recipient_email = "pythontestingkudaan@yahoo.com"

now = dt.datetime.now()
today_day = now.day
today_month = now.month
today = (today_month,today_day)

file = pandas.read_csv("birthdays.csv")

birthday_dict = {(row['month'],row['day']): row for (_,row) in file.iterrows()}

if today in birthday_dict:
    letters = ["letter_1.txt","letter_2.txt","letter_3.txt"]
    with open(f"./letter_templates/{random.choice(letters)}") as letter:
        content = letter.read()
        new_letter = content.replace('[NAME]',birthday_dict[today]["name"])
    try:
        with smtplib.SMTP(host="smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(my_email,password=password)
            connection.sendmail(from_addr=my_email,to_addrs=birthday_dict[today]["email"],msg=f"Subject:Happy Birthday!\n\n{new_letter}")

    except Exception as e:
        print(f"Error connecting to SMTP server: {e}")
