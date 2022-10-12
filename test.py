from scraper import Scraper
from structure import Structure

scp = Scraper()
stc = Structure()
usernames = ["joaogomescantor", "gusttavolima", "lucasranngel", "gisele", "bianca", "gildovigor"]

scp.acessar_instagram()
scp.logar("_florbelle", "450225zx")
scp.fechar_popups()
scp.maximizar_janela()

for username in usernames:
    scp.acessar_perfil(username)
    scp.rolar_para_baixo()

    lista_de_links = scp.pegar_lista_de_links()
    lista_de_views = scp.pegar_views()

    if len(lista_de_links) >= 30:
        stc.criar_pasta_do_usuario(username)
        stc.criar_arquivo_com_links(username, lista_de_links[0:30])
    else:
        print(f"{username} tem {len(lista_de_links)} reels")

'''print(lista_de_links)
print("\n\n")
print(lista_de_views)

for link in lista_de_links:
    cm_lk = scp.pegar_comentarios_e_likes(link)
    comentarios = cm_lk[0]
    likes = cm_lk[1]
    print(likes)
    print(comentarios)
    print(len(comentarios))
    break'''