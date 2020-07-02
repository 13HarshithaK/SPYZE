import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
def eml(alert):
    fromaddr = "anonh131998@gmail.com"
    toaddr = "anonh131998@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "SPYZE alert"
    body = alert +" "+str(time.time())
    msg.attach(MIMEText(body, 'plain'))
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("emailid", "password")
    text = msg.as_string()
    s.sendmail("emailid", "password", text)
    s.quit()