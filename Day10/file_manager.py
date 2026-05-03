import os  # OS is whatw orks accros systhem -- linex, wndows, mac --- as python is crossplatform -

#1.email_txt="D:\\33_Fulltime-resume\\1-Preparation\\Data Engineer\\Python_Learning\\30daysOfPython\\Day10\\templates\\email.txt"

#2.email_txt = "templates\\email.txt"
#3. #email_txt = "templates/email.txt"   ##forward slash work accross OS , so this is best way to add -giving forward slash

#4. email_txt = os.path.join("templates","email.txt")   --this is juts relative path , so if i come out of the directly:
# PS D:\33_Fulltime-resume\1-Preparation\Data Engineer\Python_Learning\30daysOfPython\Day10> & will try to run =python file_manager.py
# it will give eror - as the path would not exist for this email.txt 
# so will have to give the proper =ABSOLUTE PATH == to email.txt

this_file_path = os.path.abspath(__file__)  ##__file__ =works inside the MMODULE - i.e this file - on command directly it will not work== as it becomes teh object for this file 
#print(this_file_path)
BASE_DIR = os.path.dirname(this_file_path) #will give till Day10
ENTIRE_PROJECT_DIR = os.path.dirname(BASE_DIR)  #runend one more time so will give till 30daysofPython=projectpath
#print(BASE_DIR, ENTIRE_PROJECT_DIR)
email_txt = os.path.join(BASE_DIR,"templates","email.txt")
content =""

with open(email_txt,'r') as f:
    content = f.read()


print(content.format(name='Justin'))