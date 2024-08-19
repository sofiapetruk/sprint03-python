#print('[ 2 ] - Por favor, descreva qual é o problema que está ocorrendo com o seu veículo.')
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

#Principal
desc_problema = descricao_problema()
print(possivel_solucao(desc_problema))