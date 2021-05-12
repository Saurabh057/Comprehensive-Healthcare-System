from selenium import webdriver

#driver = webdriver.Chrome()

def video():
	chromedriver = "chromedriver"
	driver = webdriver.Chrome(chromedriver)

	driver.get('https://web.whatsapp.com/')



# while True:
# 	name = input("Enter Name ::")

# 	msg = input("Enter msg::")

# 	count=int(input("Enter count"))


# 	user =driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
# 	user.click()	

# 	msg_box =driver.find_element_by_class_name('_13mgZ')

# 	for i in range(count):
# 		msg_box.send_keys(msg)
# 		button=driver.find_element_by_class_name('_3M-N-')
# 		button.click()

	
# 	ch=int(input("Wanna Continue"))
# 	if(ch==0):
# 		break;