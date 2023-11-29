from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import random
import string
import time

# Login_001
def test_login_unregistered_user_001():
    driver = webdriver.Chrome()

    driver.get("https://web-demo.qahive.com/e-commerce/register")

    email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//body/div[@id='root']/main[1]/div[1]/div[1]/form[1]/div[1]/input[1]")))
    password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//body/div[@id='root']/main[1]/div[1]/div[1]/form[1]/div[2]/input[1]")))
    submit_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'submit')]")))

    email_input.send_keys("teeza@gmail.com")
    password_input.send_keys("secret_sauce")

    submit_button.click()

    unauthorized_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Unauthorized')]")))

    if unauthorized_message.is_displayed():
        print("\033[92mtest_login_unregistered_user_001 - PASSED: Unregistered user can't log in\033[0m")
    else:
        print("\033[91mtest_login_unregistered_user_001 - FAILED: Unregistered user can log in\033[0m")
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        screenshot_name = f"test_login_unregistered_user_001_Failed_{timestamp}.png"
        driver.save_screenshot(screenshot_name)
        print(f"Screenshot captured: {screenshot_name}")

    driver.quit()

# Login_002
def test_login_registered_user_002():
    driver = webdriver.Chrome()

    password = ''.join(random.choices(string.digits, k=8))

    try:
        driver.get("https://web-demo.qahive.com/e-commerce/register")
        time.sleep(1)

        register_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Register')]")))
        register_button.click()

        email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//body/div[@id='root']/main[1]/div[1]/div[1]/form[1]/div[1]/input[1]")))
        password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//body/div[@id='root']/main[1]/div[1]/div[1]/form[1]/div[2]/input[1]")))
        username_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//body/div[@id='root']/main[1]/div[1]/div[1]/form[1]/div[3]/input[1]")))
        agree_checkbox = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//body/div[@id='root']/main[1]/div[1]/div[1]/form[1]/div[4]/div[1]/label[1]/input[1]")))

        email_input.send_keys(f"{password}@gmail.com")
        password_input.send_keys("Aaaaaaaa0")
        username_input.send_keys("teeeeeeee")
        agree_checkbox.click()

        submit_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'submit')]")))
        submit_button.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(),'dashboard')]")))
    except Exception as e:
        print(f"\033[91mtest_login_registered_user_002 - FAILED: Error during registration - {e}\033[0m")
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        screenshot_name = f"test_login_registered_user_002_Failed_{timestamp}.png"
        driver.save_screenshot(screenshot_name)
        print(f"Screenshot captured: {screenshot_name}")
    else:
        driver.get("https://web-demo.qahive.com/e-commerce/register")

        email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//body/div[@id='root']/main[1]/div[1]/div[1]/form[1]/div[1]/input[1]")))
        password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//body/div[@id='root']/main[1]/div[1]/div[1]/form[1]/div[2]/input[1]")))

        email_input.send_keys(f"{password}@gmail.com")
        password_input.send_keys("Aaaaaaaa0")

        submit_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'submit')]")))
        submit_button.click()

        success_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Login Successful! Redirecting...')]")))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(),'dashboard')]")))

        print("\033[92mtest_login_registered_user_002 - PASSED: Registered user can log in\033[0m")
    finally:
        driver.quit()

# Login_003
def test_login_only_email_003():
    driver = webdriver.Chrome()

    try:
        driver.get("https://web-demo.qahive.com/e-commerce/register")


        email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//body/div[@id='root']/main[1]/div[1]/div[1]/form[1]/div[1]/input[1]")))
        email_input.send_keys("teeza@gmail.com")

        submit_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'submit')]")))
        submit_button.click()

        error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Please provide all values!')]")))
        print("\033[92mtest_login_only_email_003 - PASSED: User can't login with only email input\033[0m")
    except Exception as e:
        print(f"\033[91mtest_login_only_email_003 - FAILED: Error occurred - {e}\033[0m")
    finally:
        driver.quit()

# Login_004  
def test_login_only_password_004():
    driver = webdriver.Chrome()

    try:
        driver.get("https://web-demo.qahive.com/e-commerce/register")

        password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//body/div[@id='root']/main[1]/div[1]/div[1]/form[1]/div[2]/input[1]")))
        password_input.send_keys("secret_sauce")

        submit_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'submit')]")))
        submit_button.click()

        error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Please provide all values!')]")))
        print("\033[92mtest_login_only_password_004 - PASSED: User can't login with only password input\033[0m")
    except Exception as e:
        print(f"\033[91mtest_login_only_password_004 - FAILED: Error occurred - {e}\033[0m")
    finally:
        driver.quit()

