import smtplib

FROMADDR="greg.smith@merrillcorp.com"

TOADDRS="6123211852@tmomail.net"
SUBJECT="Test"
TEXT = "This is some text\r\n"
#message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
message = '{}'.format( TEXT)
server=smtplib.SMTP()
server.set_debuglevel(1)
server.connect('relay.stp.mrll.com')
server.sendmail(FROMADDR, TOADDRS, message)
server.quit()
