import pandas as pd
import smtplib
from datetime import datetime as dt
import random 


MY_EMAIL='santhoshspss321@gmail.com'
MY_PASSWORD='Hemanavin'
today =dt.now()
today_tuple=(today.month,today.day)

data =pd.read_csv('advanced_projects/Solution+-+birthday-wisher-end/birthdays.csv')

birth_dict={(data_row["month"], data_row["day"]): data_row for (index,data_row) in data.iterrows()}
print(birth_dict)
if today_tuple in birth_dict:
    birthdayperson =birth_dict[today_tuple]

    file_path=f'advanced_projects/Solution+-+birthday-wisher-end/letter_templates/letter_{random.randint(1,3)}.txt'
    with open(file_path) as letter:
        contents=letter.read()
        contents =contents.replace('[NAME]',birthdayperson['name'])

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthdayperson["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )    