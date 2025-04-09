##################### Extra Hard Starting Project ######################



# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

my_email = "pythontestingku@gmail.com"
password = "bfwtawemsvrruiue"
recipient_email = "pythontestingkudaan@yahoo.com"

import datetime as dt
import smtplib
import pandas

now = dt.datetime.now()
today_date = now.day
this_month = now.month

with open("birthdays.csv") as file:
    birthday_file = pandas.read_csv(file)
    bday_dict = birthday_file.to_dict(orient="records")
    bday_dict["month"]



