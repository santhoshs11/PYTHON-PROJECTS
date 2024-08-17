import smtplib


email='santhoshspss321@gmail.com'
password1='hwwp elix qofg nvei'


with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(email,password1)
    connection.sendmail(
        from_addr=email,
                        to_addrs='santhoshs.0325@gmail.com',
                        msg='subject:example msg 1\n\n this is a example message from smtp access')




