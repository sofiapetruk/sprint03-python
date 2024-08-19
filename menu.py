def menu():
    opcao = -1 #para não entrar em outras opções 
    while opcao < 1 or opcao > 7:
        print('--------------------------------------------------------------------------------------------------------------------')
        print('[ 1 ] - Por favor, escolha se você deseja fazer o cadastro no nosso aplicativo/site.')
        print('[ 2 ] - Por favor, escolha se você deseja fazer o login no nosso aplicativo/site.')
        print('[ 3 ] - Por favor, descreva qual é o problema que está ocorrendo com o seu veículo.')
        print('[ 4 ] - Por favor, escolha esta opção para descobrir as oficinas disponíveis mais próximas de você.')
        print('[ 5 ] - Avaliação do cliente')
        print('[ 6 ] - Por favor, escolha essa opção se você não conseguiu achar o que queria, iremos mostrar o número do guincho, o seuguro e o bombeiro')
        print('[ 7 ]- Sair do Programa')
        opcao = int(input('Digite uma opção: ')) #usuário irá escolher uma opção do print
        if (opcao < 1) or (opcao > 5): # se o usuário escolhe um opção inválida irá retorna para a pergunta
            print('Opção inválida')
        else: 
            return opcao # irá retorna a opção que o usuário escolheu
        
#------------------------ Cadastro ----------------------------------------
def cadastro_lista(): #criar a lista para guardar as informações do usuário
    print("**- Cadastro lista -**")
    print("------------------------")
    usuario_cadastro = []
    return usuario_cadastro

def cadastro_perguntas():
    nome = input("Digite o seu nome: ")
    email = input("Digite o seu email: ")
    senha = input("Digite o sua senha (somente número de 0 ao 9, e até 8 dígitos): ")
    telefone = input("Digite a sua senha (ddd + os 9 dígitos): ")
    return nome, email, senha, telefone

def validacao_nome(nome):
    print("**- Validação nome -**")
    if not nome:
        print("O nome está vázio, coloque o seu nome!!")
        print("------------------------")
        return False
    if not nome.istitle():
        print("Por favor tente novamente, algo deu errado. A primeira letra de cada nome tem que ser letra maiúscula")
        print("------------------------")
        return False
    return True

def validacao_email(email):
    print("**- Validação email -**")
    if not email:
        print("O email está vázio, coloque o seu email!!")
        print("------------------------")
        return False
    if '@' not in email or '.' not in email: #verificação do email
        print('Por favor tente novamente, algo deu errado! Seu email pode estar inválido é necessário ter o @gmail.com')
        print("------------------------")
        return False
    return True

def validacao_senha(senha):
    print("**- Validação senha -**")
    if not senha:
        print("A senha está vázia, coloque a sua senha!!")
        print("------------------------")
        return False
    if not senha.isdigit() or len(senha) > 8:
        print('Senha inválida, por favor tente novamente')
        print("------------------------")
        return False
    return True

def validacao_telefone(telefone):
    print("**- Validação telefone -**")
    if not telefone:
        print("O telefone está vázio, coloque o seu telefone!!")
        print("------------------------")
        return False
    if not telefone.isdigit() and len(telefone) != 11:
        print('Telefone inválido, por favor tente novamente')
        print("------------------------")
        return False
    return True


def fazer_cadastro(nome, email, senha, telefone, usuario_cadastro):
    while True:
        valido = True
        if not validacao_nome(nome):
            valido = False
        if not validacao_email(email):
            valido = False
        if not validacao_senha(senha):
            valido = False
        if not validacao_telefone(telefone):
            valido = False
        
        if valido:
            usuario_cadastro.append({
                'nome': nome,
                'email': email,
                'senha': senha,
                'telefone': telefone
            })
            print("Cadastro feito com sucesso!") # Mensagem de sucesso
            break # sair do loop se tudo estiver de acordo com as validações
        else:
            print("Tente novamente, por favor")
            nome, email, senha, telefone = cadastro_perguntas() # Repetir perguntas
    return usuario_cadastro

