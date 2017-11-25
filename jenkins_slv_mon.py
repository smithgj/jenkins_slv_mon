import requests
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def alert(alert_text):
    from_addr = "greg.smith@merrillcorp.com"
    to_addr = "6123211852@tmomail.net"

    # Create message container - the correct MIME type is multipart/alternative.
    message = MIMEMultipart('alternative')
    # message['Subject'] = "my subject"
    message['From'] = from_addr
    message['To'] = to_addr

    # Create the body of the message
    html_msg1 = """\
    <html>
      <head></head>
      <body>
        <p>
    """
    html_msg2 = """\
        </p>
      </body>
    </html>
    """
    html_msg = html_msg1 + alert_text + html_msg2

    # Record the MIME types of both parts - text/plain and text/html.
    html_part = MIMEText(html_msg, 'html')
    message.attach(html_part)

    # Send the message via local SMTP server.
    server = smtplib.SMTP('relay.stp.mrll.com')
    server.sendmail(from_addr, to_addr, message.as_string())
    server.quit()

try:
    target = 'http://us2-jenkins-1.adminsys.mrll.com:8080/computer/svc-us2p-too-12.adminsys.mrll.com/api/json?pretty=true'
    slv_data = requests.get(target, auth=('gsmithb', 'C@$@8927'))
    slv_data.raise_for_status()
except requests.HTTPError as e:
    print(e)
    alert('Error connecting to http://us2-jenkins-1.adminsys.mrll.com:8080/computer/svc-us2p-too-7.adminsys.mrll.com/api/json?pretty=true')
    alert(e)
    sys.exit(1)
if ((slv_data.json()).get('offline')) or ((slv_data.json()).get('temporarilyOffline')):
#   print ('Jenkins slave svc-us2p-too-12.adminsys.mrll.com is DOWN')
    alert('Jenkins slave svc-us2p-too-12.adminsys.mrll.com is DOWN')

