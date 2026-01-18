from pathlib import Path
import formatação

movimentos = Path(r'Controle Financeiro\Controle-Financeiro-CLI\movimentos.txt')

def checar_arquivo():
    if not movimentos.exists():
        movimentos.open('w').close()
        
        
def adicionar_movimento(data, descricao, valor, tipo):
    checar_arquivo()

    descricao = descricao.strip().lower()
    tipo = tipo.strip().lower()
    id_atual = 1

    with movimentos.open('r', encoding='utf-8') as arquivo:
        
        for linhas in arquivo:
            linhas = linhas.strip()
            if linhas != '':
                id_atual += 1

    with movimentos.open('a', encoding='utf-8') as arquivo:

        arquivo.write(f'{id_atual};{data};{descricao};{valor};{tipo}\n')


def listar_movimento():
    checar_arquivo()
    vazio = True

    dados = []
    with movimentos.open('r', encoding='utf-8') as arquivo:
        for linhas in arquivo:
            linhas = linhas.strip()

            if linhas == '':
                continue

            dados.append(linhas.split(';'))
            vazio = False
                        
        if vazio:
            print('Nenhum movimento encontrado')
        else:
            print(f'{"ID":<6} {"DATA":<11} {"DESCRIÇÃO":<20} {"VALOR":>15} {"TIPO":>8}')

            for linha in dados:
                id_atual = linha[0]
                data = linha[1]
                descricao = linha[2]
                valor = float(linha[3])
                valor_formatado = f'R$ {valor:.2f}'
                tipo = linha[4].strip()
            
                print(f'{id_atual:<6} {data:<11} {descricao:<20} {valor_formatado:>15} {tipo:>8}')


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

    formatação.cabeçalho('\033[7mRESUMO FINANCEIRO\033[m')

    print(f'Total de entradas: \033[34m{entradas:>15.2f}\033[m')
    print(f'Total de saídas: \033[34m{saidas:>17.2f}\033[m')
    print(f'Saldo: \033[32m{saldo:>27.2f}\033[m' if saldo >= 0 else f'Saldo: \033[31m{saldo:>27.2f}\033[m')





        



    
     


    


    