# Login_005
def test_login_without_input_005():
    driver = webdriver.Chrome()

    try:
        driver.get("https://web-demo.qahive.com/e-commerce/register")

        submit_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'submit')]")))
        submit_button.click()

        error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Please provide all values!')]")))
        print("\033[92mtest_login_without_input_005 - PASSED: User can't login without inputting anything\033[0m")
    except Exception as e:
        print(f"\033[91mtest_login_without_input_005 - FAILED: Error occurred - {e}\033[0m")
    finally:
        driver.quit()

# Login_006
def test_register_button_006():
    driver = webdriver.Chrome()

    try:
        driver.get("https://web-demo.qahive.com/e-commerce/register")
        time.sleep(1)

        register_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Register')]")))
        register_button.click()

        radio_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//body/div[@id='root']/main[1]/div[1]/div[1]/form[1]/div[4]/div[1]/label[1]/input[1]")))
        print("\033[92mtest_register_button_006 - PASSED: Register button works\033[0m")
    except Exception as e:
        print(f"\033[91mtest_register_button_006 - FAILED: Error occurred - {e}\033[0m")
    finally:
        driver.quit()

# Login_007
def test_short_password_007():
    driver = webdriver.Chrome()

    try:
        driver.get("https://web-demo.qahive.com/e-commerce/register")
        
        email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//body/div[@id='root']/main[1]/div[1]/div[1]/form[1]/div[1]/input[1]")))
        password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//body/div[@id='root']/main[1]/div[1]/div[1]/form[1]/div[2]/input[1]")))
        submit_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'submit')]")))
        
        email_input.send_keys("Teeraza003@gmail.com")
        password_input.send_keys("teera")
        submit_button.click()

        error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Password must contain at least one uppercase lette')]")))
        print("\033[92mtest_short_password_007 - PASSED: Password shorter than 8 characters not allowed\033[0m")
    except Exception as e:
        print(f"\033[91mtest_short_password_007 - FAILED: Error occurred - {e}\033[0m")
    finally:
        driver.quit()

# Login_008
def test_no_uppercase_password_008():
    driver = webdriver.Chrome()

    try:
        driver.get("https://web-demo.qahive.com/e-commerce/register")
        
        email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//body/div[@id='root']/main[1]/div[1]/div[1]/form[1]/div[1]/input[1]")))
        password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//body/div[@id='root']/main[1]/div[1]/div[1]/form[1]/div[2]/input[1]")))
        submit_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'submit')]")))
        
        email_input.send_keys("Teeraza003@gmail.com")
        password_input.send_keys("teera")
        submit_button.click()

        error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Password must contain at least one uppercase lette')]")))
        print("\033[92mtest_no_uppercase_password_008 - PASSED: Password without uppercase letter not allowed\033[0m")
    except Exception as e:
        print(f"\033[91mtest_no_uppercase_password_008 - FAILED: Error occurred - {e}\033[0m")
    finally:
        driver.quit()

# Login_009
def test_no_number_password_009():
    driver = webdriver.Chrome()

    try:
        driver.get("https://web-demo.qahive.com/e-commerce/register")
        
        email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//body/div[@id='root']/main[1]/div[1]/div[1]/form[1]/div[1]/input[1]")))
        password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//body/div[@id='root']/main[1]/div[1]/div[1]/form[1]/div[2]/input[1]")))
        submit_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'submit')]")))
        
        email_input.send_keys("Teeraza003@gmail.com")
        password_input.send_keys("teera")
        submit_button.click()

        error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Password must contain at least one number')]")))
        print("\033[92mtest_no_number_password_009 - PASSED: Password without a number not allowed\033[0m")
    except Exception as e:
        print(f"\033[91mtest_no_number_password_009 - FAILED: Error occurred - {e}\033[0m")
    finally:
        driver.quit()


# Run the test cases
test_login_unregistered_user_001()
test_login_registered_user_002()
test_login_only_email_003()
test_login_only_password_004()
test_login_without_input_005()
test_register_button_006()
test_short_password_007()
test_no_uppercase_password_008()
test_no_number_password_009()