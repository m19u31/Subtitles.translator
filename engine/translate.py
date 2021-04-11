import time;
from engine.browser import *;

class Translate (Browser):
	def __init__(self, socks5=None):
		super().__init__(socks5=socks5);
	def traduzir(self, palavras):
		print("Traduzindo: ");
		pagina = "https://translate.google.com/#view=home&op=translate&sl=en&tl=pt";
		self.driver.get(pagina);
		time.sleep(1);
		self.driver.find_element_by_xpath("//textarea").clear();
		#while (self.driver.find_element_by_xpath('//span[@jsname="txFAF"]/span').text != "")):
		time.sleep(2);
		self.driver.find_element_by_xpath("//textarea").send_keys(palavras);
		#while self.driver.find_element_by_xpath('//span[@jsname="txFAF"]/span').text==""):
		time.sleep(2);
		return self.driver.find_element_by_xpath('//span[@jsname="txFAF"]/span').text;
