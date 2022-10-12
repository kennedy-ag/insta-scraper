import os

class Structure():
    def __init__(self):
        self.path = "./arquivos"

    def criar_pasta_do_usuario(self, username: str):
        if not os.path.isdir(f'./arquivos/{username}'): 
            os.mkdir(f'./arquivos/{username}')

    def converter_para_numero(self, numero: str) -> int:
        if len(numero.split(' '))>1:
            numero = numero[0]
        if '\n' in numero:
            numero = numero.split('\n')[0]
        if numero[-1] == 'K':
            if '.' not in numero:
                numero = int(numero[0:-1])*1000
            else:
                numero = int(float(numero[0:-1])*1000)
        elif numero[-1] == 'M':
            if '.' not in numero:
                numero = int(numero[0:-1])*1000000
            else:
                numero = int(float(numero[0:-1])*1000000)
        return numero
    
    def criar_arquivo_com_links(self, username: str, lista_de_links: list):
        with open(f"./arquivos/{username}/links.txt", "a") as arq:
            for i in range(len(lista_de_links)):
                arq.write(f"{username}{i} - {lista_de_links[i]}\n")