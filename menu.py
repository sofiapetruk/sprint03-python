def menu():
    opcao = -1 #para não entrar em outras opções 
    while opcao >= 1 or opcao <= 10:
        print('--------------------------------------------------------------------------------------------------------------------')
        print('[ 1 ] - Por favor, escolha se você deseja fazer o cadastro no nosso aplicativo/site.')
        print('[ 2 ] - Por favor, escolha se você deseja fazer o login no nosso aplicativo/site.')
        print('[ 3 ] - Por favor, descreva qual é o problema que está ocorrendo com o seu veículo.')
        print("[ 4 ] -  Se você deseja adicionar novas possiveis soluções do problema")
        print("[ 5 ] - Por favor, escolha essa opção se você deseja adicionar nova Oficinas no catalago")
        print('[ 6 ] - Por favor, escolha esta opção para descobrir as oficinas disponíveis mais próximas de você.')
        print('[ 7 ] - Avaliação do cliente')
        print('[ 8 ] - Por favor, escolha essa opção se você não conseguiu achar o que queria, iremos mostrar o número do guincho, o seuguro e o bombeiro')
        print('[ 9 ] - Por favor, escolha essa opção se você quer ver as informações da empresa')
        print('[ 10 ]- Por favor, escolha essa opção se você deseja adicionar as caracteristicas do seu carro') 
        print("[ 11 ] - Encerrar o programa")

        try:
            opcao = int(input('Digite uma opção: ')) #usuário irá escolher uma opção do print
            if (opcao < 1) or (opcao > 10): # se o usuário escolhe um opção inválida irá retorna para a pergunta
                print('Opção inválida. Escolha um número do MENU')
            else: 
                return opcao # irá retorna a opção que o usuário escolheu
        except ValueError:
            print('Entrada inválida (somente números) você pode digitar. Por favor, digite um número entre 1 a 9.')    
        except  Exception as e:
            print(f'Ocorreu um erro: {e}')
        
        
#------------------------ Cadastro ----------------------------------------
"""def cadastro_lista(): #criar a lista para guardar as informações do usuário
    print("**- Cadastro lista -**")
    print("------------------------")
    usuario_cadastro = []
    return usuario_cadastro"""
        

def inserir_usuario_cadastro(): #vamos inserir as variáveis para criar o cadastro usuário
    try:
        nome = input("Digite o seu nome: ")
        email = input("Digite o seu email: ")
        senha = input("Digite a sua senha (precisa ser menor do que 8 caracteres): ")
        telefone = input("Digite o seu telefone (ddd + os 9 dígitos): ")
        cpf = input("Digite o seu CPF: ")
        return nome, email, senha, telefone, cpf
    except ValueError as e:
        print(f"Entrada inválida, verifique os dados inseridos: {e}")
        return None, None, None, None, None
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
        return None, None, None, None, None


def fazer_cadastro(nome, email, senha, telefone, cpf, usuario_cadastro):
    valido = True
    if not validacao_nome(nome):  # verifica se a validação das variáveis é falsa
        valido = False
    if not validacao_email(email):
        valido = False
    if not validacao_senha(senha):
        valido = False
    if not validacao_telefone(telefone):
        valido = False
        
    if valido:  # se os dados forem válidos, será cadastrado
        usuario_cadastro.append({
            'nome': nome,
            'email': email,
            'senha': senha,
            'telefone': telefone,
            'cpf': cpf
        })
        print("Cadastro feito com sucesso!") 
    else:
        print("Tente novamente, por favor")
        
    return usuario_cadastro


def alterar_usuario_cadastro(usuario_cadastro): #alterar a informação do usuário caso ele queira por meio do cpf
    alterar = input("Para alterar os dados do seu cadastro, por favor digite o seu CPF:  ")

    for usuario in usuario_cadastro: #o loop está percorrendo cada elemento da lista
        if usuario['cpf'] == alterar: # compara se o cpf é igual ao alterar
            print("Usuário encontrado. Por favor, insira os novos dados caso queira alterar, se não digite o antigo")

            novo_nome = input(f"Nome atual ({usuario['nome']}): ") 
            novo_email = input(f"Email atual ({usuario['email']}): ")
            nova_senha = input(f"Senha atual ({usuario['senha']}): ")
            novo_telefone = input(f"Telefone atual ({usuario['telefone']}): ")

            #ele verifica se tem dados nas variávies, se tiver irá atualizar o dados que foi escrito encima, se o usuário não mudou irá continuar o mesmo
            if novo_nome:
                usuario['nome'] = novo_nome
            if novo_email:
                usuario['email'] = novo_email
            if nova_senha:
                usuario['senha'] = nova_senha
            if novo_telefone:
                usuario['telefone'] = novo_telefone
            
            print("Cadastro alterado com sucesso!")
            return usuario_cadastro
        
    print("CPF não encontrado, tente novamente.") 


