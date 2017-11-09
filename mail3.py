import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_addr = "greg.smith@merrillcorp.com"
to_addr = "6123211852@tmomail.net"

# Create message container - the correct MIME type is multipart/alternative.
message = MIMEMultipart('alternative')
# message['Subject'] = "my subject"
message['From'] = from_addr
message['To'] = to_addr

# Create the body of the message
html_msg = """\
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
html_part = MIMEText(html_msg, 'html')
message.attach(html_part)

# Send the message via local SMTP server.
server = smtplib.SMTP('relay.stp.mrll.com')
server.sendmail(from_addr, to_addr, message.as_string())
server.quit()
