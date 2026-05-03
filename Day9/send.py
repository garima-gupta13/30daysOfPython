import sys
import requests
from formatting import format_msg
from send_mail import send_mail
def send(name, website = None, to_email =None, verbose = False):
    if (website is not None):
        msg = format_msg(my_name=name, my_website= website)
    else :
        msg = format_msg(my_name = name)
    
    if(verbose): 
        print(name, website, to_email)

    #send the email
    try:
        send_mail(text=msg,to_emails =[to_email],html =None)
        print('Email sent')
        sent = True
    except:
        sent = False
    return sent
    # r = requests.get("http://httpbin.org/json")
    # if(r.status_code == 200):
    #     return r.json()
    # else:
    #     return "There was an error"


def main():
    print(sys.argv) 
    name = "Unknown"
    website = "Unknown"
    if len(sys.argv) >1 :
        name = sys.argv[1]
    if len(sys.argv) >2 :
        email = sys.argv[2]
    response = send(name,to_email=email , verbose =True)
    print(response) 

if __name__ == "__main__":
    main()

