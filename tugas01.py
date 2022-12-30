from selenium import webdriver

driver = webdriver.Chrome()
websites = ['https://tiket.com/', 'https://www.tokopedia.com/', 'https://www.orangsiber.com/', 'https://demoqa.com/', 'https://automatetheboringstuff.com/']
name = ['tiket.com', 'tokopedia.com', 'orangsiber.com', 'demoqa.com', 'automatetheboringstuff.com']

for (x,y) in zip (websites,name):
    driver.get(x)
    print(y + ' - ' + driver.title)  
