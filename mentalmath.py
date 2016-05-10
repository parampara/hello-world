import selenium
from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

def Print (str):		
	print str
	sys.stdout.flush()

def PrinT(str):		
	print str,
	sys.stdout.flush()

def check_exists_by_xpath(webdriver,xpath):
    try:
        webdriver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

driver=webdriver.Firefox()
driver.get('https://rankyourbrain.com/mental-math/mental-math-test-easy/play')

WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, "answer")))

ans = driver.find_element_by_xpath('//*[@id="answer"]')

while check_exists_by_xpath(driver , '//*[@id="answer"]') :

	#time.sleep(1)

	ques = driver.find_element_by_xpath('//*[@id="beforeAnswer"]').text

	numlist=ques.split(' ')

	a=int(numlist[0])
	b=int(numlist[2])

	PrinT(ques)

	if numlist[1] == '+':
		x=a+b
	elif numlist[1] == '-' :
		x=a-b
	elif numlist[1] == '*' :
		x=a*b
	else :
		x=a/b	

	Print(str(x))

	ans.send_keys(str(x))

while 1==1 :
	a=b
