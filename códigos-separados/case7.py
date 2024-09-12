def inserir_avaliacao_cliente():
    while True:
        nome_cliente = input("Digite o seu nome: ")
        nome_oficina = input("Digite a oficina que você foi atendido(a): ")
        if not validacao_nome_oficina(nome_oficina):
            continue
        avaliacao = int(input("Dê uma nota de 1 a 5 para o atendimento feito: "))
        if not validacao_avaliacao(avaliacao):
            continue
        cpf = input("Digite o seu CPF: ")
        return nome_cliente, nome_oficina, avaliacao, cpf

def append_lista(lista_avaliacao, nome_cliente, nome_oficina, avaliacao, cpf):
    lista_avaliacao.append({
        'nome': nome_cliente,
        'oficina': nome_oficina,
        'avaliacao': avaliacao,
        'cpf': cpf
    })
    print("Avaliação criada com sucesso")
    return lista_avaliacao

def alterar_avaliacao_cliente(lista_avaliacao):
    alterar = input("Para alterar sua avaliação, por favor digite o seu CPF:")

    for avaliacao in lista_avaliacao:
        if avaliacao['cpf'] == alterar:
            print("Avaliação encontrada, por favor insira os novos dados caso queira alterar, se não, digite o antigo")
            
            novo_nome = input(f"Nome atual ({avaliacao['nome']}): ")
            nova_oficina = input(f"Oficina atual ({avaliacao['oficina']}): ")
            if not validacao_nome_oficina(nova_oficina):
                nova_oficina = avaliacao['oficina']  # Mantém o antigo se a validação falhar
            nova_avaliacao = int(input(f"Avaliação atual ({avaliacao['avaliacao']}): "))
            if not validacao_avaliacao(nova_avaliacao):
                nova_avaliacao = avaliacao['avaliacao']  # Mantém o antigo se a validação falhar

            if novo_nome:
                avaliacao['nome'] = novo_nome
            if nova_oficina:
                avaliacao['oficina'] = nova_oficina
            if nova_avaliacao:
                avaliacao['avaliacao'] = nova_avaliacao

            print("Avaliação alterada com sucesso")
            return lista_avaliacao

    print("CPF não encontrado, tente novamente.")
    return lista_avaliacao

def delete_avaliacao(lista_avaliacao):
    delete = input("Para deletar a sua avaliação, por favor digite o seu CPF:")

    for avaliacao in lista_avaliacao:
        if avaliacao['cpf'] == delete:
            lista_avaliacao.remove(avaliacao)
            print("Avaliação deletada com sucesso")
            return lista_avaliacao

    print("CPF não encontrado, tente novamente.")
    return lista_avaliacao

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
    if avaliacao < 1 or avaliacao > 5:
        print("Avaliação não permitida. Você deve dar uma nota de 1 a 5.")
        return False
    return True

def validacao_nome_oficina(nome_oficina):
    if not nome_oficina:
        print("O nome da oficina está vazio. Por favor, coloque o nome da oficina que você foi.")
        return False
    # Exemplo de validação adicional:
    # if nome_oficina not in lista_de_oficinas:  # lista_de_oficinas seria uma lista previamente definida com os nomes válidos
    #     print("Nome de oficina não encontrado, tente novamente colocando um nome correto")
    #     return False
    return True

# Exemplo de uso das funções:
def main():
    lista_avaliacoes = []

    while True:
        print("\n1. Inserir Avaliação")
        print("2. Alterar Avaliação")
        print("3. Deletar Avaliação")
        print("4. Listar Avaliações")
        print("5. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            nome_cliente, nome_oficina, avaliacao, cpf = inserir_avaliacao_cliente()
            lista_avaliacoes = append_lista(lista_avaliacoes, nome_cliente, nome_oficina, avaliacao, cpf)
        elif opcao == 2:
            lista_avaliacoes = alterar_avaliacao_cliente(lista_avaliacoes)
        elif opcao == 3:
            lista_avaliacoes = delete_avaliacao(lista_avaliacoes)
        elif opcao == 4:
            read_avaliacao(lista_avaliacoes)
        elif opcao == 5:
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chama a função principal
main()
