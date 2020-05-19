import os
import smtplib
import imghdr
from email.message import EmailMessage


# EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
# EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
EMAIL_ADDRESS = '2444093230x@gmail.com'
EMAIL_PASSWORD = 'y50024019923677*'

contacts = ['YourAddress@gmail.com', 'test@example.com']

msg = EmailMessage()
msg['Subject'] = 'Check out Bronx as a puppy!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS

msg.set_content('This is a plain text email')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""", subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

# import numpy as np
# np.random.seed(20)
# data = np.random.randint(1, 20, (3, 4), dtype=np.int)
# print(data)