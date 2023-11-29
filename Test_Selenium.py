from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import random
import string
import time

# Function to perform the login test for an unregistered user
def test_login_unregistered_user_001():
    # Set up Chrome WebDriver
    driver = webdriver.Chrome()

    # Open the website for user registration
    driver.get("https://web-demo.qahive.com/e-commerce/register")

    # Find email and password input fields, and submit button
    email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//body/div[@id='root']/main[1]/div[1]/div[1]/form[1]/div[1]/input[1]")))
    password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//body/div[@id='root']/main[1]/div[1]/div[1]/form[1]/div[2]/input[1]")))
    submit_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'submit')]")))

    # Input email and password for unregistered user
    email_input.send_keys("teeza@gmail.com")
    password_input.send_keys("secret_sauce")

    # Click the submit button
    submit_button.click()

    # Wait for the "Unauthorized" message
    unauthorized_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Unauthorized')]")))

    # Check if the unauthorized message is visible
    if unauthorized_message.is_displayed():
        print("\033[92mtest_login_unregistered_user_001 - PASSED: Unregistered user can't log in\033[0m")
    else:
        print("\033[91mtest_login_unregistered_user_001 - FAILED: Unregistered user can log in\033[0m")
        # Capture screenshot on failure
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        screenshot_name = f"test_login_unregistered_user_001_Failed_{timestamp}.png"
        driver.save_screenshot(screenshot_name)
        print(f"Screenshot captured: {screenshot_name}")

    # Close the browser after test
    driver.quit()

# Function to perform the login test for a registered user
def test_login_registered_user_002():
    # Set up Chrome WebDriver
    driver = webdriver.Chrome()

    # Generate a random password
    password = ''.join(random.choices(string.digits, k=8))

    try:
        # Open the website for user registration
        driver.get("https://web-demo.qahive.com/e-commerce/register")
        # Add a short delay to ensure page loading
        time.sleep(1)

        # Click the Register button
        register_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Register')]")))
        register_button.click()

        # Input registration details
        email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//body/div[@id='root']/main[1]/div[1]/div[1]/form[1]/div[1]/input[1]")))
        password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//body/div[@id='root']/main[1]/div[1]/div[1]/form[1]/div[2]/input[1]")))
        username_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//body/div[@id='root']/main[1]/div[1]/div[1]/form[1]/div[3]/input[1]")))
        agree_checkbox = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//body/div[@id='root']/main[1]/div[1]/div[1]/form[1]/div[4]/div[1]/label[1]/input[1]")))

        email_input.send_keys(f"{password}@gmail.com")
        password_input.send_keys("Aaaaaaaa0")
        username_input.send_keys("teeeeeeee")
        agree_checkbox.click()

        # Submit the registration form
        submit_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'submit')]")))
        submit_button.click()

        # Wait for successful registration
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(),'dashboard')]")))
    except Exception as e:
        print(f"\033[91mtest_login_registered_user_002 - FAILED: Error during registration - {e}\033[0m")
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        screenshot_name = f"test_login_registered_user_002_Failed_{timestamp}.png"
        driver.save_screenshot(screenshot_name)
        print(f"Screenshot captured: {screenshot_name}")
    else:
        # Perform login with registered user
        driver.get("https://web-demo.qahive.com/e-commerce/register")

        # Input registered user credentials
        email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//body/div[@id='root']/main[1]/div[1]/div[1]/form[1]/div[1]/input[1]")))
        password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//body/div[@id='root']/main[1]/div[1]/div[1]/form[1]/div[2]/input[1]")))

        email_input.send_keys(f"{password}@gmail.com")
        password_input.send_keys("Aaaaaaaa0")

        # Click the submit button
        submit_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'submit')]")))
        submit_button.click()

        # Wait for successful login
        success_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Login Successful! Redirecting...')]")))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(),'dashboard')]")))

        print("\033[92mtest_login_registered_user_002 - PASSED: Registered user can log in\033[0m")
    finally:
        # Close the browser after test
        driver.quit()

# Run the test cases
test_login_unregistered_user_001()
test_login_registered_user_002()
