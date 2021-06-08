from selenium import webdriver
import time
#driver = webdriver.Chrome()

def video():
	chromedriver = "/home/saurabh/BE project/projectv2/proj/chromedriver"
	driver = webdriver.Chrome(chromedriver)
	driver.maximize_window()

	driver.get('https://zoom.us/signin')

	email=driver.find_element_by_name('email')
	password=driver.find_element_by_name('password')
	email.send_keys('chs390118@gmail.com')
	
	password.send_keys('Mandakini@4')
	# driver.find_element_by_xpath("//button[contains(@class,'signin')]").click()
	time.sleep(10)

	driver.find_element_by_id('dropdown-hostmeeting').click()
	# password.submit()
	driver.find_element_by_xpath("//a[contains(text(),'With Video On')]").click();

	time.sleep(100)
	# button =driver.find_element_by_class_name('signin btn')
	# print(button)
	# time.sleep(10000)
	# driver.find_element_by_id('btnHostMeeting').click()

	# password.submit()

video()

# while True:
# 	name = input("Enter Name ::")

# 	msg = input("Enter msg::")

# 	count=int(input("Enter count"))


# 	user =driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
# 	user.click()	

# 	msg_box =driver.find_element_by_class_name('_13mgZ')

# 	for i in range(count):
# 		msg_box.send_keys(msg)
		# button=driver.find_element_by_class_name('_3M-N-')
# 		button.click()

	
# 	ch=int(input("Wanna Continue"))
# 	if(ch==0):
# 		break;