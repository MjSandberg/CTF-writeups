from selenium import webdriver

whole = ""
browser = webdriver.Chrome('C:\webdriver\chromedriver.exe')
browser.get("http://hax.allesctf.net:5000/")


elem = browser.find_element_by_name("circuit")
elem.send_keys("- H U1 H D\nX H U2 H D")            # Deutsch Algo
elem2 = browser.find_element_by_class_name("ui button")
elem2.click()

for i in range(0,200):
    browser.delete_all_cookies()
    browser.add_cookie({'domain': 'hax.allesctf.net',
      'httpOnly': False,
      'name': 'randomness',
      'path': '/',
      'secure': False,
      'value': str(i)})
    browser.refresh()


    string = browser.find_element_by_css_selector("body").text
    whole += string[0]
print(whole)
browser.quit()


whole[::-1]
