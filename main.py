import yagmail
import os
import pandas


#Sending Email to a List of Contacts

sender = "e.owusu89@gmail.com"

subject = "Interview Invitation"

contacts = pandas.read_csv('contacts.csv')
print(contacts)
yag = yagmail.SMTP(user = sender,password = os.getenv('PASSWORD'))
my_secret = os.environ['PASSWORD']


for index,rows in contacts.iterrows():
  content = f"""Hi {rows['name']} kindly consider this as an invitation for an interview"""
  yag.send(to=rows['email'], subject = subject, contents = content)


print("Email Sent!")
  




