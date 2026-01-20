from pathlib import Path
import formatacao
import json

movimentos = Path(r'Controle Financeiro\Controle-Financeiro-CLI\movimentos.json')

def checar_arquivo():
    if not movimentos.exists():
        movimentos.write_text('[]', encoding='utf-8')   


def ler_dados():
    checar_arquivo()
    return json.loads(movimentos.read_text(encoding='utf-8')) 


def salvar_dados(dados):
    movimentos.write_text(
        json.dumps(dados, indent=2, ensure_ascii=False),
        encoding='utf-8'
    )


   
def adicionar_movimento(data, descricao, valor, tipo):
    checar_arquivo()

    descricao = descricao.strip().lower()
    tipo = tipo.strip().lower()
    
    # Le a lista atual JSON
    dados = json.loads(movimentos.read_text(encoding='utf-8'))

    # gera um novo ID
    novo_id = 1
    if len(dados) > 0:
        maior = 0
        for l in dados:
            if int(l['id']) > maior:
                maior = int(l['id'])
            novo_id = maior + 1

    # Criar transação
    transacao = {
        'id': novo_id,
        'data': data,
        'descricao': descricao,
        'valor': float(valor),
        'tipo': tipo
    }

    # Adiciono transação a lista
    dados.append(transacao)

    movimentos.write_text(json.dumps(dados, indent=2, ensure_ascii=False), encoding='utf-8')



def listar_movimento():
    checar_arquivo()
    formatacao.cabeçalho('Movimentos')
    dados = ler_dados()

    print(f'{'ID':<6} {'DATA':<11} {'DESCRIÇÃO':<20} {'VALOR':>12} {'TIPO':>7}')
    for l in dados:
        id_atual = l['id']
        data = l['data']
        descricao = l['descricao']
        valor = float(l['valor'])
        valor_formatado = (f'R$ {valor:.2f}')
        tipo = l['tipo']

        
        print(f'{id_atual:<6} {data:<11} {descricao:<20} {valor_formatado:>12} {tipo:>7}')

    

def calcular_saldo():
    
    return total_entradas() - total_saidas()    

    

def total_entradas():
    
    entradas = 0.0

    dados = ler_dados()

    for l in dados:
        valor = float(l['valor'])
        tipo = l['tipo'].strip().lower()
        if tipo == 'entrada':
            entradas += valor

    return entradas

    
def total_saidas():
    
    saidas = 0.0

    dados = ler_dados()

    for l in dados:
        valor = float(l['valor'])
        tipo = l['tipo'].strip().lower()
        if tipo == 'saida':
            saidas += valor

    return saidas
        


def resumo_financeiro():

    entradas = total_entradas()
    saidas = total_saidas()
    saldo =  calcular_saldo()

    formatacao.cabeçalho('\033[7mRESUMO FINANCEIRO\033[m')

    print(f'Total de entradas: \033[34m{entradas:>15.2f}\033[m')
    print(f'Total de saídas: \033[34m{saidas:>17.2f}\033[m')
    print(f'Saldo: \033[32m{saldo:>27.2f}\033[m' if saldo >= 0 else f'Saldo: \033[31m{saldo:>27.2f}\033[m')





        



    
     


    


    
