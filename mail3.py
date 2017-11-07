import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

me = "greg.smith@merrillcorp.com"
you = "6123211852@tmomail.net"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
# msg['Subject'] = "my subject"
msg['From'] = me
msg['To'] = you

# Create the body of the message
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the link you wanted.
    </p>
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
part = MIMEText(html, 'html')
msg.attach(part)

# Send the message via local SMTP server.
s = smtplib.SMTP('relay.stp.mrll.com')
s.sendmail(me, you, msg.as_string())
s.quit()