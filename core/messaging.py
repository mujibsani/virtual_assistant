import smtplib
from core.secrets import sender_email, to, epwd
from email.message import EmailMessage
import pyautogui
import webbrowser
from time import sleep


def send_email(receiver, subject, email_content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, epwd)
    server.sendmail(sender_email, to, email_content)
    email = EmailMessage()
    email['From'] = sender_email
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(email_content)
    server.send_message(email)
    server.close()


def whats_app_message(phone_number, message):
    Message = message
    webbrowser.open('http://web.whatsapp.com/send?phone=' + phone_number + '&text=' + Message)
    sleep(10)
    pyautogui.press('enter')
