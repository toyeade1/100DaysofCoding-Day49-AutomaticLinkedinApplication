from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
import time


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
path = '/Users/a/Library/Mobile Documents/com~apple~CloudDocs/Development/chromedriver'
driver = webdriver.Chrome(executable_path=path, options=options)
URL = 'https://www.linkedin.com/jobs/search/?currentJobId=3324610716&f_AL=true&f_E=2%2C3&f_PP=106224388&f_TPR' \
      '=r2592000&f_WT=2&geoId=103644278&keywords=python%20developer&location=United%20States&refresh=true&sortBy=R '
driver.get(URL)

signin = driver.find_element('xpath', '/html/body/div[3]/a[1]')
time.sleep(3)
signin.click()
time.sleep(2)
username = driver.find_element('id', 'username')
username.send_keys(os.environ['username'])
password = driver.find_element('id', 'password')
password.send_keys(os.environ['password'])
login = driver.find_element('xpath', '//*[@id="organic-div"]/form/div[3]/button')
login.click()
time.sleep(3)

job_list = driver.find_elements('class name', 'jobs-search-results__list-item')

for jobs in job_list:
    print(f'loading job:\n {jobs.text}')
    jobs.click()
    time.sleep(4)

    # Try and apply for the job and check if it is a one-step apply option.
    try:
        easy_apply = driver.find_element('class name',
                                         'jobs-apply-button')
        easy_apply.click()
        time.sleep(2)

        # Check to see if it is a multistep application.
        submit_button = driver.find_element('xpath',
                                            '/html/body/div[3]/div/div/div[2]/div/div/form/footer/div[3]/button')

        next_button = driver.find_element('class name',
                                          'artdeco-button__text')

        print(f'THIS IS THE NEXT BUTTON -> {next_button}')

        if next_button.text == 'Next':
            time.sleep(2)
            close_button = driver.find_element('xpath', '/html/body/div[3]/div/div/button')
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element('xpath', '/html/body/div[3]/div[2]/div/div[3]/button[1]')
            discard_button.click()
            print('Complex Application. Application Skipped...')
            continue
        else:
            submit_button.click()
            print('Application Submitted')

        time.sleep(2)
        close_button = driver.find_element('xpath', '/html/body/div[3]/div/div/button')
        close_button.click()

    except NoSuchElementException:
        print('No Easy Apply Button Found. Application Skipped...')
        continue

# This would be to fill out an application for one job with complex questions:

# cont = driver.find_element('css selector', '.mt5 > div > div > div > button')
# cont.click()
# time.sleep(2)
# driver.find_element('css selector', '.jobs-easy-apply-content > div > form > footer > div > button').click()
# time.sleep(1)
# driver.find_element('xpath', '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]').click()
# time.sleep(1)
# review_app = driver.find_element('xpath', '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]').click()
# time.sleep(1)
# submit_app = driver.find_element('xpath', '/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[3]/button[2]')
# submit_app.click()
# print('Application Submitted')

driver.quit()
