from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from random import choice

class Play2048:

    def __init__(self):
        self.browser = webdriver.Firefox()        
        
    def start(self):
        ''''Inicialize basic elements and run looper'''
        self.browser.get('https://play2048.co/')
        self.retry_elem = self.browser.find_element(By.CLASS_NAME, 'retry-button')
        self.running()

    def running(self):
        ''''Loop through the script functions'''
        while True:
            self.random_movement()
            self.its_over()               
   
    def random_movement(self):
        '''Input random movements to the game'''
        html_Elem = self.browser.find_element(By.TAG_NAME,'html')
        movement_values = ['UP', 'LEFT', 'DOWN', 'RIGHT']        
        for element in movement_values:
            movement = choice(movement_values)            
            if movement == 'UP':
                html_Elem.send_keys(Keys.ARROW_UP)
            elif movement == 'LEFT':
                html_Elem.send_keys(Keys.ARROW_LEFT)
            elif movement == 'DOWN':
                html_Elem.send_keys(Keys.ARROW_DOWN)
            elif movement == 'RIGHT':
                html_Elem.send_keys(Keys.ARROW_RIGHT)
            sleep(0.2)
       
    def its_over(self):        
        '''Verify if the game is over'''
        if self.retry_elem.is_displayed():            
            sleep(2)
            self.retry_elem.click()
           
     
if __name__ == '__main__':
    spam = Play2048()
    spam.start()  