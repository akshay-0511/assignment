#1)to check the given phone is valid or not
import re
def isvalid(num):
    pattern=re.compile('^[+]?\d{3}[-\s\.]?\d{3}[-\s\.]\d{4}')
    return pattern.match(num)
num=input('enter num:')
if isvalid(num):
    print("valid phone number")
else:
    print('invalid phone number')



#2)extracting the emails
import re
import requests
url= input("enter the url:- ")
email=r"[\w\.-]@+[\w\.-]+"
r= requests.get(url)
for email in re.findall(email, r.text):
    print(f"emails:- \n{email}")






#3)one line questions 
#frankly said i do not about the linux but i am sure i can if i get to work on it or tarian about it


# i crated the web application by using the django and python but yet not host... that application just about the trainning institute site. if go to this page u get to know about the institute, training details, course details , trainner information and HR number. and if you click on the join then you get one form that store your information in DB.