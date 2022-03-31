import pyinputplus as pypi

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class Gemailer:

    def __init__(self, address_receive, email_content):
        self.browser = webdriver.Firefox()
        self.browser.get('https://mail.google.com/')
        self.address_receive = address_receive
        self.email_content = email_content
        self.sender_login = 'destoper.automate@gmail.com' 
        self.sender_pass = '81176852'

    def main(self):
        '''Call the main functions and start'''
        self.__login()
        self.__send_email()
        self.__end_message()

    def __login(self):
        '''Call login functions and give time to load pages'''
        self.__login_user()
        sleep(3)                           # sleep to give time to load the page
        self.__login_password()
        sleep(3)                           # sleep to give time to load the page

    def __login_user(self):
        '''LOGIN: user step'''
        # Writing email
        login_elem = self.browser.find_element_by_css_selector("input[type='email']")
        login_elem.send_keys('destoper.automate@gmail.com')
        # Send user button
        login_button_elem = self.browser.find_element_by_xpath('//*[@id="identifierNext"]/div/button')
        login_button_elem.click()

    def __login_password(self):
        '''LOGIN: user password step'''
        # Writing email
        password_elem = self.browser.find_element_by_css_selector("input[type='password']")
        password_elem.send_keys(self.sender_pass)
        # Send user button
        password_button_elem = self.browser.find_element_by_xpath('//*[@id="passwordNext"]/div/button')
        password_button_elem.click()

    def __send_email(self):
        '''Call send functions and give time to load pages'''
        self.browser.get('https://mail.google.com/mail/u/0/#inbox?compose=new')  # changing URL to send the email
        sleep(3)                                                                 # sleep to give time to load the page
        self.__send_to()
        self.__send_content() 
        self.__send_press_button()           

    def __send_to(self):
        '''SEND EMAIL: email recipient step'''
        to_elem = self.browser.find_element_by_css_selector("textarea[name=to]")
        to_elem.send_keys(self.address_receive)   

    def __send_content(self):
        '''SEND EMAIL: email content step'''
        content_elem = self.browser.find_element_by_css_selector("div[aria-label='Corpo da mensagem']")    # You need to change the aria-label name to your language
        content_elem.send_keys(self.email_content)    

    def __send_press_button(self):
        '''SEND EMAIL: press send button and print finish message'''
        send_button_elem = self.browser.find_element_by_css_selector("div[aria-label='Enviar ‪(Ctrl-Enter)‬']") # You need to change the aria-label name to your language
        send_button_elem.click()                                           
 
    def __end_message(self):
        print('EMAIL SENT!')

if __name__ == '__main__':
    recipient = pypi.inputEmail(prompt='Enter the recipient email: ')
    content = pypi.inputStr(prompt='Email content: ')
    
    spam = Gemailer(recipient, content)
    spam.main()