# ----------------- Login ---------------------------------------

def login_perguntas():
    email_login = input("Digite o seu email: ")
    senha_login = input("Digite a sua senha: ")

    return email_login, senha_login

def fazer_login(email_login, senha_login, usuario_cadastro):
    for usuario in usuario_cadastro:

        if usuario['email'] == email_login and usuario['senha'] == senha_login:
            print("Parabéns, acesso concedido")
            return usuario
        else:
            print('Email ou senha incorretos, por favor tente novamente ou faça o cadastro caso não houver.') 
            email_login, senha_login = login_perguntas()

# --------------------- Problema do veículo ----------------------------------
def descricao_problema():
    desc_problema = input("Descreva o problema que está acorrendo no seu veículo: ").lower()
    return desc_problema

def possivel_solucao(desc_problema):
    solucoes = {
        "morrendo": '''
            Possíveis problemas:
            1. Problemas de ignição -> Problemas nas velas de ignição, cabos ou bobina de ignição podem causar falhas no funcionamento do motor.
            2. Filtro de combustível sujo -> Um filtro de combustível obstruído pode restringir o fluxo de combustível para o motor.
            3. Problemas de Motor -> Questões internas do motor, como problemas de sincronização, sensores de posição defeituosos ou problemas 
            de compressão, podem levar a uma operação.
            4. Falha no sistema elétrico -> Problemas com a bateria, alternador ou sistema de distribuição elétrica podem levar o motor a morrer.
            5. Problemas no sistema de injeção de combustível -> Falhas nos injetores de combustível ou no regulador de pressão de combustível 
            podem causar interrupções no fornecimento de combustível ao motor.''',

        "barulho": '''
            Possíveis problemas:
            1. Problemas nos freios -> Pastilhas de freio desgastadas, discos de freio empenados ou pinças de freio travadas podem causar 
            barulhos durante a frenagem.
            2. Problemas no motor -> Componentes internos do motor desgastados, como pistões, bielas ou válvulas, podem gerar batidas, 
            cliques ou outros ruídos anormais.
            3. Problemas de transmissão -> Desgaste das engrenagens, falta de fluido ou problemas de sincronização podem causar ruídos de 
            trituração, zumbidos ou rangidos.
            4. Problemas nos rolamentos das rodas -> Rolamentos desgastados ou danificados podem produzir ruídos de rotação ou rangidos ao dirigir.''',

        "pneu": '''
            Possíveis problemas:
            1. Furos ou perfurações -> Pneus podem ficar perfurados por pregos, parafusos  ou objetos afiados na estrada, resultando em 
            vazamentos de ar e possíveis avarias.
            2. Desgaste irregular -> O desgaste irregular dos pneus pode ser causado por problemas de alinhamento,  balanceamento inadequado, 
            suspensão desgastada ou condução agressiva.
            3. Pneus carecas -> Se os pneus estiverem muito desgastados e a profundidade da banda de  rodagem estiver abaixo do limite legal, 
            os pneus podem se tornar carecas.''',
    
        "transmissão": '''
            Possíveis problemas:
            1. Danos mecânicos -> Danos nos componentes internos da transmissão, como engrenagens, sincronizadores ou embreagens, podem levar a 
            problemas de funcionamento, como dificuldade em engatar as marchas, ruídos anormais ou a perda total da transmissão.
            2. Vazamento de fluido de transmissão -> Um vazamento de fluido de transmissão pode resultar em níveis insuficientes de lubrificação, 
            levando a danos nos componentes da transmissão e a mau funcionamento.
            3. Problemas de sincronização (transmissões manuais) -> Desgaste dos sincronizadores pode dificultar a troca de marchas.')
            4. Problemas de solenoides ou válvulas (transmissões automáticas) -> Podem resultar em trocas de marcha irregulares ou falha em  engatar
            as marchas corretas'''
    }
    for palavra, solucao in solucoes.items():
        if palavra in desc_problema:
            return solucao
    return "Não conseguimos identificar, digite novamente, ou pessa ajuda alguém do nosso servirço"

