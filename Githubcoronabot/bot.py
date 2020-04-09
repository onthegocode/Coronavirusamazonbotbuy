import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import time


def main():
    while True:
        okay = input('Going to ask you to input your amazon email and amazon password, nothing will be saved and its just used to login to  your amazon account. If this is okay type y if no type n and the program will close').upper()
        if okay == 'Y':
            email = input('Type your amazon email: ')
            password = input('Type your amazon password: ')
            x = random.randint(420, 1980)
            y = random.randint(420, 1980)
            time1 = random.uniform(0.18, 0.421)
            time2 = random.uniform(0.12, 0.321)
            options = Options()
            ua = UserAgent()
            userAgent = ua.random
            print(userAgent)
            options.add_argument(f'user-agent={userAgent}')
            driver = webdriver.Chrome(chrome_options=options,
                                      executable_path='chromedriver.exe')
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

            while not driver.find_element_by_xpath("//*[@id='shipoption-select']/div/div/div/div/div[2]/div[3]/div/span/span/span/input").click():
                driver.refresh()
                time.sleep(random.randint(20,30))
            if not driver.find_element_by_xpath("//*[@id='shipoption-select']/div/div/div/div/div[2]/div[3]/div/span/span/span/input").click():
                driver.close()
                main()

            else:
                driver.find_element_by_xpath(
                    "//*[@id='shipoption-select']/div/div/div/div/div[2]/div[3]/div/span/span/span/input").click()
        else:
            break


main()
