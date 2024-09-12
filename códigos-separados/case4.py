def escolher_oficina(lista_oficinas):
    busca = input("Digite o nome ou parte do nome da oficina que deseja encontrar: ")
    resultados = []
    for oficina in lista_oficinas:
        if busca.lower() in oficina.nome.lower():
            resultados.append(oficina)

    if resultados:
        for i, oficina in enumerate(resultados, 1):
            print(f"[{i}] {oficina}")
        escolha = int(input("Escolha a oficina pelo número: ")) - 1
        return resultados[escolha]
    else:
        print("Nenhuma oficina encontrada.")
        return None

def imprimir_oficinas(lista_oficinas):
    for i, oficina in enumerate(lista_oficinas, 1):
        print(f"[{i}] {oficina}")

def inserir_oficina(lista_oficinas):
    nome = input("Adicionar nome da Oficina: ")
    endereco = input("Adicionar endereço da Oficina: ")
    cnpj = input("Digite o CNPJ da sua Oficina: ")

    # Validar o CNPJ aqui

    nova_oficina = Oficina(nome, endereco, cnpj)
    lista_oficinas.append(nova_oficina)

def alterar_oficina(lista_oficinas):
    alterar = input("Para alterar o seu cadastro, por favor digite o seu CNPJ: ")

    for oficina in lista_oficinas:
        if oficina.cnpj == alterar:
            novo_nome = input(f"Nome atual ({oficina.nome}): ")
            novo_endereco = input(f"Endereço atual ({oficina.endereco}): ")

            if novo_nome:
                oficina.nome = novo_nome
            if novo_endereco:
                oficina.endereco = novo_endereco
            print("Oficina alterada com sucesso")
            return

    print("CNPJ não encontrado.")

def delete_oficina(lista_oficinas):
    delete = input("Para deletar o seu cadastro da oficina, por favor digite o seu CNPJ: ")

    for i, oficina in enumerate(lista_oficinas):
        if oficina.cnpj == delete:
            lista_oficinas.remove(lista_oficinas)
            print("Oficina deletada com sucesso")
            return

    print("Não encontramos seu CNPJ.")

def read_oficina(lista_oficinas):
    for oficina in lista_oficinas:
        print(oficina)

# Exemplo de uso
lista_oficinas = []

inserir_oficina(lista_oficinas)
inserir_oficina(lista_oficinas)

imprimir_oficinas(lista_oficinas)

alterar_oficina(lista_oficinas)

delete_oficina(lista_oficinas)

imprimir_oficinas(lista_oficinas)