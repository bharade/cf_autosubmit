import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def script():
    if len(sys.argv) != 4:
        print("Usage: python script.py <contest_number> <Quesn> <file name>")
        return

    contest_number = sys.argv[1]
    Quesn = sys.argv[2]
    file = sys.argv[3]
    website = f"https://codeforces.com/contest/{contest_number}/problem/{Quesn}"
    path = r'C:\Users\Asus\Desktop\Codeforces\chromedriver.exe'
    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service)
    driver.get(website)

    enter_button = driver.find_element(By.LINK_TEXT, "Enter")
    enter_button.click()

    username_box = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "handleOrEmail")))
    password_box = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "password")))
    username_box.send_keys("your_username")
    password_box.send_keys("password")

    login_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']")))
    login_button.click()

    file_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))
    file_input.clear()
    #adjust the folder accordingly
    file_input.send_keys(r"C:\Users\Asus\Desktop\Codeforces\{}.cpp".format(file))  # Replace with the actual file path

    
    
    submit_button = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH,'//input[@value="Submit"]')))
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)
    submit_button.click()
    WebDriverWait(driver, 4).until(EC.url_contains("/contest/"))

    time.sleep(5)
    driver.refresh()
    
    table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//table[@class='status-frame-datatable']")))
    first_row = table.find_element(By.XPATH, ".//tr[2]")
    verdict = first_row.find_element(By.XPATH, ".//td[6]")
    verdict_text = verdict.text
    print("Verdict:", verdict_text)
    time.sleep(5)
    driver.quit()

script()
