from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup
from threading import Thread
def usernames():
	users=[]
	unames=open("usernames.txt",'r')
	for uname in unames.readlines():
			users.append(uname.strip('\n'))
	return users
        
def passwords():
	passwds=[]
	passwords=open("passwords.txt",'r')
	for password in passwords.readlines():
			passwds.append(password.strip('\n'))
	return passwds


def Main():
	start=int(input("Where to start?")) #because running all instances might freeze your system 
	end=int(input("Where to end?"))
	for i in range(start,end):
		t=Thread(target=enter(i))
		t.start()
def enter(i):
		browser=webdriver.Chrome()
		browser.get("https://jgi.i-on.in")

		#Entering username
		username=browser.find_element_by_id("cpusername")
		uname=usernames()
		username.send_keys(uname[i]) 


	    # Entering password
		password=browser.find_element_by_id("cppassword")
		pwd=passwords()
		password.send_keys(pwd[i])
		
		checkbox=browser.find_element_by_id("checkTerm")
		checkbox.click()

		password.submit()
		browser.close()
		browser.quit()


	
if (__name__=="__main__"):

	Main()


