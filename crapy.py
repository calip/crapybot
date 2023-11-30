from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class Crapy:
  def __init__(self):
    options = Options()
    options.add_argument('--headless')
    self.driver = webdriver.Firefox(options=options)

  def get_data(self, url):
    soup = BeautifulSoup(url.page_source, 'html.parser')
    self.driver.close()
    title = soup.find('div', id='zeus-header')
    return title.prettify()

