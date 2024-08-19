# print('[ 4 ] - Avaliação do cliente')
#Talvez colocar para printar como foi feita a avaliação, para fica constatado no site
def pergunta_avaliacao_cliente():
    nome_cliente = input("Digite o seu nome: ")
    nome_oficina = input("Digite a oficina que você foi atendido(a): ")
    avaliacao = input("De uma nota de 1 a 5 para o atendimento feito: ")
    return nome_cliente, nome_oficina, avaliacao

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