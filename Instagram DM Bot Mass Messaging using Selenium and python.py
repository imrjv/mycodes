from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random


driver = webdriver.Chrome()

# Redirecting to instagram login page
driver.get("https://www.instagram.com/")

# Account Credentials
username = 'randomAutomation351'
password = '123@456@789'

addresses = ['_rjvra_', 'harshil_1502_hp', '_rjvra_', 'harshil_1502_hp', '_rjvra_', 'harshil_1502_hp', '_rjvra_', 'harshil_1502_hp']
messages = ['This is the first message', 'This is the second message', 'This is the third message', 'This is the fourth message', 'This is the fifth message', 'This is the sixth message']

def loginIntoInstagram(username, password):
    try:
        # Delay time between events
        time.sleep(random.randrange(2, 5))

        # Get username with the element name
        inputUsername = driver.find_element(By.NAME, 'username')

        # Get password with the element name
        inputPassword = driver.find_element(By.NAME, 'password')

        # Input the username
        inputUsername.send_keys(username)

        # Delay time between the events
        time.sleep(random.randrange(2, 5))

        # Input the password
        inputPassword.send_keys(password)

        # Delay time between the events
        time.sleep(random.randrange(1, 4))

        # Send the credentials by pressing Enter key
        inputPassword.send_keys(Keys.ENTER)

        # Wait time to load the page
        driver.implicitly_wait(20)

    except Exception as err:
        print(err)


def sendingMessages(addresses):

    # Click on the message button
    messageButton = driver.find_element(By.CSS_SELECTOR, '#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg.KtFt3 > div > div:nth-child(2) > a')
    messageButton.click()

    # Delay time between the events
    time.sleep(random.randrange(1, 3))

    driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[3]/button[2]').click()

    # Delay time between the events
    time.sleep(random.randrange(2, 5))

    # Click on the send message button
    driver.find_element(By.XPATH, '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button').click()

    # Loop through the address
    for address in addresses:
        # Get the search area and input the value from the address array
        newAddress = driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input')
        newAddress.send_keys(address)

        # Select the user from the list
        driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div').click()
        # Delay time between the events
        time.sleep(random.randrange(3, 5))

        # Click on the next element
        driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[1]/div/div[2]/div/button').click()
        time.sleep(random.randrange(1, 7))

        # Get the text area
        textarea = driver.find_element(By.XPATH, '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
        time.sleep(random.randrange(1, 5))

        # Input the random value from the messages list
        textarea.send_keys(random.choice(messages))
        time.sleep(random.randrange(3, 8))

        # Press the Enter key
        textarea.send_keys(Keys.ENTER)
        time.sleep(random.randrange(1, 7))

        # Click on new message icon
        driver.find_element(By.XPATH, '/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()

        # Wait time
        driver.implicitly_wait(10)


loginIntoInstagram(username, password)

sendingMessages(addresses)

# Quit the browser
driver.quit()





