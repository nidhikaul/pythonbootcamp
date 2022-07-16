import smtplib
import datetime as dt
import random

my_email = "abc@gmail.com"
password = "yourpassword"


import datetime as dt

now = dt.datetime.now()
# year = now.year
# month = now.month
weekday = now.weekday()

#Send email every wednesday

if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="xyz@gmail.com", 
            msg=f"Subject:Wednesday Motivation\n\n{quote}"
        )

# date_of_birth = dt.datetime(year=1991, month=7, day=21 )
# print(date_of_birth)