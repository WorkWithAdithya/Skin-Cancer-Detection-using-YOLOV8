import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


sender_email = "ourprojectemails@gmail.com"  # Enter your email
sender_password = "oxipcucyayarblht"      # Enter your email password

#receiver_email = receiver_entry.get()
receiver_email = "amruthavm.kedilaya@gmail.com"
#subject = subject_entry.get()
subject = "Feedback of the project"
message = "Person fall detected"

# Constructing the email
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

try:
    # Establishing a connection to the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Logging in to the email account
    server.login(sender_email, sender_password)
    # Sending the email
    server.send_message(msg)
    # Quitting the server
    server.quit()
    print( "Email sent successfully!")
except Exception as e:
    #messagebox.showerror("Error", f"An error occurred: {str(e)}")
    print( f"An error occurred: {str(e)}")

# Creating the GUI

