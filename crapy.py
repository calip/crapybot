from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import re
import globals

class Crapy:
  def __init__(self, url):
    self.domain = self.get_domain(url)
    self.marketplace = self.get_marketplace()
    self.driver = self.init_driver()
    self.driver.get(url)


  def init_driver(self):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    return driver

  def get_domain(self, url):
    pattern = r"https?://([A-Za-z_0-9.-]+).*"
    match = re.search(pattern, url)
    domain = match.group(1)
    return domain.split("www.")[-1].split("//")[-1].split(".")[0]
  
  def get_marketplace(self):
    if any(ext in self.domain for ext in globals.MARKETPLACES):
      return self.domain
    else:
      return 'Target not found!'

  def get_data(self):
    switcher = {
      'tokopedia' : self.get_tokopedia(),
      'bukalapak' : self.get_bukalapak(),
      'shopee' : self.get_shopee()
    }
    return switcher.get(self.domain, lambda: "Invalid arg")
    
  def get_tokopedia(self):
    soup = BeautifulSoup(self.driver.page_source, 'html.parser')
    self.driver.close()
    title = soup.find('div', id='zeus-header')
    return title.prettify()
  
  def get_bukalapak(self):
    return 'bukalapak'
  
  def get_shopee(self):
    return 'shopee'