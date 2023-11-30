from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class Crapy:
  def __init__(self, url):
    options = Options()
    options.add_argument('--headless')
    self.driver = webdriver.Firefox(options=options)
    self.driver.get(url)

  def get_data(self):
    soup = BeautifulSoup(self.driver.page_source, 'html.parser')
    self.driver.close()
    title = soup.find('div', id='zeus-header')
    return title.prettify()

