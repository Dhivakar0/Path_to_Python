# import smtplib
#
# my_email = "pythontestingku@gmail.com"
# password = "bfwtawemsvrruiue"
# recipient_email = "pythontestingkudaan@yahoo.com"
#
# with smtplib.SMTP(host="smtp.gmail.com",port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(from_addr=my_email,to_addrs="pythontestingkudaan@yahoo.com",
#                         msg="Subject:Study well\n\n You can do it!!!")



# *************************************************************************************************


import smtplib
import random
import datetime as dt

my_email = "pythontestingku@gmail.com"
password = "bfwtawemsvrruiue"
recipient_email = "pythontestingkudaan@yahoo.com"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 4:
    with open("quotes.txt") as file:
        quotes_list = file.readlines()
        quote = random.choice(quotes_list)
        subject = "Here is today's quote for the day!"

        with smtplib.SMTP(host="smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email,to_addrs=recipient_email,msg=f"Subject:{subject}\n\n{quote}.")



