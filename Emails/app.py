import smtplib

conn = smtplib.SMTP('smtp.gmail.com',587)
conn.ehlo()
conn.starttls()
conn.login('useyouremail@gmail.com','useyourpassword@password')
conn.sendmail('myothermail@gmail.com','adithyakamath96@gmail.com','Subject: How are you?\n How are you? Let\'s meetup for lunch!')
conn.quit()
