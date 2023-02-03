from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd

image_list=[]
Title_list=[]
author_list=[]
date_published=[]  #not available at site
desc_list=[]
subhead_list=[]
books_list=[]

browser=webdriver.Chrome(ChromeDriverManager().install())
for page_number in range (0,15):
    browser.get(f"https://www.buchhandel.de/fachzeitschriften?page={page_number}&pageSize=100")
    ##browser.find_element(By.CSS_SELECTOR,".header_nav-main .nav-pills li #ember358").click()  ### no need to click the button , we can access the page directly from full link
    browser.implicitly_wait(7)


    image=browser.find_elements(By.CSS_SELECTOR,".table_logentries tbody .table_row td:nth-of-type(1) div img")
    browser.implicitly_wait(10)
    Title=browser.find_elements(By.CSS_SELECTOR,".table_logentries tbody .table_row td:nth-of-type(3) p:first-of-type span:first-of-type")
    browser.implicitly_wait(10)
    author=browser.find_elements(By.CSS_SELECTOR,".table_logentries tbody .table_row td:nth-of-type(3) p:nth-of-type(2)")
    browser.implicitly_wait(10)
    desc=browser.find_elements(By.CSS_SELECTOR,".table_logentries tbody .table_row td:nth-of-type(3) p:first-of-type span:nth-of-type(2)")
    browser.implicitly_wait(10)
    subhead=browser.find_elements(By.CSS_SELECTOR,".table_logentries tbody .table_row td:nth-of-type(3) p:first-of-type span:last-of-type")
    browser.implicitly_wait(10)
    print(len(Title))
    print(len(subhead))
    print(type(Title[0]))
    print(Title[10].text)

    for td in range(0,len(Title)):
        image_list.append(image[td].get_attribute('src'))
        browser.implicitly_wait(3)
        Title_list.append(Title[td].text)
        browser.implicitly_wait(3)
        author_list.append(author[td].text)
        browser.implicitly_wait(3)
        desc_list.append(desc[td].text)
        browser.implicitly_wait(3)
        subhead_list.append(subhead[td].text)
        browser.implicitly_wait(3)
        books_list.append([image_list[td],Title_list[td],author_list[td],desc_list[td],subhead_list[td]])

    df=pd.DataFrame(books_list,columns=['image URL','Title','Author','Description','Subhead description'])
    df.to_csv('books.csv')
    ##print(books_list)
    ##print(subhead_list)    
    ##print(Title_list)
    ##print(desc_list)


