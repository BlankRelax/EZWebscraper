import sys
from time import time
sys.path.append('E:\\Repositories\\EZWebscraper')
print(sys.path)
from selenium.webdriver.common.by import By
from core.engine.base import RPA_BASE
from core.storage.text_file import TextSaver

class MenuBar:

    def __init__(self,driver) -> None:
        self.XPATH="""//*[@id="product-navigation-menu"]/div[2]/ul"""
        self.driver=driver
        
    def element(self):
        element=RPA_BASE.return_element(driver=self.driver,element_id=self.XPATH)
        elements=element.find_elements(By.XPATH,f"""{self.XPATH}/li""" )
        return elements
    
    def click(self,name):
        len_mb=len(self.element())
        for i in range(len_mb):
            bar_elements=self.element()
            if bar_elements[i].text==name:
                bar_elements[i].click()
        return f'{name} clicked !'

class ContentPage:
    def __init__(self,driver) -> None:
        self.XPATH="""//*[@id="main-content"]/div[2]/div/div/div[2]/ul"""
        self.driver=driver
        
    def element(self):
        element=RPA_BASE.return_element(driver=self.driver,element_id=self.XPATH)
        elements=element.find_elements(By.XPATH,f"{self.XPATH}/li" )
        return elements
    
    def get_content_list(self)->int:
        return len(self.element())
    
    def click(self,i:int=0):
        elements=self.element()
        elements[i].click()
        print('clicked')
        return None
    def main_content(self):
        return RPA_BASE.return_element(driver=self.driver,element_id="""//*[@id="main-content"]""").text

def run():
    content=[]
    driver = RPA_BASE.return_driver()
    driver.get(url="https://www.bbc.co.uk/news/uk")
    MenuBar(driver=driver).click('Politics')
    cp=ContentPage(driver=driver)
    for i in range(cp.get_content_list()):
        cp.click(i=i)
        content.append(cp.main_content())
        driver.back()
    return content

if __name__ == "__main__":
    text:list = run()
    TextSaver.to_file(text_list=text, loc='E:\\Repositories\\EZWebscraper\\data', folder_name=str(time()))
