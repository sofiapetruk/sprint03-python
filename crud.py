def inserir_descricao_problema(solucoes):
    problema = input("Digite o problema que deseja adicionar: ").lower()
    solucao = input("Digite a solução para o problema: ")
    print("Problema e solução adicionados com sucesso.")
    return problema, solucao

def append_solucao(problema, solucao, solucoes):
    solucoes.append({
        'problema': problema,
        'solucao': solucao,
    })
    print("Solução criada com sucesso")
    return solucoes

def alterar_descricao_problema(solucoes):
    problema_busca = input("Digite o problema que deseja alterar: ").lower()

    for item in solucoes:

        if item['problema'] == problema_busca:
            nova_solucao = input("Digite a nova solução para o problema: ")

            if nova_solucao:
                item['solucao'] = nova_solucao
                print("Solução alterada com sucesso.")
                
            return solucoes

    print("Problema não encontrado.")   
    return solucoes

def delete_descricao_problema(solucoes):
    problema_busca = input("Digite o problema que deseja deletar: ").lower()

    for item in solucoes:

        if item['problema'] == problema_busca:

            solucoes.remove(item)
            print("Solução deletada com sucesso.")
            return solucoes
    
    print("Problema não encontrado.")    
    return solucoes

def read_descricao_problema(solucoes):
    if not solucoes:  # Verifica se a lista está vazia
        print("Nenhum problema cadastrado.")
        return
    
    for item in solucoes:
        print(f"Problema: {item['problema']}")
        print(f"Solução: {item['solucao']}")
