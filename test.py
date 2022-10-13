from scraper import Scraper
from structure import Structure

scp = Scraper()
stc = Structure()
username = "gildovigor"

scp.acessar_instagram()
scp.logar("_florbelle", "450225zx")
scp.fechar_popups()
scp.maximizar_janela()

scp.acessar_perfil(username)
scp.rolar_para_baixo()

lista_de_views = scp.pegar_views()
lista_de_links = scp.pegar_lista_de_links()
links = stc.criar_links_com_arquivo(username)

sidx = lista_de_links.index(links[0])
lista_de_views = lista_de_views[sidx:sidx+30]


for i in range(len(links)):
    cm_lk = scp.pegar_comentarios_e_likes(links[i])

    comentarios = cm_lk[0]
    likes = cm_lk[1]


    if lista_de_views[i] == '':
        lista_de_views[i] = str(lista_de_views[i-1])

    if likes == 12000 or likes > stc.converter_para_numero(lista_de_views[i]):
        print(f"L: {likes}.")
        likes = stc.converter_para_numero(lista_de_views[i])//3

    stc.escrever_video(username, i, stc.converter_para_numero(lista_de_views[i]), likes)
    stc.escrever_comentarios(username, i, comentarios)