def delete_usuario_cadastro(usuario_cadastro): #deletar as o cadastro do usuário
    delete = input("Para deletar o seu cadastro, por favor digite o seu CPF:  ")

    for usuario in usuario_cadastro:
        if usuario['cpf'] == delete:
            usuario_cadastro.remove(usuario)
            print("Usuário deletado com sucesso")
            return usuario_cadastro
        
    print("Não encontramos seu CPF, tente novamente.")  
    return usuario_cadastro


def read__usuario_cadastro(usuario_cadastro): #vai o que foi cadastrado
    if not usuario_cadastro:
        print("Nenhum usuário cadastrado.")
        return

    for usuario in usuario_cadastro:
        print(f"Nome do cliente: {usuario['nome']}")
        print(f"Email: {usuario['email']}")
        print(f"Senha: {usuario['senha']}")
        print(f"Telefone: {usuario['telefone']}")
        print(f"CPF: {usuario['cpf']}")
        print("-"*30)
    


def validacao_nome(nome):
    print("**- Validação nome -**")
    if not nome:
        print("O nome está vazio, coloque o seu nome!!")
        print("------------------------")
        return False
    if not nome.istitle():
        print("Por favor tente novamente, algo deu errado. A primeira letra de cada palavra tem que ser letra maiúscula")
        print("------------------------")
        return False
    return True

def validacao_email(email):
    print("**- Validação email -**")
    if not email:
        print("O email está vazio, coloque o seu email!!")
        print("------------------------")
        return False
    if '@' not in email or '.' not in email: 
        print('Por favor tente novamente, algo deu errado! Seu email pode estar inválido é necessário ter o @gmail.com')
        print("------------------------")
        return False
    return True

def validacao_senha(senha):
    print("**- Validação senha -**")
    if not senha:
        print("A senha está vazia, coloque a sua senha!!")
        print("------------------------")
        return False
    if not len(senha) < 8:
        print('Senha inválida, por favor tente novamente (tem que ser menor que 8 caracteres)')
        print("------------------------")
        return False
    return True

def validacao_telefone(telefone):
    print("**- Validação telefone -**")
    if not telefone:
        print("O telefone está vazio, coloque o seu telefone!!")
        print("------------------------")
        return False
    if not telefone.isdigit() and len(telefone) != 11:
        print('Telefone inválido, por favor tente novamente (ddd + telefone)')
        print("------------------------")
        return False
    return True

