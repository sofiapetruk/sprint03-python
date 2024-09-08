def oficinas_disponiveis():
    lista_oficina = {"nome": "Zé Oficina", "distância em km": 1.5, "referencia": "Centro São Paulo",
                    "nome": "Auto Car", "distância em km": 3.0, "referencia": "Paulista ",
                    "nome": "Carbon Auto Mecanica", "distância em km": 4.5, "referencia": "Castelo Branco",
                    "nome": "Auto Mecânica Hitoshi", "distância em km": 3.5, "referencia": "Vila Mariana",
                    "nome": "Johny Car", "distância em km": 2.5, "referencia": "Vila Madelena"
                    }   
    return lista_oficina 

def imprmir_oficina(lista_oficina):
    for i, j, k in lista_oficina.keys():
        print(f'O {i} da oficina é: {lista_oficina[i]} a {j} é de: {lista_oficina[j]} e a {k} do lugar: {lista_oficina[k]}')


lista_oficina = oficinas_disponiveis()
imprmir_oficina(lista_oficina)