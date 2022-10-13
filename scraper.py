from selenium import webdriver
from selenium.webdriver.common.by import By
from xpath import *
import time

class Scraper:
    def __init__(self):
        self.navegador = webdriver.Chrome("chromedriver.exe")

    def acessar_instagram(self):
        self.navegador.get("https://instagram.com/")
        time.sleep(2)

    def logar(self, usuario: str, senha: str):
        input_usuario = self.navegador.find_element(By.XPATH, INPUT_USUARIO_XPATH)
        input_usuario.click()
        input_usuario.send_keys(usuario)

        input_senha = self.navegador.find_element(By.XPATH, INPUT_SENHA_XPATH)
        input_senha.click()
        input_senha.send_keys(senha)

        botao_login = self.navegador.find_element(By.XPATH, BOTAO_LOGIN_XPATH)
        botao_login.click()
        time.sleep(15)
    
    def fechar_popups(self):
        self.navegador.find_element(By.XPATH, AGORA_NAO_XPATH).click()
        time.sleep(4)
        self.navegador.find_element(By.XPATH, AGORA_NAO_POPUP_XPATH).click()

    def maximizar_janela(self):
        self.navegador.maximize_window()

    def acessar_perfil(self, usuario: str):
        self.navegador.get("https://instagram.com/"+usuario+"/reels")
        time.sleep(5)

    def rolar_para_baixo(self):
        self.navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    def pegar_lista_de_links(self) -> list:
        elements = self.navegador.find_elements(By.XPATH, VIDEO_XPATH)
        links = [e.get_attribute("href") for e in elements if "/reel/" in e.get_attribute("href")]
        return links

    def pegar_views(self):
        return [i.text for i in self.navegador.find_elements(By.XPATH, VIEWS_XPATH)]

    def pegar_comentarios_e_likes(self, url: str):
        self.navegador.get(url)
        self.navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        comments = [c.text for c in self.navegador.find_elements(By.XPATH, COMMENT_XPATH)]

        if len(comments)<15:
            comments.extend(comments)
            comments.extend(comments[0:10])
        else:
            comments.extend(comments)

        try:
            likes_str = self.navegador.find_element(By.XPATH, LIKES_XPATH)
            likes_str = likes_str.text
            likes = ""
            for i in likes_str:
                if i.isdigit():
                    likes += i
            if likes == '':
                likes = '12000'
        except:
            likes = '12000'
        return (comments, int(likes))