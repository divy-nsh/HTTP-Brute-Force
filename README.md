# Brute-Force Login Script with CSRF Token Bypass (Conceptual)

**Disclaimer:**

* This script is intended for educational and research purposes only.
* **Never use this script for unauthorized activities.**
* **Always obtain proper authorization before performing any security testing.**
* **Use this script responsibly and ethically.**

**Requirements:**

* **Python 3:** Ensure you have Python 3 installed on your system. You can download it from https://www.python.org/downloads/
* **Selenium WebDriver:** This script uses Selenium WebDriver to interact with the browser. You'll need to install the WebDriver for your desired browser (e.g., ChromeDriver for Chrome, GeckoDriver for Firefox). Refer to the Selenium documentation for installation instructions: https://www.selenium.dev/documentation/webdriver/

**Installation:**

1. Install the required libraries using pip:

   ```bash
   pip install selenium

Download and install the appropriate WebDriver for your desired browser (if not already installed).

**Usage:**

```Bash

python Http-Brute.py -u <target_url> --uid <username_xpath> --pid <password_xpath> --sid <submit_xpath> --user <username_file> --pass <password_file> --change <check_for_302_redirect>
```
**Arguments:**

* `-u, --url:` Target URL of the login page. (Required)
* `--uid, --username_xpath:` XPath of the username/email input field. (Required)
* `--pid, --password_xpath:` XPath of the password input field. (Required)
* `--sid, --submit_xpath:`XPath of the login button or submit element. (Required)
* `--user, --username_file:` Path to the file containing usernames (one username per line). (Required)
* `--pass, --password_file:` Path to the file containing passwords (one password per line). (Required)
* `--change, <check_for_302_redirect>:` Set to "Y" (case-insensitive) to check for a 302 redirect (indicating successful login) after attempting login credentials.

**Note:**

Replace <your_script_name.py> with the actual filename of your script.
Ensure the provided XPaths accurately target the username, password, and submit elements on the login page.
The script attempts login with each username-password combination from the provided files.

**How it Works:**

1. Parses arguments: Reads command-line arguments using argparse.
2. Loads usernames and passwords: Reads usernames from the provided file and loads passwords from the file.
3. Attempts login: Iterates through each username-password combination, attempts to log in using Selenium, and checks for successful login based on the presence of a specific element (customizable) or a 302 redirect (if --change is set to "Y").
4. Checks for success:
   * Checks for HTTP 302 redirects (if applicable).
   * Checks for the presence of a specific element on the successful login page (customizable).
5. Handles exceptions: Includes error handling for common issues like WebDriverException, TimeoutException, and other exceptions.
6. Exits on success: Exits the script immediately after the first successful login attempt.

**Disclaimer:**

This script is provided as-is and without any warranty. The author is not responsible for any misuse or damage caused by this script.

**Additional Notes:**

This script provides a basic example of brute-force login using Selenium. You may need to modify it based on the specific characteristics of the target website.
Brute-force attacks can be time-consuming and resource-intensive. Consider alternative security testing methods for more efficient vulnerability identification.
Always use this script responsibly and ethically.


**Example:**

```Bash

python Http-Brute.py -u [https://www.example.com/login](https://www.example.com/login) -u "//input[@id='username']" -p "//input[@id='password']" -s "//button[@type='submit']" -user usernames.txt -pass passwords.txt --change Y
```
This example command attempts to brute-force login on the target URL "https://www.example.com/login" using usernames from "usernames.txt" and passwords from "passwords.txt". It checks for a 302 redirect after each login attempt.
