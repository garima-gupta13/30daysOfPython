#EMAIL INBOX VIA PYTHON
import imaplib  # to open email from inbox
import email


host = "imap.gmail.com"
username ='techsavygg@gmail.com'
password='azbgtyqngrichdkd'


##read the UNSEEN emails

# def get_inbox():
#     #1. login 
#     mail = imaplib.IMAP4_SSL(host)
#     mail.login(username,password)
#     mail.select("inbox")
#     my_message = []
#     _, search_data = mail.search(None, 'UNSEEN')
#     for num in search_data[0].split():
#         email_data = {}  #created dictionary
#         #print(num)
#         _,data = mail.fetch(num,'(RFC822)')
#         #print(data[0])
#         a , b = data[0]
#         #oiginal is in bytes == as b -- in beginning == so convert to string
#         _, b = data[0]
#         email_message = email.message_from_bytes(b)
#         print(email_message)

#         for header in ['subject','to','from','date']:
#             print("{}:{}".format(header, email_message[header]))
#             email_data[header] = email_message[header]
#         for part in email_message.walk():
#             if part.get_content_type() == "text/plain" :
#                 body = part.get_payload(decode= True)
#                 #print(body.decode())  # as in bytes , so to decode
#                 email_data['body'] = body.decode()
#             elif part.get_content_type() == "text/html":
#                 html_body = part.get_payload(decode= True)
#                 #print(html_body.decode())  # as in bytes , so to decode
#                 email_data['html_body'] = html_body.decode()
#         my_message.append(email_data)
#     return my_message
def get_inbox():
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select("inbox")
    _, search_data = mail.search(None, 'UNSEEN')
    my_message = []
    for num in search_data[0].split():
        email_data = {}
        _, data = mail.fetch(num, '(RFC822)')
        # print(data[0])
        _, b = data[0]
        email_message = email.message_from_bytes(b)
        for header in ['subject', 'to', 'from', 'date']:
            print("{}: {}".format(header, email_message[header]))
            email_data[header] = email_message[header]
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                email_data['body'] = body.decode()
            elif part.get_content_type() == "text/html":
                html_body = part.get_payload(decode=True)
                email_data['html_body'] = html_body.decode()
        my_message.append(email_data)
    return my_message


if __name__ == "__main__":
    my_inbox = get_inbox
    print(my_inbox)


    ## dont know while runnint for me its not returning the mail that i sent the unseen one, only guiiving output as 
    ## --- <function get_inbox at 0x000001CFA9181440>