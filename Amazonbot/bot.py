import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import os
import time
import json


def clear(): return os.system('cls')


def login():
    global email
    global password
    global which
    while True:
        content = open('u_s.json').read()
        config = json.loads(content)
        email = config['Email']
        password = config['Password']
        if config['Email'] == 'emAilS' and config['Password'] == 'passWorDs':
            clear()
            okay = input('\n  The script is going to ask you to input your amazon email and amazon password,\n  nothing is saved and its just used to login to your amazon account.\n  It will never be seen by anyone but yourself \n\n  If you want to continue enter y if not enter n and the program will close:  ').upper()
            if okay == 'Y':
                clear()
                x = input("Email: ")
                clear()
                i = input('Password: ')

                dictionary = {
                    "Email": x,
                    "Password": i}

                with open("u_s.json", "w") as outfile:
                    json.dump(dictionary, outfile)

                content = open('u_s.json').read()
                config = json.loads(content)
                email = config['Email']
                password = config['Password']

        clear()
        which = input(
            'Do you want Fresh Market or Whole Foods Market Type F for Fresh or W for Whole Foods: ').upper()
        break


# whole foods market
def wf():
    x = random.randint(420, 1980)
    y = random.randint(420, 1980)
    time1 = random.uniform(0.14, 0.261)
    time2 = random.uniform(0.12, 0.216)
    options = Options()
    ua = UserAgent()
    userAgent = ua.random
    print(userAgent)
    options.add_argument(f'user-agent={userAgent}')
    driver = webdriver.Chrome(chrome_options=options,
                              executable_path='chromedriver.exe')
    driver.delete_all_cookies()  # Deletes cookies
    driver.get("https://www.amazon.com/ap/signin?_encoding=UTF8&ignoreAuthState=1&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&switch_account=")

    driver.set_window_size(x, y)

    time.sleep(random.randint(1, 2))
    aemail = driver.find_element_by_name("email")
    for i in email:
        aemail.send_keys(i)
        time.sleep(time1)

    time.sleep(random.randint(1, 2))
    driver.find_element_by_xpath("//*[@id='continue']").click()

    time.sleep(random.randint(1, 2))

    apassword = driver.find_element_by_name("password")
    for i in password:
        apassword.send_keys(i)
        time.sleep(time2)
    time.sleep(random.randint(1, 3))

    driver.find_element_by_xpath("//*[@id='signInSubmit']").click()
    driver.implicitly_wait(1000)

    driver.implicitly_wait(1000)
    driver.get(
        "https://www.amazon.com/gp/cart/view.html?ie=UTF8&ref_=nav_crt_ewc_hd")
    driver.implicitly_wait(1000)
    driver.find_element_by_xpath(
        "//*[@id='sc-alm-buy-box-ptc-button-VUZHIFdob2xlIEZvb2Rz']/span/input").click()
    driver.implicitly_wait(1000)
    driver.find_element_by_xpath(
        "//*[@id='a-autoid-0']/span/a").click()
    driver.implicitly_wait(1000)
    driver.find_element_by_xpath(
        "//*[@id='subsContinueButton']/span/input").click()
    driver.implicitly_wait(1000)
    driver.find_element_by_xpath(
        "//*[@id='changeQuantityFormId']/div[2]/div[2]/div/div/span/span/input").click()

    driver.implicitly_wait(1000)
    driver.find_element_by_xpath(
        "//*[@id='shipoption-select']/div/div/div/div/div[1]/div[3]/div[2]/div/ul/li[2]/span/span/span/button").click()
    driver.implicitly_wait(1000)
    driver.find_element_by_xpath(
        "//*[@id='shipoption-select']/div/div/div/div/div[2]/div[3]/div/span/span/span/input").click()
    driver.implicitly_wait(1000)
    driver.find_element_by_xpath(
        "//*[@id='20200417']/div/div/ul/li/span/span/div/div[2]/span/span/button")
    driver.implicitly_wait(1000)
    while not driver.find_element_by_xpath("//*[@id='shipoption-select']/div/div/div/div/div[2]/div[3]/div/span/span/span/input").click():
        driver.refresh()
        time.sleep(random.randint(20, 30))
    time.sleep(5)
    if not driver.find_element_by_xpath("//*[@id='shipoption-select']/div/div/div/div/div[2]/div[3]/div/span/span/span/input").click():
        driver.close()
        main()

    else:
        driver.find_element_by_xpath(
            "//*[@id='shipoption-select']/div/div/div/div/div[2]/div[3]/div/span/span/span/input").click()


# Fresh market
def f():
    x = random.randint(420, 1980)
    y = random.randint(420, 1980)
    time1 = random.uniform(0.14, 0.261)
    time2 = random.uniform(0.12, 0.216)
    options = Options()
    options.add_experimental_option("detach", True)
    ua = UserAgent()
    userAgent = ua.random
    print(userAgent)
    options.add_argument(f'user-agent={userAgent}')
    driver = webdriver.Chrome(chrome_options=options,
                              executable_path='chromedriver.exe')
    driver.delete_all_cookies()  # Deletes cookies
    driver.get("https://www.amazon.com/ap/signin?_encoding=UTF8&ignoreAuthState=1&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&switch_account=")

    driver.set_window_size(x, y)

    time.sleep(random.randint(1, 2))
    aemail = driver.find_element_by_name("email")
    for i in email:
        aemail.send_keys(i)
        time.sleep(time1)

    time.sleep(random.randint(1, 2))
    driver.find_element_by_xpath("//*[@id='continue']").click()

    time.sleep(random.randint(1, 2))

    apassword = driver.find_element_by_name("password")
    for i in password:
        apassword.send_keys(i)
        time.sleep(time2)
    time.sleep(random.randint(1, 3))

    driver.find_element_by_xpath("//*[@id='signInSubmit']").click()
    driver.implicitly_wait(1000)
    driver.get(
        "https://www.amazon.com/gp/cart/view.html?ie=UTF8&ref_=nav_crt_ewc_hd")

    driver.implicitly_wait(1000)
    driver.find_element_by_xpath(
        "//*[@id='sc-alm-buy-box-ptc-button-QW1hem9uIEZyZXNo']/span/input").click()
    driver.implicitly_wait(1000)
    driver.find_element_by_xpath("//*[@id='a-autoid-0']/span/a").click()
    driver.implicitly_wait(1000)
    driver.find_element_by_xpath(
        "//*[@id='changeQuantityFormId']/div[2]/div[2]/div/div/span/span/input").click()
    driver.implicitly_wait(1000)
    while not driver.find_element_by_xpath("//*[@id='locationChangeWarningStrings']/div[2]/div/div/span[2]/span/input").click():
        driver.refresh()
        time.sleep(random.randint(20, 30))
    time.sleep(5)


def main():
    '''
    Main Function 

    Puts everything together :D

    '''
    clear()  # clears cmd
    login()  # Calls login function

    if which == 'W':  # Whole Foods
        print('Got your email and password all good')
        time.sleep(3)
        clear()
        print('\n'*5)
        print(f'  Your email: {email}')
        print(f'  Your Password: {password}')
        print('\n'*5)
        wf()

    elif which == 'F':
        print('Got your email and password all good')
        time.sleep(3)
        clear()
        print('\n'*5)
        print(f'  Your email: {email}')
        print(f'  Your Password: {password}')
        print('\n'*5)
        f()

    while which != 'W' or which != 'F':
        clear()
        main()


if __name__ == '__main__':
    main()
