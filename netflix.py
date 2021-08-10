
from contextlib import contextmanager
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of

print("#made by rykerdz\n")
first_string = input("Entry is 'email:password:new_password'   : ")
my_list = first_string.split(":")

@contextmanager
def wait_for_page_load(driver, timeout=30):
    old_page = driver.find_element_by_tag_name('html')
    yield
    WebDriverWait(driver, timeout).until(staleness_of(old_page))
 
 
def main():
 
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://www.netflix.com/password")
    try:
        elem = driver.find_element_by_name("userLoginId")
    except NoSuchElementException:
        elem = driver.find_element_by_name("email")
    elem.send_keys(my_list[0])
    elem = driver.find_element_by_name("password")
    elem.send_keys(my_list[1])
    elem.send_keys(Keys.RETURN)
    with wait_for_page_load(driver):
        pass
    # driver.get("https://www.netflix.com/password")
    # driver.get("https://www.netflix.com/password")

    elem = driver.find_element_by_name("currentPassword")
    elem.send_keys(my_list[1])
    elem = driver.find_element_by_name("newPassword")
    elem.send_keys(my_list[2])
    elem = driver.find_element_by_name("confirmNewPassword")
    elem.send_keys(my_list[2])
    elem = driver.find_element_by_id("btn-save")
    elem.click()
    with wait_for_page_load(driver):
        pass

    print("#\n#\n#\nsuccessfully changed the password of ' " + my_list[0] + " ' to : "+ my_list[2]+"\n\n")
    sleep(5)
 
 
if __name__ == '__main__':
    main()