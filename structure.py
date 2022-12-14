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

    def criar_links_com_arquivo(self, username: str) -> list:
        with open(f"./arquivos/{username}/links.txt", 'r') as arquivo:
            return self.tratar_lista_gerada(arquivo.readlines())

    def tratar_lista_gerada(self, lista: list):
        lista_temp = [i.strip() for i in lista]
        return [i.split(' - ')[1] for i in lista_temp]

    def escrever_video(self, username: str, numero: int, views: int, likes: int):
        with open(f"./arquivos/{username}/videos/{username}__{numero}.txt", 'a') as arquivo:
            arquivo.write(f"{views}\n{likes}")

    def escrever_comentarios(self, username: str, numero: int,  comentarios: list):
        for i in range(len(comentarios)):
            arquivo = open(f"./arquivos/{username}/comentarios/{username}__{numero}__{i}.txt", 'w', encoding="utf-8")
            arquivo.write(comentarios[i])
            arquivo.close()