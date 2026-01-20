from pathlib import Path
import formatacao
import json

movimentos = Path(r'Controle Financeiro\Controle-Financeiro-CLI\movimentos.txt')
movimentos_JSON  = Path(r'Controle Financeiro\Controle-Financeiro-CLI\movimentos_JSON.json')

def checar_arquivo():
    if not movimentos_JSON.exists():
        movimentos_JSON.write_text('[]', encoding='utf-8')   


def ler_dados():
    checar_arquivo()
    return json.loads(movimentos_JSON.read_text(encoding='utf-8')) 


def salvar_dados(dados):
    movimentos_JSON.write_text(
        json.dumps(dados, indent=2, ensure_ascii=False),
        encoding='utf-8'
    )


   
def adicionar_movimento(data, descricao, valor, tipo):
    checar_arquivo()

    descricao = descricao.strip().lower()
    tipo = tipo.strip().lower()
    
    # Le a lista atual JSON
    dados = json.loads(movimentos_JSON.read_text(encoding='utf-8'))

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

    movimentos_JSON.write_text(json.dumps(dados, indent=2, ensure_ascii=False), encoding='utf-8')



def listar_movimento():
    checar_arquivo()
    
    dados = ler_dados()

    

def calcular_saldo():
    checar_arquivo()
    entradas = 0
    saidas = 0
    vazio = True
    dados = []
    

    with movimentos.open('r', encoding='utf-8') as arquivo:
        for linhas in arquivo:
            linhas = linhas.strip()
            if linhas == '':
                continue

            vazio = False
            dados = linhas.split(';')
            tipo_entrada = dados[4].strip().lower()
            movimento = float(dados[3])

            if tipo_entrada == 'entrada':
                entradas += movimento
            elif tipo_entrada == 'saida':
                saidas += movimento
        saldo = entradas - saidas
        
        if vazio:
            print('Não existe nenhum movimento')
            return 0.0
        
        return saldo
       

def total_entradas():
    checar_arquivo()

    vazio = True
    entradas = 0.0
    sem_entrada = True

    with movimentos.open('r', encoding='utf-8') as arquivo:
        for linhas in arquivo:
            linhas = linhas.strip()
            if linhas == '':
                continue

            vazio = False
            dados = linhas.split(';')
            tipo_entrada = dados[4].strip().lower()
            movimento = float(dados[3])

            if tipo_entrada == 'entrada':
                entradas += movimento
                sem_entrada = False
            
        if vazio:
            print('Nenhuma movimentação encontrado.')

        if sem_entrada:
            print('Nenhuma entrada encontrada')
            return 0.0
        else:
            return entradas
        

def total_saidas():
    checar_arquivo()

    vazio = True
    saidas = 0.0
    sem_saida = True

    with movimentos.open('r', encoding='utf-8') as arquivo:
        for linhas in arquivo:
            linhas = linhas.strip()
            if linhas == '':
                continue

            vazio = False
            dados = linhas.split(';')
            tipo_entrada = dados[4].strip().lower()
            movimento = float(dados[3])

            if tipo_entrada == 'saida':
                saidas += movimento
                sem_saida = False
            
        if vazio:
            print('Nenhuma movimentação encontrado.')

        if sem_saida:
            print('Nenhuma saida encontrada')
            return 0.0
        else:
            return saidas
        


def resumo_financeiro():
    checar_arquivo()

    entradas = total_entradas()
    saidas = total_saidas()
    saldo =  calcular_saldo()

    formatacao.cabeçalho('\033[7mRESUMO FINANCEIRO\033[m')

    print(f'Total de entradas: \033[34m{entradas:>15.2f}\033[m')
    print(f'Total de saídas: \033[34m{saidas:>17.2f}\033[m')
    print(f'Saldo: \033[32m{saldo:>27.2f}\033[m' if saldo >= 0 else f'Saldo: \033[31m{saldo:>27.2f}\033[m')





        



    
     


    


    
