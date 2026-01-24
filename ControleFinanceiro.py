from pathlib import Path
import json

class ControleFinanceiro:

    def __init__(self, caminho):

        self.arquivo = Path(caminho)
        self.checar_arquivo()

        
    def checar_arquivo(self):
        if not self.arquivo.exists():
            self.arquivo.write_text('[]', encoding='utf-8')  

            
    def ler_dados(self):
        conteudo = self.arquivo.read_text(encoding='utf-8')
        if conteudo.strip() == '':
            return []
        return json.loads(self.arquivo.read_text(encoding='utf-8'))
    

    def salvar_dados(self, dados):

        self.arquivo.write_text(
        json.dumps(dados, indent=2, ensure_ascii=False),
        encoding='utf-8'
        )


    def adicionar_movimento(self, data, descricao, valor, tipo):

        descricao = descricao.strip().lower()
        tipo = tipo.strip().lower()

        if tipo not in ('entrada', 'saida'):
            raise ValueError('Tipo inválido')

        dados = self.ler_dados()

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

        self.salvar_dados(dados)


    def listar_movimentos(self):

        dados = self.ler_dados()

        print(f'{'ID':<6} {'DATA':<11} {'DESCRIÇÃO':<20} {'VALOR':>12} {'TIPO':>7}')
        for l in dados:
            id_atual = l['id']
            data = l['data']
            descricao = l['descricao']
            valor = float(l['valor'])
            valor_formatado = (f"R$ {valor:.2f}")
            tipo = l['tipo']

            
            print(f'{id_atual:<6} {data:<11} {descricao:<20} {valor_formatado:>12} {tipo:>7}')


    def total_entradas(self):
    
        entradas = 0.0

        dados = self.ler_dados()

        for l in dados:
            valor = float(l['valor'])
            tipo = l['tipo'].strip().lower()
            if tipo == 'entrada':
                entradas += valor

        return entradas
    

    def total_saidas(self):
    
        saidas = 0.0

        dados = self.ler_dados()

        for l in dados:
            valor = float(l['valor'])
            tipo = l['tipo'].strip().lower()
            if tipo == 'saida':
                saidas += valor

        return saidas
    

    def calcular_saldo(self):
    
        return self.total_entradas() - self.total_saidas()
    
    
    def resumo_financeiro(self):

        return {
        'entradas' : self.total_entradas(),
        'saidas' : self.total_saidas(),
        'saldo' :  self.calcular_saldo()
        }

    

     



        
