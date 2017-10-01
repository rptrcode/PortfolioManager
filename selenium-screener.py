from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from bs4 import BeautifulSoup


profile = FirefoxProfile("C:\\Users\\rangaram\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\wlli9t7w.SELENIUM")
browser = webdriver.Firefox(profile)
browser.get("https://www.screener.in/watchlist/")
WebDriverWait(browser, 120).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "table-responsive")))
# table = browser.find_element_by_class_name("table-responsive") 

# print(table.text)

content = browser.page_source

soup = BeautifulSoup(content)
print(soup)

with open("output1.html", "w") as file:
    file.write(str(soup))


data = []
table = soup.find('table', attrs={'class':'table'})
table_body = table.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values

print(data)