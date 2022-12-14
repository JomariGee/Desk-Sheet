#---------------------------------------------------------------
# Automate filling out a Microsoft form for an extra desk shift
#---------------------------------------------------------------
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import colorama, time, os
from colorama import Fore, Back, Style

#Necessary for colorama to work on Windows
colorama.init()
os.system("cls" or "clear")

#Get the time the shift started
shift_start_time = input(Fore.CYAN + "Enter the shifts start time (\"9:00am\"): " +  Style.RESET_ALL)
#Get the time the shift ended
shift_end_time = input(Fore.CYAN + "\nEnter the shifts end time: " + Style.RESET_ALL)
#Get the name for the RA who originally had the shift
original_ra_name = input(Fore.YELLOW + "\nWho's shift was this: " + Style.RESET_ALL)

#Declare Chrome options and install driver if need be
chrome_options = webdriver.ChromeOptions()
#Uncomment below code to keep page open before closing, useful when modifying input
#chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))

#Maximize the browser URL 
driver.get("") #Add
driver.maximize_window()

#Login into Microsoft
def microsoft_login():
    try: 
        time.sleep(1.9) 	
        username = "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]"
        driver.find_element(by=By.XPATH, value=username).send_keys("") #Add

        #Hit the 'next' button
        next_button = WebDriverWait(driver, .9).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div")))
        next_button.click()
        
        #Enter password
        time.sleep(1)
        password = "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input"
        driver.find_element(by=By.XPATH, value=password).send_keys("") #Add
       
        #Hit the 'sign-in' button to staying signed in
        sign_in_button = WebDriverWait(driver, .5).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div")))
        sign_in_button.click()

        #Hit the 'no' button to staying signed in
        no_button = WebDriverWait(driver, .9).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[1]")))
        no_button.click()
    
    #Rerun the program if an element isn't found (Bug that sometimes happens)
    except NoSuchElementException:
        print(Fore.RED + "[!]Re-running because an element wasn't found" + Style.RESET_ALL)
        driver.find_element(by=By.XPATH, value=username).clear()
        time.sleep(.5)        
        microsoft_login()

#Enter extra desk form
def extra_bread():
    try: 
        #Enter my name
        time.sleep(.5) 	
        my_name = "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div[3]/div/div/input"
        driver.find_element(by=By.XPATH, value=my_name).send_keys("") #Add

        #Hit the calendar button, then hit the current date highlighted
        calendar_button_for_current_day = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/button")))
        calendar_button_for_current_day.click()
        current_day = "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div/div/table/tbody/tr[4]/td[3]/div"
        driver.find_element(by=By.XPATH, value=current_day).click()
        
        #Enter the shifts start time
        start_of_shift = "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/div/input"
        driver.find_element(by=By.XPATH, value=start_of_shift).send_keys(shift_start_time)
        
        #Enter the shifts end time
        end_of_shift = "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div/input"
        driver.find_element(by=By.XPATH, value=end_of_shift).send_keys(shift_end_time)

        #Check 'No' for mandatory shift 
        mandatory_checkbox_yes = "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[5]/div/div[3]/div/div[2]/div/label/div"
        driver.find_element(by=By.XPATH, value=mandatory_checkbox_yes).click()
        
        #Enter person's name that shift was shifted with 
        shift_name_switch = "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[6]/div/div[3]/div/div/input"
        driver.find_element(by=By.XPATH, value=shift_name_switch).send_keys(original_ra_name)

        #Click the submit button 
        submit_button = "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/button"
        driver.find_element(by=By.XPATH, value=submit_button).click()
        
        #Close site upon form completion
        driver.quit()
        
    #Rerun the program if an element isn't found (Bug that sometimes happens)
    except NoSuchElementException:
        print(Fore.RED + "[!]Re-running because an element wasn't found" + Style.RESET_ALL)
        driver.find_element(by=By.XPATH, value=my_name).clear()
        driver.find_element(by=By.XPATH, value=start_of_shift).clear()
        driver.find_element(by=By.XPATH, value=end_of_shift).clear()
        driver.find_element(by=By.XPATH, value=shift_name_switch).clear()
        time.sleep(.5)        
        extra_bread()
        
if __name__ =="__main__":
    microsoft_login()
    extra_bread()