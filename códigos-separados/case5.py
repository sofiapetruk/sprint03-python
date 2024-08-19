#Opção 7 - caso de errado em todos as opções, escolha esse opção para te mostrar para qual número ligar para o Seguro da porto, chamar o guincho ou chamar o bombeiro
def servixo_extra():
    ligar_seguro = '(11) 4395-8860'
    ligar_bombeiro = '193'
    ligar_guincho = '(11) 3337-6786'
    return ligar_seguro, ligar_bombeiro, ligar_guincho

def servico_print(ligar_seguro, ligar_bombeiro, ligar_guincho):
    print(f'A seguir o número do Seguro da Porto: {ligar_seguro}')
    print(f'A seguir o número do bombeiro: {ligar_bombeiro}')
    print(f'A seguir o número do guincho da Porto Seguro: {ligar_guincho}')

#Principal
ligar_seguro, ligar_bombeiro, ligar_guincho = servixo_extra()
servico = servico_print(ligar_seguro, ligar_bombeiro, ligar_guincho)