# Email sending via smtp(simple mail transfer protocol) using python
# import smtplib

# from email.mime.text import MIMEText      # multipurpose internet mail extantion

# from email.mime.multipart import MIMEMultipart

# from email.mime.base import MIMEBase

# from email import encoders


# send email to reciever and sender detail  




# sender_email = 'mfaizesumara20@gmail.com'  # sender email address
# receiver_email = 'padaliyameet558@gmai.com' # receiver email address
# app_password = 'tvgq stzj uelp ifyt'  # app password for sender email account

# massage = MIMEMultipart()  # create a multipart message object
# massage['From'] = sender_email  # set the sender email address
# massage['To'] = receiver_email  # set the receiver email address
# massage['Subject'] = 'This is a test email'  # set the subject of the email


# # set email text

# body = 'Hello: \n this is a test email sent from Python!'  # email body text
# massage.attach(MIMEText(body, 'plain'))  # attach the body text to the message object


# # used exception handling to send email
# file_path = 'C:/Users/HP/Desktop/Email Attachment.txt'  # path to the attachment file   
# try:

#     # connect email with gmail server
#     with open(file_path, 'rb') as attachment:
#         part = MIMEBase('application', 'octet-stream')
#         part.set_payload(attachment.read())

#         encoders.encode_base64(part)
#         part.add_header('Content-Disposition', f'attachment; filename={file_path}')
#         massage.attach(part)

#     server=smtplib.SMTP('smtp.gmail.com',587)
#     server.starttls()
#     server.login(sender_email,app_password)
#     text=massage.as_string()

#         # send email to reciver
#     server.sendmail(sender_email,reciever_email,massage.as_string())

#         # print a success message if email is sent successfully
#     print("email sent successfully")


# except Exception as e:
#     print("failed to send email")


# finally:
#     server.quit()




import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

#  stwn gjfr wsbm jffk

sender_email = 'mfaizesumara20@gmail.com'
receiver_email = 'mfaizesumara20@gmail.com'
app_password = 'stwn gjfr wsbm jffk'


# Create email
message = MIMEMultipart()

message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'This is a test email'


# Email body
body = 'Hello!\nThis is a test email sent from Python!'

message.attach(MIMEText(body, 'plain'))


# Attachment
file_path = 'MFAIZE.jpg'  # Path to the attachment file

try:

    # Open attachment
    with open(file_path, 'rb') as attachment:

        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())

        encoders.encode_base64(part)

        filename = os.path.basename(file_path)

        part.add_header(
            'Content-Disposition',
            f'attachment; filename="{filename}"'
        )

        message.attach(part)


    # Connect to Gmail
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    # Login
    server.login(sender_email, app_password)

    # Send email
    server.sendmail(
        sender_email,
        receiver_email,
        message.as_string()
    )

    print("Email sent successfully!")

    # Close server
    server.quit()


except Exception as e:

    print("Failed to send email")
    print("Error:", e)