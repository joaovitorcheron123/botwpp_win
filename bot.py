from selenium import webdriver
import time

class WppBot:
    def __init__(self):
        self.msg = "Olá, essa é uma mensagem de teste https://www.youtube.com/watch?v=BHACKCNDMW8"
        self.grupos = ["Teste 1","Amigos do João"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviaMsg(self):
        #<span dir="auto" title="Amigos do João" class="_19RFN _1ovWX _F7Vk">Amigos do João</span>
        #<div tabindex="-1" class="_13mgZ">
        #<span data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)

        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('_13mgZ')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.msg)
            botao_enviar = self.driver.find_element_by_xpath('//span[@data-icon="send"]')
            time.sleep(3)
            botao_enviar.click()
            time.sleep(3)

bot = WppBot()
bot.EnviaMsg()