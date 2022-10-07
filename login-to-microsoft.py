#----------------------
# Login into Microsoft
#----------------------
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import colorama, time
from colorama import Fore, Back, Style
colorama.init()

#Declare Chrome options and install driver if need be
chrome_options = webdriver.ChromeOptions()  
#Uncomment below code to keep page open before closing, useful when modifying input
#chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))

#Maximize the browser URL 
driver.get("") #Add
driver.maximize_window()

def microsoft_login():
    try: 
        time.sleep(1.9) 	
        username = "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]"
        driver.find_element(by=By.XPATH, value=username).send_keys("") #Add

        #Hit the 'next' button
        next_button = WebDriverWait(driver, .9).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div"))
            )
        next_button.click()
        
        #Enter password
        time.sleep(1)
        password = "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input"
        driver.find_element(by=By.XPATH, value=password).send_keys("") #Add
       
        #Hit the 'sign-in' button to staying signed in
        sign_in_button = WebDriverWait(driver, .5).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div"))
            )
        sign_in_button.click()

        #Hit the 'no' button to staying signed in
        no_button = WebDriverWait(driver, .9).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[1]"))
            )
        no_button.click()
    
    #Rerun the program if an element isn't found (Bug that sometimes happens)
    except NoSuchElementException:
        print(Fore.RED + "[!]Re-running because an element wasn't found" + Style.RESET_ALL)
        driver.find_element(by=By.XPATH, value=username).clear()
        time.sleep(.5)        
        microsoft_login()
