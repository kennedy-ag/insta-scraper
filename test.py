from scraper import Scraper
from structure import Structure

scp = Scraper()
stc = Structure()
username = "anitta"

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


for link in links:
    cm_lk = scp.pegar_comentarios_e_likes(link)
    comentarios = cm_lk[0]
    likes = cm_lk[1]
    print(comentarios)
    print(len(comentarios))
    print(likes)
    break