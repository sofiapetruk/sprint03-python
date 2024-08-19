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


#Principal
lista_cadastro = cadastro_lista()
nome, email, senha, telefone = cadastro_perguntas()
usuario_cadastro = fazer_cadastro(nome, email, senha, telefone, lista_cadastro)
print(usuario_cadastro)
email_login, senha_login = login_perguntas()
usuario = fazer_login(email_login, senha_login, usuario_cadastro)
#login = fazer_login(email, senha, usuario_cadastro)
#print(login)
