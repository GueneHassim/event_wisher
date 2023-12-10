
# The goal is to write a simple Python code that allows me to automate
## redundant tasks such as sending birthday wishes, etc.
### To achieve this, I'm going to use the smtplib and datetime modules.
#### Learning goal: With this project, my aim is to briefly explore these
##### two modules.
###### I will upgrade it with a little GUI using Tkinter at a later time.
##### us random module as well for the random selection of the quote to send

import smtplib
import datetime as dt
import random

EVENT_DATE = "2023-12-2" #you must change it yours current day

MY_EMAIL =  "" #insert your email in the bracket
MY_PK = "mijj ojmc kkjz xlex" "" #insert your email application password in the bracket
RECEIVER_EMAIL = "" # receiver_email


#with datetime i create a str of the current day
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

today_date = f"{year}-{month}-{day}"

#open quotes file and randomly pick a quote to send
def quote_pick():
    with open("./quotes.txt") as note:
        quotes_data = note.readlines()
        quote_index = random.randint(0, len(quotes_data))
        quote = quotes_data[quote_index] 
        return quote

def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PK)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECEIVER_EMAIL, msg=f"Subject:Hello\n\n{quote_pick()}")

# Now, for the last part: comparing the current date with a condition and generating an automatic
## email sent from a specified address to a specific address...
### I may consider upgrading it later with additional features, such as a database of people with birthdays
#### or other types of events.

#event_date = input("write the evente date in the following way Y-M-D:")
#event_name = input("write down a brief bio about the event, eg. 'Sempronio bday'")
if today_date == EVENT_DATE:
    send_email()
    print(f"email sended to {RECEIVER_EMAIL}")
