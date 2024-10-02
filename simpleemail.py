import smtplib

def send_email(sender_email, sender_password, receiver_email, subject, body):
    # Create SMTP session
    with smtplib.SMTP('smtp.example.com', 587) as server:
        # Start TLS for security
        server.starttls()
        # Log in to the SMTP server
        server.login(sender_email, sender_password)

        # Compose the email
        email_message = f"Subject: {subject}\n\n{body}"

        # Send the email
        server.sendmail(sender_email, receiver_email, email_message)

# Example usage:
sender_email = "ourprojectemails@gmail.com"
sender_password = "oxipcucyayarblht"
receiver_email = "amruthavm.kedilaya@gmail.com"
subject = "Hello from Python!"
body = "This is a test email sent from a Python script."

send_email(sender_email, sender_password, receiver_email, subject, body)
