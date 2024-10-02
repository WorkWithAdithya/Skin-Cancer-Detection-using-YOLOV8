import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import messagebox


def sendmail(sname,semail,filepath,pclass):
    name = sname
    email = semail
    print("Name:", name)
    print("Email:", email)
    sender_email = "ourprojectemails@gmail.com"  # Enter your email
    receiver_email = email
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'ourprojectemails@gmail.com'
    smtp_password = 'oxipcucyayarblht'

    # Create a multipart message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = 'Email with Image Attachment'

    # Add a message body
    message.attach(MIMEText('Predicted Disease is: '+ pclass))

    # Attach the image
    with open(filepath, 'rb') as file:
        image_data = file.read()
    predictedimg=filepath
    print(predictedimg)
    image = MIMEImage(image_data, name=predictedimg)
    message.attach(image)

    # Connect to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(message)

    messagebox.showinfo("MessageBox",'Email sent successfully.')