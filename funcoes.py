def gera_contato(nome, telefone, email, favorito):
    return {"nome": nome, "telefone": telefone, "email": email, "favorito": favorito}

def imprime_contato(contato):
    favorito = "☆" if contato["favorito"] else " "
    nome = contato["nome"]
    telefone = contato["telefone"]
    email = contato["email"]

    return (f"[{favorito}] {nome} - {telefone} - {email}")

#("1 - Adicionar contato")
def adicionar_contato(agenda, contato):
    agenda.append(contato)
    print(f"Contato adicionado: \n{contato}")
    return

#("2 - Visualizar lista de contatos")
def visualizar_contatos(agenda):
    print( f"Indice / Favorito / Nome / Telefone / Email")
    for indice, registro in enumerate(agenda, start=1):
        contato = imprime_contato(registro)
        print( f"{indice}. {contato}")
    return

#("3 - Editar contato")
def alterar_contato(agenda, indice, contato):
    agenda[indice]["nome"] = contato["nome"]
    agenda[indice]["telefone"] = contato["telefone"]
    agenda[indice]["email"] = contato["email"]
    agenda[indice]["favorito"] = contato["favorito"]
        
    print("\nContato alterado:")
    print( f"{indice}. {imprime_contato(agenda[indice])}")
    return

#("4 - Marcar/desmarcar como favorito")
def favoritar(agenda,indice):
    if agenda[indice]["favorito"]:
        agenda[indice]["favorito"] = False
    else:
        agenda[indice]["favorito"] = True
    
    print("\nContrato alterado:")
    print( f"{indice}. {imprime_contato(agenda[indice])}")

#("5 - Ver lista de contatos favoritos")
def listar_favoritos(agenda):
    print( f"Indice / Favorito / Nome / Telefone / Email")
    for indice, registro in enumerate(agenda, start=1):
        if registro["favorito"]: 
            contato = imprime_contato(registro)
            print( f"{indice}. {contato}")
    return

#("6 - Apagar contato")
def apagar_contato(agenda, indice):
    agenda.remove(agenda[indice])
    print("Contato removido")
    return