from selenium import webdriver

chrome_driver_path = r'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.python.org/')
data = driver.find_element(by='xpath', value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul')

news_list = data.text.split('\n')

event_dict = dict()
i = 0
while i < len(news_list) - 1:
    event_dict[f'{news_list[i]}'] = news_list[i + 1]
    i += 2

print(event_dict)

driver.quit()