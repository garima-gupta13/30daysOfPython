import smtplib  # to send msg from mail server
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#now to send an email we must login in account and send
#we can also set these in ENVIRONMENT variables
username ='techsavygg@gmail.com'
password='azbgtyqngrichdkd'  ## thisis the app passwrod and not the email password - in word fiel have mentioend steps

def send_mail(text='Email Body', subject ='Hello World', from_email = 'Hungry Py<techsavygg@gmail.com>', to_emails = None, html = None):
    assert isinstance(to_emails,list) ## so i want to see if to_emails - is a list & if its not raise aan error -- thus gave ASSERT


    #now we ned to  fromulate the string to pass in the msg_str == we can use string butwont be abl;e to send an email directly using string, have to use defualt things that are there, os importing MIMEMultipart == allows to attach the plain text with HTML text & also Files --
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject

    txt_part = MIMEText(text,'plain')
    msg.attach(txt_part)
    if(html is not None):
        html_part = MIMEText("<h1>This is working</h1>",'html')
        msg.attach(html_part)
    msg_str = msg.as_string()
    #l)login to my  smtp server == smtp that helps to send email - we have python's inbuild library to use this - smtplib = we can use smtp- to create smtp server

    server = smtplib.SMTP(host='smtp.gmail.com',port = 587) #host from where we are sending, if someother domain then add that, and 587 is the standard port to use
    server.ehlo()
    server.starttls()
    server.login(username,password)  ##login with username & password
    server.sendmail(from_email, to_emails, msg_str)

    server.quit()  #to quit the smtp server connection that we have

    # Can do this way also & it will automatically exist when its done: we are doing above as want to see step by steps whats happening
    #with smtplib.SMTP() as server:
           #server.login()
           #pass



