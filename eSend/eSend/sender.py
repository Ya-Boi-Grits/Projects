import os, ssl, smtplib
from email.message import EmailMessage

g_pass = os.getenv('G_APP_PASS')


e_sender = 'grave.determination@gmail.com'
e_password = g_pass
e_receiver = 'wosepid914@bitvoo.com'
e_subject = 'This is a test subject'
e_body = ''' I'M NOT YELLING IM JUST ANGRY DSLIFHG CUADLSIHF
'''

em = EmailMessage()
em['FROM'] = e_sender
em['TO'] = e_receiver
em['Subject'] = e_subject
em.set_content(e_body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gemail.com', 465, context=context) as smtp:
    smtp.login(e_sender, e_password)
    smtp.sendmail(e_sender, e_receiver, em.as_string())
