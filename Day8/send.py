import sys
import requests
from formatting import format_msg
def send(name, website = None, verbose = False):
    if (website is not None):
        msg = format_msg(my_name=name, my_website= website)
    else :
        msg = format_msg(my_name = name)
    
    if(verbose): 
        print(name, website)

        #send the message
    r = requests.get("http://httpbin.org/json")
    if(r.status_code == 200):
        return r.json()
    else:
        return "There was an error"


def main():
    print(sys.argv)  # returns list of all teh arguments tha tare passed in the command line
    name = "Unknown"
    website = "Unknown"
    if len(sys.argv) >1 :
        name = sys.argv[1]
        website = sys.argv[2]
    response = send(name,website , verbose =True)
    print(response) 
# pypi.org ==> to download third party packages
#and importing 3rd party packages

#A)to call this send function directly on call of this send module -- i.e send.py
#response = send("Justin", verbose =True)
#print(response)

#B) better pythonic way to do this is , means to call the function direcly on startup - i.e when this file is called only then it runs , and when send.py is imported else where then this doenst run
if __name__ == "__main__":
    main()


    ##so now only when the send.py is called this main() function will be called
    ## and it will not be called on the import send ==
    ## as import loads teh entire code so