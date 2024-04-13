import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_phishing_email(sender_email, sender_password, recipient_email, subject, message):
    try:
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()
        smtp_server.login(sender_email, sender_password)

        email_message = MIMEMultipart()
        email_message['From'] = sender_email
        email_message['To'] = recipient_email
        email_message['Subject'] = subject
        email_message.attach(MIMEText(message, 'plain'))

        smtp_server.send_message(email_message)
        print("Phishing email sent successfully")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        smtp_server.quit()

if __name__ == "__main__":
    sender_email = input("Enter your email address: ")
    sender_password = input("Enter your email password: ")
    recipient_email = input("Enter recipient's email address: ")
    subject = input("Enter email subject: ")
    message = input("Enter email message: ")

    send_phishing_email(sender_email, sender_password, recipient_email, subject, message)