#------------------------- Oficinas mais próximas --------------------------------
"""def oficinas_disponiveis():
    lista_oficina = {"nome": "Zé Oficina", "distância em km": 1.5, "referencia": "Centro São Paulo",
                    "nome": "Auto Car", "distância em km": 3.0, "referencia": "Paulista ",
                    "nome": "Carbon Auto Mecanica", "distância em km": 4.5, "referencia": "Castelo Branco",
                    "nome": "Auto Mecânica Hitoshi", "distância em km": 3.5, "referencia": "Vila Mariana",
                    "nome": "Johny Car", "distância em km": 2.5, "referencia": "Vila Madelena"
                    }   
    return lista_oficina
[ 2 ] está localizada a 3.0km da Paulista  """
def imprimir_oficinas():
    escolha = -1 #para não entrar em outras opções 
    while escolha < 1 or escolha > 5:
        print('''
        Informações das Oficinas:
        [ 1 ]Zé Oficina está localizada a 1.5km do Centro São Paulo       
        [ 2 ]Auto Car está localizada a 3.0km da Paulista  
        [ 3 ]CARBON AUTO MECANICA está localizada a 4.5km da Castelo Branco 
        [ 4 ]Auto Mecânica Hitoshi está localizada a 3.5km da Vila Mariana  
        [ 5 ]Johny Car está localizada a 2.5km da Madelen''')

        escolha = int(input('Por favor, escolha o número da Oficina mais perto de você: '))
        if (escolha < 1) or (escolha > 5): # se o usuário escolhe um opção inválida irá retorna para a pergunta
            print('Opção inválida, tente novamente')
        else: 
            return escolha # irá retorna a opção que o usuário escolheu

def escolha_usuario(escolha):
    #irá verificar o que o usuário escolhe e da uma dessas opções
    if escolha in [1,2,3,4,5]:
        print('Parabéns pela escolha, o mecânico estará te esperando.')


# ------------------------------ Avaliação Cliente --------------------------
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

#-------------------------- Serviço Extra --------------------------
def servixo_extra():
    ligar_seguro = '(11) 4395-8860'
    ligar_bombeiro = '193'
    ligar_guincho = '(11) 3337-6786'
    return ligar_seguro, ligar_bombeiro, ligar_guincho

def servico_print(ligar_seguro, ligar_bombeiro, ligar_guincho):
    print(f'A seguir o número do Seguro da Porto: {ligar_seguro}')
    print(f'A seguir o número do bombeiro: {ligar_bombeiro}')
    print(f'A seguir o número do guincho da Porto Seguro: {ligar_guincho}')


#------------------------ Main ----------------------------
def main(opcao):
    match opcao:
        case 1:
            lista_cadastro = cadastro_lista()
            nome, email, senha, telefone = cadastro_perguntas()
            usuario_cadastro = fazer_cadastro(nome, email, senha, telefone, lista_cadastro)
        case 2:
            email_login, senha_login = login_perguntas()
            usuario = fazer_login(email_login, senha_login, usuario_cadastro)
        case 3:
            desc_problema = descricao_problema()
            print(possivel_solucao(desc_problema))
        case 4:
            print('fgvrg')
        case 5:
            nome_cliente, nome_oficina, avaliacao = pergunta_avaliacao_cliente
        case 6:
            ligar_seguro, ligar_bombeiro, ligar_guincho = servixo_extra()
            servico = servico_print(ligar_seguro, ligar_bombeiro, ligar_guincho)
        case 7:
            print('Programa encerrado') #encerra o programa


#Principal 
opcao = -1
while opcao != 7:
    opcao = menu()
    result = main(opcao)