def validacao_cpf(cpf): #fazer que o cpf não pode ser da outra pessoa
    print("**- Validação do CPF -**")
    if not cpf:
        print("O CPF está vazio, coloque o seu telefone!!")
        print("------------------------")
    if not cpf.isdigit() and len(cpf) != 11:
        print("O CPF está incorreto, você só deve digitar os 11 números e sem traço")
        print("------------------------")
        return False  
    return True


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
    desc_problema = input("Descreva o problema que está ocorrendo no seu veículo: ").lower()
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
            3. Problemas de sincronização (transmissões manuais) -> Desgaste dos sincronizadores pode dificultar a troca de marchas.
            4. Problemas de solenoides ou válvulas (transmissões automáticas) -> Podem resultar em trocas de marcha irregulares ou falha em  engatar
            as marchas corretas'''
    }
    for palavra, solucao in solucoes.items():
        if palavra in desc_problema:
            return solucao
    return "Não conseguimos identificar, digite novamente, ou peça ajuda a alguém do nosso serviço."

def inserir_descricao_problema(solucoes):
    problema = input("Digite o problema que deseja adicionar: ").lower()
    solucao = input("Digite a solução para o problema: ")
    solucoes[problema] = solucao
    print("Problema e solução adicionados com sucesso.")
    return solucoes

def alterar_descricao_problema(solucoes):
    problema = input("Digite o problema que deseja alterar: ").lower()
    if problema in solucoes:
        nova_solucao = input("Digite a nova solução para o problema: ")
        solucoes[problema] = nova_solucao
        print("Solução alterada com sucesso.")
        return solucoes
    else:
        print("Problema não encontrado.")

def delete_descricao_problema(solucoes):
    problema = input("Digite o problema que deseja deletar: ").lower()
    if problema in solucoes:
        del solucoes[problema]
        print("Solução deletada com sucesso.")
    else:
        print("Problema não encontrado.")

def read_descricao_problema(solucoes, desc_problema):
    if desc_problema in solucoes:
        print(f"Solução: {solucoes[desc_problema]}")
    else:
        print("Problema não encontrado.")

        
#------------------------- Oficinas mais próximas --------------------------------
""""def imprimir_oficinas(lista_oficinas):
    for i, oficina in enumerate(lista_oficinas, 1):
        print(f"[{i}] {oficina}")"""

"""def imprimir_oficinas():
    escolha = -1 #para não entrar em outras opções 
    while escolha < 1 or escolha > 5:
        print('''
        Informações das Oficinas:
        [ 1 ]Zé Oficina está localizada a 1.5km do Centro São Paulo       
        [ 2 ]Auto Car está localizada a 3.0km da Paulista  
        [ 3 ]CARBON AUTO MECANICA está localizada a 4.5km da Castelo Branco 
        [ 4 ]Auto Mecânica Hitoshi está localizada a 3.5km da Vila Mariana  
        [ 5 ]Johny Car está localizada a 2.5km da Madelen
        [ 6 ]Escolha esse opção se você deja adicionar mias oficina''')

        escolha = int(input('Por favor, escolha o número da Oficina mais perto de você: '))
        if (escolha < 1) or (escolha > 5): # se o usuário escolhe um opção inválida irá retorna para a pergunta
            print('Opção inválida, tente novamente')
        else: 
            return escolha # irá retorna a opção que o usuário escolheu"""
        

"""def escolha_usuario(escolha):
    #irá verificar o que o usuário escolhe e da uma dessas opções
    if escolha in [1,2,3,4,5]:
        print('Parabéns pela escolha, o mecânico estará te esperando.')"""



def inserir_oficina():
    try:
        nome = input("Adicionar nome Oficina: ")
        endereco = input("Adicionar endereço da Oficina: ")
        cnpj = input("Digite o CNPJ da sua Oficina: ")
        return nome, endereco, cnpj 
    
    except ValueError as e:
        print(f"Entrada inválida, verifique os dados inseridos: {e}")
        return None, None, None
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
        return None, None, None


def append_lista_oficina(lista_oficina, nome, endereco, cnpj):
    validacao = True

    if not validacao_nome(nome):
        validacao = False
    if not validacao_endereco(endereco):
        validacao = False   
    if not validacao_cnpj(cnpj):
        validacao = False 


    if validacao:
        lista_oficina.append({
        'nome': nome,
        'endereco': endereco,
        'cnpj': cnpj
    })
    print("Oficina cadastrada com sucesso")
    return lista_oficina
    


def alterar_oficina(lista_oficina):
    alterar = input("Para alterar o seu cadastro, por favor digite o seu CNPJ: ")

    for oficina in lista_oficina:
        if oficina['cnpj'] == alterar:
            print("Oficina encontrada, por favor insira os novos dados caso queira alterar, senão, digite os antigos")

            novo_nome = input(f"Nome atual ({oficina['nome']}): ")
            novo_endereco = input(f"Endereço atual ({oficina['endereco']}): ")

            if novo_nome:
                oficina['nome'] = novo_nome
            if novo_endereco:
                oficina['endereco'] = novo_endereco

            print("Oficina alterada com sucesso")
            return lista_oficina  

    print("CNPJ não encontrado, tente novamente.")  
    


def delete_oficina(lista_oficina):
    delete = input("Para deletar o seu cadastro da oficina, por favor digite o seu CNPJ: ")

    for oficina in lista_oficina:
        if oficina['cnpj'] == delete:
            lista_oficina.remove(oficina)
            print("Oficina deletada com sucesso")
            return lista_oficina  

    print("Não encontramos seu CNPJ, tente novamente")  
    

        
            
def read_oficina(lista_oficina):   
    for oficina in lista_oficina:
        print(f"Nome da oficina: {oficina['nome']}  ")    
        print(f"Endereço: {oficina['endereco']}")
        print(f"CNPJ: {oficina['cnpj']}")
        print("-"*30)

def validacao_nome(nome):
    print("**- Validação nome -**")
    if not nome:
        print("O nome está vazio, coloque o seu nome!!")
        print("------------------------")
        return False
    if not nome.istitle():
        print("Por favor tente novamente, algo deu errado. A primeira letra de cada palavra tem que ser letra maiúscula")
        print("------------------------")
        return False
    return True

def validacao_endereco(endereco):
    print("**- Validação do ENDEREÇO -**")
    if not endereco:
        print("O endereço está vazio, coloque o seu endereço!!")
        print("------------------------")
        return False
    return True    


def validacao_cnpj(cnpj): 
    print("**- Validação da CNPJ -**")
    if not cnpj:
        print("O cnpj está vazio, coloque o seu CNPJ!!")
        print("------------------------")
    if not len(cnpj) != 14:
        print("O CNPJ está incorreto, você só deve digitar os 14 números e sem traço")
        print("------------------------")
        return False  
    return True     


   

        

"""def escolher_oficina(lista_oficinas):
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
        return None"""



# ------------------------------ Avaliação Cliente --------------------------
"""def lista_avaliacoes():
    lista_avaliacao = []
    return lista_avaliacao"""



def inserir_avaliacao_cliente():
    nome_cliente = input("Digite o seu nome: ")
    nome_oficina = input("Digite a oficina que você foi atendido(a): ")
    avaliacao = input("De uma nota de 1 a 5 para o atendimento feito: ")
    cpf = input("Digite o seu CPF: ")
    return nome_cliente, nome_oficina, avaliacao, cpf

def append_lista(nome_cliente, nome_oficina, avaliacao, cpf, lista_avaliacao):
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


#------------------------------ Informações ----------------------------------------
def informacoes_empresa():
    print('dfsdfsdfsdfsdfsdfsd')

#-------------------------- Adicionar carro -------------------------------
"""def criar_lista_carro():
    carros = []
    return carros"""

def inserir_carro():
    try:
        marca = input("Digite a MARCA do seu carro: ")
        modelo = input ("Digite o MODELO do seu carro: ")
        ano = int(input("Digite o ano do seu carro: "))
        quilometragem = float(input("Digite a quilometragem do seu carro (km): "))
        placa = input("Digite a sua placa: ")
        return marca, modelo, ano, quilometragem, placa
    
    except ValueError as e:
        print(f"Entrada inválida, verifique os dados inseridos: {e}")
        return None, None, None, None, None
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
        return None, None, None, None, None

def adicionar_carro(marca, modelo, ano, quilometragem, placa, carros):
    carros.append({
            'marca' : marca,
            'modelo' : modelo,
            'ano' : ano,
            'quilometragem' : quilometragem,
            'placa' : placa,
        })
    print("Carro cadastrado com sucesso!")
    
    return carros
        
    

def alterar_carro(carros):
    alterar = input("Para alterar o seu cadastro carro, por favor digite a sua PLACA:")  

    for carro in carros:
        if carro['placa'] == alterar:
            print("Carro encontrado, por favor insira os novos dados caso que ira alterar, se não digite o antigo")

            marca = input(f"Marca atual: ({carro['marca']})")
            modelo = input(f"Modelo atual ({carro['modelo']})")
            ano = int(input(f"Ano atual ({carro['ano']})"))
            km = float(input(f"Quilometragem atual ({carro['quilometragem']})"))
            
            if marca:
                carro['marca'] = marca
            if modelo:
                carro['modelo'] = modelo
            if ano:
                carro['ano'] = ano
            if km:
                carro['quilometragem'] = km

            print("Alterado com sucesso")
            return
        
        
    print("Placa não encontrado, tente novamente.")   
                    

def delete_carro(carros):
    delete = input("Para deletar o seu cadastro carro, por favor digite a sua PLACA:  ")

    for carro in carros:
        if carro['placa'] == delete:
            carros.remove(carro)
            print("Carro deletado com sucesso")
            return
        
    print("Não enconstramos sua PLACA, tente novamente")  
    delete_carro(carros)        

def read_carro(carros):
    for carro in carros:
        print(f"Marca do carro: {carro['marca']}")
        print(f"Modelo do carro: {carro['modelo']}")
        print(f"Ano: {carro['ano']}")
        print(f"Km: {carro['quilometragem']}") 
        print(f"Placa: {carro['placa']}")
        print("-"*30)
    


    

def crud_perguntas(): 
    escolha = -1
    while escolha < 1 or escolha > 4:
        print("---------------------------------------------------------------------")
        print("(1) - Você deseja inserir os dados da opção escolhida?")
        print("(2) - Você quer fazer alguma alteração dos dados?")
        print("(3) - Você deseja deletar o dado")
        print("(4) - Você deseja vizualizar todos os dados cadastrados?")

        try:
            escolha = int(input("Escolha uma opção de 1 a 4: "))
            if (escolha < 1) or (escolha > 4):
                print('Opção inválida. Escolha um número do MENU')
            else: 
                return escolha
        except ValueError:
            print('Entrada inválida (somente números) você pode digitar. Por favor, digite um número entre 1 a 5.') 
        
        





#------------------------ Main ----------------------------
def main():
    usuario_cadastro = []
    lista_oficina = []
    lista_avaliacao = []
    carros = []
    solucoes = {}
    while True:
        opcao = menu()

        if opcao == 1:
            while True:
                escolha = crud_perguntas()

                if  escolha == 1:
                    nome, email, senha, telefone, cpf = inserir_usuario_cadastro()
                    if nome and email and senha and telefone and cpf:
                        usuario_cadastro = fazer_cadastro(nome, email, senha, telefone, cpf,  usuario_cadastro)    
                elif  escolha == 2:
                    usuario_cadastro = alterar_usuario_cadastro(usuario_cadastro)
                elif  escolha == 3:
                    usuario_cadastro = delete_usuario_cadastro(usuario_cadastro)
                elif  escolha == 4:
                    read__usuario_cadastro(usuario_cadastro) 
                
                crud_refazer = input("Deseja continuar a fazer o CRUD? (s/n)").lower() 
                if crud_refazer == "s":
                    continue
                else:
                    opcao = menu()    
                    break    
            
        elif opcao == 2:
            email_login, senha_login = login_perguntas()
            fazer_login(email_login, senha_login, usuario_cadastro)                 
            
        elif opcao == 3:
            desc_problema = descricao_problema()
            print(possivel_solucao(desc_problema))

        elif opcao == 4:
            while True:
                escolha = crud_perguntas()
                if escolha == 1:
                    solucoes = inserir_descricao_problema(solucoes)
                elif escolha == 2:
                    alterar_descricao_problema(solucoes)
                elif escolha == 3:
                    delete_descricao_problema(solucoes)
                elif escolha == 4:
                    read_descricao_problema(solucoes, desc_problema)  

        elif opcao == 5:
            while True:
                escolha = crud_perguntas()

                if escolha == 1:
                    nome, endereco, cnpj = inserir_oficina()
                    if nome and endereco and cnpj:
                        lista_oficina = append_lista_oficina(nome, endereco, cnpj, lista_oficina)
                elif escolha == 2:
                    lista_oficina = alterar_oficina(lista_oficina)
                elif escolha == 3:    
                    lista_oficina = delete_oficina(lista_oficina)
                elif escolha == 4:
                    read_oficina(lista_oficina)

                crud_refazer = input("Deseja continuar a fazer o CRUD? (s/n)").lower() 
                if crud_refazer == "s":
                    continue
                else:
                    opcao = menu()    
                    break    
            
                

        elif opcao == 6:
            escolher_oficina(lista_oficina)    
            

        elif opcao == 7:
            while True:
                escolha = crud_perguntas()

                if escolha == 1:
                    nome_cliente, nome_oficina, avaliacao, cpf =inserir_avaliacao_cliente()
                    lista_avaliacao = append_lista(lista_avaliacao, nome_cliente, nome_oficina, avaliacao, cpf)
                    
                elif escolha == 2:
                    lista_avaliacao = alterar_avaliacao_cliente(lista_avaliacao)

                elif escolha == 3:
                    lista_avaliacao = delete_avaliacao(lista_avaliacao)

                elif escolha == 4:    
                    lista_avaliacao = read_avaliacao(lista_avaliacao)

                crud_refazer = input("Deseja continuar a fazer o CRUD? (s/n)").lower() 
                if crud_refazer == "s":
                    continue
                else:
                    opcao = menu()    
                    break   
            


        elif opcao == 8:
            ligar_seguro, ligar_bombeiro, ligar_guincho = servixo_extra()
            servico_print(ligar_seguro, ligar_bombeiro, ligar_guincho)
            

        elif opcao == 9:
            informacoes_empresa()
            
        elif opcao == 10:
            while True:
                escolha = crud_perguntas()

                if escolha == 1:
                    marca, modelo, ano, quilometragem, placa = inserir_carro()
                    if marca and modelo and ano and quilometragem and placa:
                        carros = adicionar_carro(marca, modelo, ano, quilometragem, placa, carros)

                elif escolha == 2:
                    carros = alterar_carro(carros)

                elif escolha == 3:
                    carros = delete_carro(carros)

                elif escolha == 4:
                    read_carro(carros)

                crud_refazer = input("Deseja continuar a fazer o CRUD? (s/n)").lower() 
                if crud_refazer == "s":
                    continue
                else:
                    opcao = menu()    
                    break  
                
        refazer = input("Deseja continuar? (s/n)").lower()
        if refazer != "s":
            print("Muito Obrigado")
            break

        elif opcao == 11:
            print("Fim do Programa")
            break


        

#Principal 
main()