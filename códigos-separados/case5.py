"""def lista_avaliacoes():
    lista_avaliacao = []
    return lista_avaliacao"""



def inserir_avaliacao_cliente():
    nome_cliente = input("Digite o seu nome: ")
    nome_oficina = input("Digite a oficina que você foi atendido(a): ")
    avaliacao = input("De uma nota de 1 a 5 para o atendimento feito: ")
    cpf = input("Digite o seu CPF: ")
    return nome_cliente, nome_oficina, avaliacao, cpf

def append_lista(lista_avaliacao, nome_cliente, nome_oficina, avaliacao, cpf):
    lista_avaliacao.append({
        'nome' : nome_cliente,
        'oficina' : nome_oficina,
        'avaliacao' : avaliacao,
        'cpf' : cpf
        
    })
    print("Avaliacao criado com sucesso")
    return lista_avaliacao
    


def alterar_avaliacao_cliente(lista_avaliacao):
    alterar = input("Para alterar o sua avaliacao, por favor digite o seu CPF:")

    for avaliacao in lista_avaliacao:
        if avaliacao['cpf'] == alterar:
            print("Avaliação encontrada, por favor insira os novos dados caso queira alterar, se não digite o antigo")
            
            novo_nome = input(f"Nome atual ({avaliacao['nome']}): ")
            nova_oficina = input(f"Oficina atual ({avaliacao['oficina']})")
            nova_avaliacao = input(f"Avaliação atual ({avaliacao['avaliacao']})")

            if novo_nome:
                avaliacao['nome'] = novo_nome
            if nova_oficina:
                avaliacao['oficina'] =  nova_oficina
            if nova_avaliacao:
                avaliacao['avaliacao'] = nova_avaliacao

            print("Alterado com sucesso")
            return

        else:
            print("CPF não enconstrado, tente novamente")   
            alterar_avaliacao_cliente(lista_avaliacao) 

def delete_avaliacao(lista_avaliacao):
    delete = input("Para deletar a sua avaliacao, por favor digite o seu CPF:")

    for avaliacao in lista_avaliacao:
        if avaliacao['cpf'] == delete:
            lista_avaliacao.remove(avaliacao)
            print("Avaliação deletada com sucesso")
            return
        else:
            print("Não encontramos seu CPF, tente novamente")
            delete_avaliacao(lista_avaliacao)

def read_avaliacao(lista_avaliacao):
    if not lista_avaliacao:
        print("Nenhuma avaliação encontrada.")
        return
    
    for avaliacao in lista_avaliacao:
        print(f"Nome do Cliente: {avaliacao['nome']}")
        print(f"Nome da Oficina: {avaliacao['oficina']}")
        print(f"Avaliação: {avaliacao['avaliacao']}")
        print(f"CPF: {avaliacao['cpf']}")
            




def validacao_avaliacao(avaliacao):
    if not avaliacao:
        print("A avaliacao está vázia, coloque um número de 1 a 5!!")
        return False
    if not avaliacao < 1 or avaliacao > 5:
        print("Avaliação não permitida, você deve fazer uma validação de 1 a 5")
        return False
    return True

def validacao_nome_oficina(nome_oficina):
    if not nome_oficina:
        print("O nome da oficina está vázia, coloque o nome da oficina que você foi!!")
        return False
    #if not nome_oficina # vou tem que colocar quando fizer a lista das oficinas
        print("Nome de oficina não encontrado, tente novamente colocando um nome correto")
        return False
    return True