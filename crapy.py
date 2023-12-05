from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import re

class Crapy:
  def __init__(self, url):
    self.driver = self.init_driver()
    self.driver.get(url)
    self.domain = self.get_domain(url)

  def init_driver(self):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    return driver

  def get_domain(self, url):
    pattern = r"(?P<domain>[\w\-]+\.+[\w\-]+)"
    match = re.search(pattern, url)
    domain = match.group("domain")
    return domain

  def get_data(self):
    soup = BeautifulSoup(self.driver.page_source, 'html.parser')
    self.driver.close()
    title = soup.find('div', id='zeus-header')
    return title.prettify()