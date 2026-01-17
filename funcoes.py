from pathlib import Path

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
            
            
          


    
     


    


    
