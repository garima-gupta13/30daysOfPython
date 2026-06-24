import smtplib  # to send msg from mail server
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from templates import Template
#now to send an email we must login in account and send
#we can also set these in ENVIRONMENT variables
username ='techsavygg@gmail.com'
password='azbgtyqngrichdkd'  ## thisis the app passwrod and not the email password - in word fiel have mentioend steps


class Emailer():
    subject =""
    to_emails =[]
    has_html = False
    from_email = 'Hungry Py<techsavygg@gmail.com>'
    template_name = None
    template_html = None
    context= {}
    test_send =False
    def __init__(self,subject,template_name=None, context={}, template_html =None, to_emails= None, test_send=False):
        if template_name == None and template_html == None:
            raise Exception("You must set a template")
        assert isinstance(to_emails, list)
        self.to_emails = to_emails
        self.subject = subject
        if template_html != None:
            self.has_html = True
            self.template_html = template_html
        self.template_name = template_name
        self.context = context
        self.test_send = test_send

    def format_msg(self):
        #now we ned to  fromulate the string to pass in the msg_str == we can use string butwont be abl;e to send an email directly using string, have to use defualt things that are there, os importing MIMEMultipart == allows to attach the plain text with HTML text & also Files --
        msg = MIMEMultipart('alternative')
        msg['From'] = self.from_email
        msg['To'] = ", ".join(self.to_emails)
        msg['Subject'] = self.subject
       
        if self.template_name !=None :
            tmpl_str = Template(self.template_name,self.context)
            txt_part = MIMEText(tmpl_str.render(),'plain')
            print(txt_part)
            msg.attach(txt_part)
        if self.template_html !=None :
            tmpl_str = Template(self.template_html,self.context)
            html_part = MIMEText(tmpl_str.render(),'html')
            print(html_part)
            msg.attach(html_part)
        msg_str = msg.as_string()
        return msg_str

    def send_mail(self):
        msg = self.format_msg()

        #l)login to my  smtp server == smtp that helps to send email - we have python's inbuild library to use this - smtplib = we can use smtp- to create smtp server

        did_send = False
        if not self.test_send:
            with smtplib.SMTP(host='smtp.gmail.com',port = 587) as server:
                server.ehlo()
                server.starttls()
                server.login(username,password)  ##login with username & password
                try:
                    server.sendmail(self.from_email, self.to_emails, msg)
                    did_send =True
                except:
                    did_send =False
        return did_send










#Will create a class for SEND_EMAIL also :: ABOVE created the class
# import smtplib  # to send msg from mail server
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# #now to send an email we must login in account and send
# #we can also set these in ENVIRONMENT variables
# username ='techsavygg@gmail.com'
# password='azbgtyqngrichdkd'  ## thisis the app passwrod and not the email password - in word fiel have mentioend steps

# def send_mail(text='Email Body', subject ='Hello World', from_email = 'Hungry Py<techsavygg@gmail.com>', to_emails = None, html = None):
#     assert isinstance(to_emails,list) ## so i want to see if to_emails - is a list & if its not raise aan error -- thus gave ASSERT


#     #now we ned to  fromulate the string to pass in the msg_str == we can use string butwont be abl;e to send an email directly using string, have to use defualt things that are there, os importing MIMEMultipart == allows to attach the plain text with HTML text & also Files --
#     msg = MIMEMultipart('alternative')
#     msg['From'] = from_email
#     msg['To'] = ", ".join(to_emails)
#     msg['Subject'] = subject

#     txt_part = MIMEText(text,'plain')
#     msg.attach(txt_part)
#     if(html is not None):
#         html_part = MIMEText("<h1>This is working</h1>",'html')
#         msg.attach(html_part)
#     msg_str = msg.as_string()
#     #l)login to my  smtp server == smtp that helps to send email - we have python's inbuild library to use this - smtplib = we can use smtp- to create smtp server

#     server = smtplib.SMTP(host='smtp.gmail.com',port = 587) #host from where we are sending, if someother domain then add that, and 587 is the standard port to use
#     server.ehlo()
#     server.starttls()
#     server.login(username,password)  ##login with username & password
#     server.sendmail(from_email, to_emails, msg_str)

#     server.quit()  #to quit the smtp server connection that we have

#     # Can do this way also & it will automatically exist when its done: we are doing above as want to see step by steps whats happening
#     #with smtplib.SMTP() as server:
#            #server.login()
#            #pass



